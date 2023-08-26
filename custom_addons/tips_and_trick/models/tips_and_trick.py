from odoo import models, fields


class School(models.Model):
    _name = "tips.tricks"
    _description = "Tips details"

    name = fields.Char(string='name')
    number = fields.Integer(string='number')
    float_no = fields.Float(string='Float No')
    document = fields.Binary()
    true = fields.Boolean(string='True?')
    image = fields.Image()
    date = fields.Date()
    date_time = fields.Datetime()
    yes_no = fields.Selection([
        ('yes','Yes'),
        ('no','No')
    ], string='Yes or No')
    product_id = fields.Many2one('product.product',string='product')
    product_ids = fields.Many2one('product.product')
    currency_id = fields.Many2one('res.currency',string='currency')
    price = fields.Monetary()
