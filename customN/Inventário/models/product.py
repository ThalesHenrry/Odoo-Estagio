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

    estoque_id = fields.Selection([('software', 'SOFTWARE'),
                                   ('hardware', 'HARDWARE')], string="Estoque")


class prod(models.Model):
    _inherit = "product.product"

    dependente = fields.Many2one('product.product', string="Dependentes")

    comp_id = fields.One2many('inventario', 'comp', string="Usuário")
    moni_id = fields.One2many('inventario', 'moni', string="Monitor")
    tm_id = fields.One2many('inventario', 'tm', string="Teclado/Mouse")
    head_id = fields.One2many('inventario', 'head', string="Telefone/Headphone")

    prod_tipo = fields.Selection(related="product_tmpl_id.estoque_id", string="Estoque")
