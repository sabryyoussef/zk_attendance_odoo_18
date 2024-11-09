from odoo import models, fields, api
import requests


class ZkApi(models.Model):  # Changed class name from MyCustomModel to ZkApi
    _name = 'zk.api.model'
    _description = 'ZK API Configuration'  # Changed description to be more professional
    
    name = fields.Char(string='Name', required=True)
    base_url = fields.Char(
        string='Base URL or IP Address', 
        required=True,
        help='Base URL or IP Address of the ZKTeco device API'
    )
    endpoint = fields.Char(
        string='API Endpoint', 
        required=True, 
        help='Endpoint to fetch attendance data from'
    )
    api_key = fields.Char(
        string='API Key', 
        required=True, 
        help='API key for authentication'
    )
    external_data = fields.Text(string='External Data')
    machine_count = fields.Integer(  # Moved field definition up with other fields
        string='Connected Devices',
        compute='_compute_machine_count'
    )

    def _compute_machine_count(self):
        for record in self:
            record.machine_count = self.env['zk.machine'].search_count([
                ('api_config_id', '=', record.id)
            ])

    def fetch_external_data(self):
        for record in self:
            if not record.base_url or not record.endpoint or not record.api_key:
                record.external_data = "Base URL, API endpoint, or API key is not defined."
                continue

            url = f"{record.base_url.rstrip('/')}/{record.endpoint.lstrip('/')}"  # Improved URL joining
            headers = {'Authorization': f"Bearer {record.api_key}"}

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()
                attendance_records = data.get('attendance_records', [])
                external_data_str = "\n".join(
                    [f"User ID: {rec['user_id']}, Timestamp: {rec['timestamp']}" 
                     for rec in attendance_records]
                )

                record.external_data = external_data_str or "No attendance records found."  # Added fallback message
            except requests.RequestException as e:
                record.external_data = f"Error fetching data: {str(e)}"
                
    def action_show_api_key(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'API Key',
                'message': self.api_key,
                'sticky': False,
                'type': 'info',
                'next': {
                    'type': 'ir.actions.act_window_close'
                }
            }
        }

    def action_view_machines(self):
        self.ensure_one()
        return {
            'name': 'Connected Devices',
            'type': 'ir.actions.act_window',
            'res_model': 'zk.machine',
            'view_mode': 'list,form',
            'domain': [('api_config_id', '=', self.id)],
            'context': {'default_api_config_id': self.id},
        }