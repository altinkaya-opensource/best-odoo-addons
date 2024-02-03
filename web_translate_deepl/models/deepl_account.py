# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, api, fields, _
from odoo.exceptions import UserError
import requests


class DeepLAccount(models.Model):
    _name = "deepl.account"
    _description = "DeepL Account"

    name = fields.Char(string="Name", required=True)
    auth_key = fields.Char(string="Auth Key", required=True)
    translation_context = fields.Text(string="Translation Context")
    formality = fields.Selection(
        [
            ("default", "Default"),
            ("more", "More"),
            ("less", "Less"),
            ("prefer_more", "Prefer More"),
            ("prefer_less", "Prefer Less"),
        ],
        help="""
        default (default)
        more - for a more formal language
        less - for a more informal language
        prefer_more - for a more formal language if available, otherwise fallback to default formality
        prefer_less - for a more informal language if available, otherwise fallback to default formality
        """,
        string="Formality",
        default="default",
    )

    def _translate(self, text, source_lang, target_lang):
        """
        Connect to DeepL API and translate the given text.
        :param text:
        :param source_lang:
        :param target_lang:
        :return:
        """
        self.ensure_one()
        url = "https://api.deepl.com/v2/translate"
        headers = {
            "Authorization": "DeepL-Auth-Key %s" % self.auth_key,
            "User-Agent": "Odoo/12.0",
        }
        data = {
            "text": [text],
            # Convert Odoo's language code to DeepL's language code
            "target_lang": target_lang.split("_")[0].upper(),
            "source_lang": source_lang.split("_")[0].upper(),
            "formality": self.formality,
        }

        if self.translation_context:  # Add context
            data["context"] = self.translation_context

        response = requests.post(url, data=data, headers=headers, timeout=10)
        if response.status_code != 200:
            raise UserError(_("DeepL API Error: %s") % response.text)
        return response.json().get("translations")[0].get("text")

    def rpc_translate(self, company_id, target_lang, text):
        """
        Translate the given text to the target language.
        :param company_id: current company id
        :param target_lang: language code to translate
        :param text: text to translate
        :return:
        """
        company_sudo = self.env["res.company"].sudo().browse(company_id)
        if company_sudo and company_sudo.deepl_account_id:
            target_lang_id = self.env["res.lang"].browse(target_lang)
            base_lang_id = target_lang_id.tr_base_lang_id
            if not base_lang_id:
                raise UserError(
                    _("Base language not found! Set translation base language for %s")
                    % target_lang_id.display_name
                )

            return company_sudo.deepl_account_id._translate(
                text,
                base_lang_id.code,
                target_lang_id.code,
            )
        else:
            raise UserError(_("DeepL account not found for this company!"))

    def rpc_get_current_company_lang(self):
        """
        Get the current DeepL integration status and user language.
        These fields are used for form rendering.
        :return:
        """
        user_company = self.env.user.company_id
        return {
            "company_id": user_company.id,
            "deepl_enabled": bool(user_company.deepl_account_id),
            "user_lang": self.env.user.lang,
        }

    def action_test_connection(self):
        """
        Basic connection test for DeepL API.
        :return:
        """
        self.ensure_one()
        text_2_translate = "Hello World!"
        source_lang = "EN"
        target_lang = "TR"
        translation = self._translate(text_2_translate, source_lang, target_lang)
        raise UserError(
            _('DeepL API Success: "Hello World" translation: %s') % translation
        )
