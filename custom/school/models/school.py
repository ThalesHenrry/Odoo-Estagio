from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SchoolProfile(models.Model):
    _name = "school"

    # O "trim" por default é True, use apenas para alternar para false
    name = fields.Char(string="Nome da Escola", help="This is School Name", required=True,
                       size=45, trim=True)
    email = fields.Char(string="Email", size=45)
    phone = fields.Char(string="Telefone", size=15)
    is_virtual_class = fields.Boolean(string="Suporte para Aula Online?")
    school_rank = fields.Integer(string="Rank", default="100", required=True, size=6)
    result = fields.Float(string="Resultado")
    adress = fields.Text(string="Endereço")
    time_date = fields.Datetime("Data e Hora", default=fields.Datetime.now(), readonly=1)
    type_school = fields.Selection([("public", "Escola Pública"), ("private", "Escola Particular")])
    documents = fields.Binary(string="Documentos")
    name_docs = fields.Char(string="Nome Documentos")
    school_image = fields.Image(string="Imagens da Escola", max_widht=100, max_height=100,
                                help="Essa é a imagem da escola")
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto Rank")
    teste = fields.Char(name="space")



    # restrição de nome unico
    _sql_constraints = [
        ('name_unique', 'unique (name)', "Por favor cadastre uma nova escola, essa já existe.")
    ]

    @api.depends("type_school")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.type_school == "private":
                rec.auto_rank = 50  # Ranking automatico para escolas
            elif rec.type_school == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    def name_get(self):
        student_list = []
        for school in self:
            name = school.name  # Aparecer tipo, ao lado do nome da escola
            if school.type_school:
                name += " ({})".format(school.type_school)
            student_list.append((school.id, name))
        return student_list

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        print("Name ", name)
        print("Args ", args)
        print("operator ", operator)  # pesquisas gerais no campo escola
        print("limit ", limit)
        if name:
            records = self.search(
                ['|', '|', ('name', operator, name), ('email', operator, name), ('type_school', operator, name)])
            return records.name_get()
        return super(SchoolProfile, self).name_search(name=name, args=args, operator=operator, limit=limit)


