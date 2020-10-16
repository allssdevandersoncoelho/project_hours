import json
import requests
from odoo import models, fields, _
from odoo.exceptions import UserError, Warning


class ProjectTask(models.Model):
    _inherit = 'project.task'

    register_ids = fields.One2many('register', inverse_name='project_task_id')

    def get_register(self):
        url_register = self.env['ir.config_parameter'].get_param(
            'url_register')

        try:
            response = requests.get(url=url_register, timeout=60)
        except Exception as ex:
            raise UserError(ex)

        if response.status_code == 200:
            recs = json.loads(response.text)
            for rec in recs:
                rec.update({
                    'project_task_id': self.id
                })
                register = self.env['register'].search([
                    ('call_code', '=', rec.get('call_code'))
                ])
                if not register:
                    self.env['register'].create(rec)
                else:
                    raise Warning(_("Registro já gravado"))
