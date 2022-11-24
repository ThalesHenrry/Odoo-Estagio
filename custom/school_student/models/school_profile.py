from odoo import models, fields, api
from odoo.exceptions import UserError


class School(models.Model):
    _inherit = "school"
    school_list = fields.One2many(comodel_name="school.student", inverse_name="school_id", string="School List")

