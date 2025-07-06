from odoo import models, fields, _, api


class Contact(models.Model):
    _inherit = 'res.partner'

    custom_contact_note = fields.Text('Custom Contact Notes')
