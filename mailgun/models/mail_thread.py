##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

import logging
import requests

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def mailgun_fetch_message(self, message_url):
        api_key = self.env["ir.config_parameter"].sudo().get_param("mailgun.apikey")
        res = requests.get(
            message_url,
            headers={"Accept": "message/rfc2822"},
            auth=("api", api_key),
            verify=False,
        )
        self.message_process(False, res.json().get("body-mime"))
