# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Website Google Consent Mode",
    "summary": "Consent mode lets you communicate your users’ cookie or app identifier consent status to Google."
    " Tags adjust their behavior and respect users’ choices.",
    "version": "16.0.1.0.1",
    "author": "Ahmet Yiğit Budak",
    "license": "AGPL-3",
    "website": "https://github.com/yibudak/best-odoo-addons",
    "depends": ["website", "website_enhanced_google_tag_manager"],
    "data": [
        # TEMPLATE
        "templates/website_template.xml",
    ],
    "installable": True,
    # Odoo Apps Store Specific #
    "images": ["static/description/banner.png"],
    "price": 0.00,
    "currency": "EUR",
    "category": "Website",
}
