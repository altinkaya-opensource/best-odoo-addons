# Copyright 2023 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, fields
from odoo.http import request
import json


class Website(models.Model):
    _inherit = "website"

    def get_cookie_allow_type(self):
        """
        Function to compute the cookie type in QWeb.
        """
        self.ensure_one()
        request_cookies = request.httprequest.cookies
        consent_dict = json.loads(request_cookies.get("website_cookies_bar", "{}"))
        if not consent_dict:
            return False
        if consent_dict.get("optional"):
            return "all"
        else:
            return "required_only"
