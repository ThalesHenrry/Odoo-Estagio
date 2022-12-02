from odoo import fields, models, api


class Funcionarios(models.Model):
    _name = "func"
    _order = 'name'

    name = fields.Char()
    cargo = fields.Char()
    school_id = fields.Many2one("school", string="School")
    data_hora = fields.Datetime("Data e Hora", default=fields.Datetime.now(), readonly=1)
    data_e = fields.Date(string="Data de Entrada")
    data_s = fields.Date(string="Data de Saida")