from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase description'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    _rec_name = 'name'

    reference = fields.Char(string="Requisition Reference", readonly=True, required=True, default=lambda self: _("New"),
                            tracking=True, force_save="1")
    name = fields.Char(String='Purchase Requisition', required=True, default='New', tracking=True)
    requisition_date = fields.Datetime(String='Requisition Date', default=fields.Datetime.now(), tracking=True,
                                       required=True)
    approved_date = fields.Datetime(String='Approve Date', required=True, strore=True)
    required_date = fields.Datetime(String='Required Date', default=fields.Datetime.now(), readonly=True, required=True)
    company_id = fields.Many2one(comodel_name='res.company', required=True, tracking=True, readonly=True,
                                 default=lambda self: self.env.company.id)
    budget_id = fields.Char(String='Budget', default='CCL-23-24 Fiscal year', readonly=True, fore_save=True)
    department_id = fields.Char(String='Department Id', default='Devops', required=True, tracking=True,
                                readonly=True)
    attachment = fields.Many2many(comodel_name='ir.attachment', relation='purchase_request_ir_attachment_rel',
                                  column1='purchase_request_id', column2='attachment_id', string='Attachment',
                                  tracking=True)
    # line_ids = fields.One2many('purchase.request.line', 'purchase_request_id')
    initiator_approver = fields.Many2one(comodel_name='res.users', tracking=True)
    hod_approver = fields.Many2one(comodel_name='res.users', tracking=True)
    gm_approver = fields.Many2one(comodel_name='res.users', tracking=True)
    priority = fields.Selection(string='Priority', selection=[('high', 'High'), ('medium ', 'Medium'), ('low', 'Low')],
                                required=True, tracking=True)
    requisition_type = fields.Selection(string='Requisition Type',
                                        selection=[('local', 'Local Purchase'), ('foreign', 'Foreign Purchase'),
                                                   ('direct', 'Direct Purchase')], required=True, tracking=True)
    pr_type = fields.Selection(string='Pr Type', selection=[
        ('factory', 'Factory PR'),
        ('head_office', 'Head Office PR'),
        ('it', 'It PR')
    ], tracking=True, required=True, default='factory', )
    service = fields.Selection(string='Service', selection=[
        ('product', 'Storable Products'),
        ('service', 'Service')
    ], tracking=True)
    state = fields.Selection(string='Status', selection=[
        ('draft', 'Draft'),
        ('scm', 'SCM'),
        ('pm', 'PM'),
        ('coo', 'COO'),
        ('approved', 'Approved'),
        ('canceled', 'Canceled'),
        ('closed', 'Closed'),
    ], required=True, tracking=True, default='draft')
    remarks = fields.Text(string='Remarks', tracking=True)
    rfq_count = fields.Integer(compute='_compute_rfq_count')
    line_ids = fields.One2many('purchase.request.line', 'purchase_request_id', 'Products', required=True)

    # is_rfq_allowed = fields.Boolean(compute='_compute_is_rfq_allowed', search='_search_is_rfq_allowed')

    @api.constrains('line_ids')
    def product_line_validation(self):
        if not self.line_ids:
            raise ValidationError(_('Product line cannot be empty, please add some product'))
        if any(line.product_qty <= 0 for line in self.line_ids):
            raise ValidationError('Quantity must be greater than 0.')
        if not any(0 < line.approved_qty <= line.product_qty for line in self.line_ids):
            raise ValidationError('Approved quantity must be greater than 0 or less than or equal product quantity.')

    def action_submit(self):
        self.write({'state': 'scm'})

    def action_hod_submit(self):
        self.write({'state': 'pm'})
        return {'type': 'ir.actions.act_window_close'}

    # def action_coo_submit(self):
    #     self.write({'state': 'coo'})
    #     return {'type': 'ir.actions.act_window_close'}

    def action_approved_submit(self):
        self.state = 'approved'
        return {'type': 'ir.actions.act_window_close'}

    # def type_validation(self):
    #     if self.pr_type != 'it':
    #         raise ValidationError(_('Pr type should be IT.'))

    def action_cancel(self):
        self.write({'state': 'canceled'})

    def action_pr_close(self):
        self.write({'state': 'closed'})

    def action_pr_amendment(self):
        self.write({'state': 'draft'})
        if '/AMD' in self.name:
            amd_name = self.name.split('-')
            cnvt_data = int(amd_name[1])
            self.name = amd_name[0] + '-' + str(cnvt_data + 1)
        else:
            self.name += '/AMD-1'

    @api.model
    def create(self, vals_list):
        vals_list['reference'] = self.env['ir.sequence'].next_by_code('purchase.request') or _('New')
        res = super(PurchaseRequest, self).create(vals_list)
        return res
