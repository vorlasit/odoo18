from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class BroadChat(models.Model):
    _name = 'lod.broad.chat'

    _inherit = ['mail.thread', 'mail.activity.mixin']  
    _description = 'Broad Chat'

    name = fields.Char(string='Name', required=True,tracking=True)   
    broad_chat = fields.Html(string='Chat',tracking=False) 
    chat_list_ids = fields.One2many('lod.broad.chat.list', 'chat_id', string='Chat Lists')
    
    
    def create(self, vals):
        res = super().create(vals) 
        self.env['lod.broad.chat.list'].create({
            'broad_chat': res.broad_chat,
            'chat_id': res.id,
        }) 
        res.name = res.create_uid.name 
        res.broad_chat = ''
        return res

    
    def write(self, values): 
        result = super(BroadChat, self).write(values) 
        if 'broad_chat' in values: 
            self.env['lod.broad.chat.list'].create({
                'broad_chat': values.get('broad_chat', ''),
                'chat_id': self.id,
            }) 
            super(BroadChat, self).write({'broad_chat': ''})
        return result

 


class BroadChatList(models.Model):
    _name = 'lod.broad.chat.list'
    _description = 'Broad Chat List'
 
    broad_chat = fields.Html(string='Chat')
    chat_id = fields.Many2one('lod.broad.chat', string='Chat', ondelete='cascade')
