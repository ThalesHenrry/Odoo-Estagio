from lxml import etree
from odoo import models, fields, api
from odoo.exceptions import UserError


class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char()
    school_id = fields.Many2one("school", string="School")
    hobby_list = fields.Many2many("hobby", "school_hobby_rel", "student_id", "hobby_id", string="Hobby List")

    is_virtual_school = fields.Boolean(realted="school_id.is_virtual_class", string="Suporte Aula Online", store=True)
    school_address = fields.Text(related="school_id.adress", string="Address")
    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string="Student Fees")
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference([('school', 'school'),
                               ('account.move', 'Invoice')],
                              string="Reference Field")
    active = fields.Boolean(string="Ativo")
    data_nasc = fields.Date(string="Data de Nascimento")
    idade = fields.Integer(string="Idade")


    @api.model
    def create(self, values):
        print("Before Edit Values ", values)
        values['active'] = True                     # Deixa automaticamente o aluno como ativo
        print("After Edit Values ", values)
        rtn = super(school_student, self).create(values)
        return rtn

    def copy(self, default={}):
        default['active'] = False
        default['name'] = "copy (" + self.name + ")"  # Faz a duplicata do estudante se chamar copy + nome do estudante copiado
        rtn = super(school_student, self).copy(default=default)
        print("Return statement ", rtn)
        return rtn

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(school_student, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                          submenu=submenu)

        if view_type == 'tree':
            doc = etree.XML(res['arch'])
            school_field = doc.xpath("//field[@name='school_id']")
            if school_field:
                school_field[0].addnext(etree.Element('field', {'string': 'Total Fees', 'name': 'total_fees'}))
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res


        # Campo interativo mostrando mensagem de erro

    # def write(self, values):
    #     rtn = super(school_student, self).write(values)
    #     if not self.hobby_list:
    #         raise UserError("Por favor, selecione o Hobby")
    #     return rtn

    # @api.model
    # def create(self, vals):
    #     rtn = super(school_student, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("Lista está vazia!"))
    #     return rtn
