from odoo import fields, models


class Register(models.Model):
    _name = 'register'

    call_type = fields.Char(string='Tipo de Ligação')
    source_number = fields.Char(string='Número')
    call_datetime = fields.Char(string='Data da Ligação')
    destine_number = fields.Char(string='Destino')
    call_code = fields.Char(string='Código')
    project_task_id = fields.Many2one('project.task')
