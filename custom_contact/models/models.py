from odoo import models, fields, _, api


class Contact(models.Model):
    _inherit = 'res.partner'

    contact_source = fields.Selection(
        selection=[('website', 'Website'),
                   ('referral', 'Referral'),
                   ('campaign', 'Campaign'),
                   ('social_media', 'Social Media'),
                   ('cold_call', 'Cold Call')],
        string="Contact Source",  
        help="Track the origin of the contact",
        default='website'  
    )
