{
    'name': 'Biometric Device Integration',
    'version': '18.0.1.0.0',
    'summary': 'Integrating Biometric Device (Model: ZKteco uFace 202) With HR Attendance (Face + Thumb)',
    'description': 'This module integrates Odoo with the biometric device(Model: ZKteco uFace 202)',
    'category': 'Human Resources/Attendance',
    'author': 'Dr.Sabry Youssef',
    'company': 'vet_brains',
    'website': "https://www.vetbrains.com",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/zk_machine_view.xml',
        'views/zk_machine_attendance_view.xml',
        'views/zk_api_key_view.xml',
        'views/hr_employee_views.xml',
        'data/download_data.xml',
        
    ],
    'assets': {
        'web.assets_backend': []
    },
    'images': ['static/description/banner.gif'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}