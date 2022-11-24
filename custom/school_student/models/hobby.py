from odoo import models, fields


class Hobbies(models.Model):
    _name = 'hobby'

    name = fields.Char('Hobby')
