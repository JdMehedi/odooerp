# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class request_for_qoutation(models.Model):
#     _name = 'request_for_qoutation.request_for_qoutation'
#     _description = 'request_for_qoutation.request_for_qoutation'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
