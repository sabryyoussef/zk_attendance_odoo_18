from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    biometric_device_ip = fields.Char(
        string='Biometric Device IP',
        help='IP address of the employee\'s biometric device'
    )
    zk_device_id = fields.Many2one(
        'zk.machine',
        string='Biometric Device',
        help='The biometric device this employee uses for attendance'
    )