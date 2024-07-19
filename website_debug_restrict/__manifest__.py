# Copyright 2022 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Website Debug Restrict",
    "summary": "Restrict debug mode for non-admin users",
    "version": "16.0.1.0.1",
    "author": "Ahmet Yiğit Budak",
    "license": "AGPL-3",
    "website": "https://github.com/yibudak/best-odoo-addons",
    "depends": ["base", "web", "website"],
    "data": [
        "security/res_users.xml",
    ],
    "installable": True,
    # Odoo Apps Store Specific #
    "images": ["static/description/banner.png"],
    "price": 0.00,
    "currency": "EUR",
    "category": "Website",
    "assets": {
        "web.assets_frontend": [
            "website_debug_restrict/static/src/xml/error_dialog.xml",
        ],
    },
}
