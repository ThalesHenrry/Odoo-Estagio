from odoo import fields, models, api, _


class inventario(models.Model):
    _name = "inventario"

#Campo Funcionario

    name = fields.Many2one("hr.employee", string="Funcionários")
    dep = fields.Many2one(related="name.department_id", string="Departamento")

    ip = fields.Integer(string="IP")
    ramal = fields.Integer(string="Ramal")
    pr = fields.Integer(string="Ponto de Rede")

 # Campos Hardware

    comp = fields.Many2one("product.product", string="Compartilhamento", domain=[('classe', '=', 'compartilhamento')])
    dum = fields.Many2one(related="comp.dependente", string="-")
    moni = fields.Many2one("product.product", string="Monitores", domain=[('classe', '=', 'monitor')])
    dois = fields.Many2one(related="moni.dependente", string="-")
    tm = fields.Many2one("product.product", string="Teclado/Mouse", domain=[('classe', '=', 'teclado/mouse')])
    dres = fields.Many2one(related="tm.dependente", string="-")
    esp = fields.Char()
    head = fields.Many2one("product.product", string="Telefone/Headset", domain=[('classe', '=', 'vendas')])

 #Campos Software

    acessor = fields.Many2one("product.product", string="Acesso Remoto", domain=[('classe', '=', 'remoto')])
    office = fields.Many2one("product.product", string="Office", domain=[('classe', '=', 'office')])
    comuni = fields.Many2one("product.product", string="Comunicação", domain=[('classe', '=', 'comunicação')])
    hitec = fields.Many2one(related="name.department_id", string="Hitec")





