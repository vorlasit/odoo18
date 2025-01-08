from odoo import http
from odoo.http import request
import json

class RestAPIController(http.Controller):
    
    @http.route('/api/get_chats', type='json', auth='public', website=True, methods=['GET'])
    def get_chats(self):
        # Fetch all chats
        chats = request.env['lod.broad.chat'].sudo().search([])
        chats_data = [{'id': chat.id, 'name': chat.name, 'chat': chat.broad_chat} for chat in chats]
        # return json.dumps({'status': 'success', 'data': chats_data})
        return {'status': 'success', 'data': chats_data}
     