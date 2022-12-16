from odoo import models, fields, api
from odoo.exceptions import UserError


class product(models.Model):
    _inherit = "product.template"

    classe = fields.Selection([('remoto', 'Remoto'),
                               ('office', 'Office'),
                               ('comunicação', 'Comunicação'),
                               ('hitec', 'Hitec'),
                               ('compartilhamento', 'Compartilhamento'),
                               ('monitor', 'Monitor'),
                               ('teclado/mouse', 'Teclado/Mouse'),
                               ('conector', 'Conector'),
                               ('Cabo', 'Cabo'),
                               ('vendas', 'Vendas')])


class prod(models.Model):
    _inherit = "product.product"

    dependente = fields.Many2one('product.product', string="Dependentes")

    comp_id = fields.One2many('inventario', 'comp', string="Usuário")
    moni_id = fields.One2many('inventario', 'moni')
    tm_id = fields.One2many('inventario', 'tm')
    head_id = fields.One2many('inventario', 'head')
