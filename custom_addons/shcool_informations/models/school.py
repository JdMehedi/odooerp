from datetime import date

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class School(models.Model):
    _name = "school.student"
    _description = "school details"

    name = fields.Many2one("res.partner", string='Student')
    class_id = fields.Integer(string='class')
    division = fields.Char(string='Division')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='age', compute='_compute_age')

    @api.onchange('name')
    def onchange_school(self):
        self.class_id = self.name

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for res in self:
            res.age = relativedelta(date.today(), res.dob).years

    @api.constrains('dob')
    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.dob > today:
                raise ValidationError('Invalid date of birth')
            elif (rec.class_id > 12) or (rec.class_id < 1):
                raise ValidationError('Invalid class')


class FindSchool(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:
            args += ['|', ('name', operator, name), ('email', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)


class Students(models.Model):
    # _name = 'student.list'
    _inherit = 'school.student'

    fathers_name = fields.Char(string='fathers_name')


class DataResult(models.Model):
    _inherit = 'res.partner'

    def orm_method(self):
        ormResult = self.env['res.partner'].search([])
        print('data:', ormResult)
