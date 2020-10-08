from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    date_init = fields.Datetime(string='Data inicio')
    date_final = fields.Datetime(string='Data final')

    @api.onchange('date_final')
    def _onchange_date_final(self):
        if self.date_init and self.date_final:

            float_time = (self.date_final - self.date_init)
            self.unit_amount = float_time.total_seconds() / 3600
