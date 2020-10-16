import json
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class WebApi(CustomerPortal):
    @http.route(['/teste'], type='json', auth='public', csrf=False)
    def getteste(self, token=None, redirect=None, **kwargs):
        '''
        Teste para rota de consulta project task.
        '''
        if kwargs.get('project_id'):
            tasks = request.env['project.task'].sudo().search([
                ('project_id', '=', kwargs.get('project_id'))
            ])

        else:
            tasks = request.env['project.task'].sudo().search([])

        task_dict = {
          'data': []
        }
        if tasks:
            for task in tasks:
                task_dict.get('data').append({
                  'id': task.id,
                  'name': task.name,
                  'project': task.project_id.name
                })

        return task_dict
