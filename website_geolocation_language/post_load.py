# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import http
from odoo.tools.func import lazy_property
import babel.core
import logging

_logger = logging.getLogger(__name__)


def post_load():
    """
    Parsing country code into language code is copied from:
    https://github.com/OCA/OCB/blob/01b012346f25842c35be1bbe184e455cc00259c7/odoo/http.py#L1316
    """
    _logger.info(
        "website_geolocation_language: Monkey patching http.Request.best_lang"
        " to use Geolocation resolved language."
    )
    _best_lang_orig = http.Request.best_lang

    @lazy_property
    def _best_lang_from_geolocation(self):
        ip_lang = None
        best_lang = _best_lang_orig.__get__(self, cls=http.Request)
        geolocation_resolve = http.Request._geoip_resolve(self)
        if geolocation_resolve and geolocation_resolve.get("country_code"):
            country_code = geolocation_resolve["country_code"]
            try:
                code, territory, _, _ = babel.core.parse_locale(country_code, sep="-")
                if territory:
                    lang = f"{code}_{territory}"
                else:
                    lang = babel.core.LOCALE_ALIASES[code]
                ip_lang = lang
            except (ValueError, KeyError):
                pass
        return ip_lang or best_lang

    http.Request.best_lang = _best_lang_from_geolocation
