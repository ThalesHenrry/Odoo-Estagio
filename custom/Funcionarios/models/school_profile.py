from odoo import models, fields, api
from odoo.exceptions import UserError


class School(models.Model):
    _inherit = "school"

    func_list = fields.One2many(comodel_name="func", inverse_name="school_id", string="Funcionarios")


