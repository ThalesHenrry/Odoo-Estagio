from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    total_fees = fields.Float(string="Fees")

    def update_student_fees(self):
        print("oi")

        self.env['school.student'].browse(self._context.get("active_ids")).update({'total_fees': self.total_fees})

        return True


class StudentFeesUpdateExtendWizard(models.TransientModel):
    _inherit = "student.fees.update.wizard"

    parent_name = fields.Char(string="Parent Name")

    def update_student_fees(self):
        print("This is inherited def update_student_fees(self): method....")

        return super(StudentFeesUpdateExtendWizard, self).update_student_fees()
