from odoo import fields, models, api, _


class estoque(models.Model):
    _name = "estoque"

    topo = fields.Selection([('compartilhamento', 'Compartilhamento'),
                               ('monitor', 'Monitor'),
                               ('teclado/mouse', 'Teclado/Mouse'),
                               ('conector', 'Conector'),
                               ('suporte', 'Suporte'),
                               ('vendas', 'Vendas')], string="Grupo")

    tabela = fields.Many2many("product.product", string="Itens")
    tmpl_id = fields.Many2one("product.template")
    classe = fields.Selection(related="tmpl_id.classe", string="Classe")

    data = fields.Date(string="Data Registro", default=fields.Date.today(), readonly="1")

    func = fields.Char()