# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

# class odoocustomization(models.Model):
#     _name = 'odoocustomization.odoocustomization'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class TechnicalApprovement(models.Model):

    _inherit = 'sale.order'

    able_to_approve = fields.Boolean(
        string="User can approve technical for orders?",
        compute='_compute_technical_approvement_right')

    is_technical_approved = fields.Boolean(
        string="Technical Approved",
        default=False,
        index=True,
        translate=True,
        required=True,
        readonly=True,
        states={
            'draft': [('readonly', False)],
        })

    quotation_type = fields.Selection(
        string="Quotation Type",
        selection=[('self-estimated', 'Self Estimated'),
                   ('vendor', 'Vendor Quotations')],
        default="self-estimated",
        required=True,
        readonly=True,
        states={'draft': [('readonly', False)],
                'sent': [('readonly', False)]})

    @api.model
    def _compute_technical_approvement_right(self):
        for record in self:
            record.able_to_approve = record.env['res.users'].has_group(
                'base.group_erp_manager')

    @api.constrains('is_technical_approved')
    def _check_technical_permission(self):
        for record in self:
            if not record.env['res.users'].has_group('base.group_erp_manager'):
                raise exceptions.ValidationError(
                    "You don't have permission to approve technical for orders"
                )
