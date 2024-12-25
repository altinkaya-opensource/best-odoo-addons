
![Odoo Version](https://img.shields.io/badge/maturity-production/stable-green)  ![Odoo Version](https://img.shields.io/badge/odoo_version-16.0-blue)  ![Licence](https://img.shields.io/badge/licence-LGPL--3-lightgrey)
# Website Google Consent Mode

WARNING: This functionality is already exist in Odoo 16.0 since September 2024

This module facilitates the integration of Odoo with Google Tag Manager's consent mode. When a user consents to required cookies, the module transmits this consent information to Google Tag Manager. Additionally, if the user consents to optional cookies, the module will also send this extended consent information (such as for personalized ads) to Google Tag Manager.
## Installation:

1. Clone this repository.
2. Add this directory to your addons path (e.g. `--addons-path=addons,path/to/this/repo`).
3. Install the module `website_google_consent_mode`.
4. There is no need to configure anything. This module works with Odoo's built-in cookie consent mechanism.

## Authors:

- [Ahmet Yiğit Budak](https://github.com/yibudak)

## Contribution:

We welcome your contributions to our project.

- This project is licensed under LGPL-3. Your contributions will be under the same license.
- We aim to adhere to **OCA quality standards** for all modules and content in this project.
- General information on contributing can be found on the [Contribute to OCA](https://odoo-community.org/page/Contribute) page.
- General rules for adding modules can be accessed at https://github.com/OCA/maintainer-tools/blob/master/CONTRIBUTING.md
- Quality control can be simplified using [OCA's quality control tools](https://github.com/OCA/maintainer-quality-tools).
