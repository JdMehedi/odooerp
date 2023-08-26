from odoo import models, fields


class BaseExtend(models.Model):
    _inherit = "school.student"

    mothers_name = fields.Char(string='mothers name')

