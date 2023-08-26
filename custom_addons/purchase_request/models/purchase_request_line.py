from odoo import fields, models, _


class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase request line'

    product_id = fields.Many2one(comodel_name='product.product', string='Product', tracking=True, required=True)
    product_code = fields.Char(string='Product Code', relted='product_id.system_code')
    uom_id = fields.Many2one(comodel_name='uom.uom', string='UOM', releted='product_id.uom_id')
    product_qty = fields.Float(string='Product Qty', tracking=True, digits='Product Unit of Measure')
    approved_qty = fields.Float(string='Approved Qty', tracking=True, digits='Product Unit of Measure')
    stock_qty = fields.Float(string='Stock Qty', tracking=True, digits='Product Unit of Measure')
    available_qty = fields.Float(string='Available Qty', tracking=True, digits='Product Unit of Measure',
                                 compute="_compute_available_qty", store=True)
    purchase_request_id = fields.Many2one('purchase.request', 'Purchase Request')
