# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, fields


class Base(models.AbstractModel):
    _inherit = "base"

    def get_field_translations(self, field_name, langs=None):
        """
        Inherited to add "base_lang" to the translation data.
        """
        res = super().get_field_translations(field_name, langs=langs)
        if res and len(res) == 2:
            translations = res[0]
            for tr in translations:
                lang_id = self.env["res.lang"].search([("code", "=", tr["lang"])])
                if lang_id and lang_id.tr_base_lang_id:
                    tr["base_lang"] = lang_id.tr_base_lang_id.code
                else:
                    tr["base_lang"] = False
        return res
