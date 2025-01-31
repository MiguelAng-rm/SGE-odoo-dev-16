# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mrm_conductores(models.Model):
#     _name = 'mrm_conductores.mrm_conductores'
#     _description = 'mrm_conductores.mrm_conductores'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

