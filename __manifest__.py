{
  'name': 'Project hours',
  'version': '11.0.1.0.0',
  'summary': 'project hours',
  'category': 'project',
  'author': 'teste',
  'depends': [
    'helpdesk_timesheet',
  ],

  'data': [
    # Data
    'data/ir.config_parameter.xml',

    # Views
    'views/helpdesk_views.xml',

    # Security
    'security/ir.model.access.csv'
  ],
  'installable': True,
  'auto_install': False,
  'application': False,
}
