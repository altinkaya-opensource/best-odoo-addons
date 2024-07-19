# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "Website GeoIP Language",
    "summary": "Automatically use visitor's language based on their IP address.",
    "description": """
    This module automatically sets the language of the visitor based on their IP address.
    """,
    "version": "16.0.1.0.0",
    "author": "Ahmet Yiğit Budak",
    "website": "https://github.com/yibudak/best-odoo-addons",
    "license": "LGPL-3",
    "depends": [
        "base",
        "website",
    ],
    "data": [],
    "post_load": "post_load",
    "installable": True,
    # Odoo Apps Store Specific #
    "images": ["static/description/banner.png"],
    "price": 0.00,
    "currency": "EUR",
    "category": "Website",
}
