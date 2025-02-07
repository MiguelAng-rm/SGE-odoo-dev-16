# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Coche(models.Model):
    _name = 'mrm_conductores.coche'
    _description = 'Coche'
    
    matricula = fields.Char('Matricula', required=True, help='Introduzca la matrícula del coche')
    marca = fields.Char('Marca', help='Introduzca la marca del coche')
    modelo = fields.Char('Modelo', help='Introduzca el modelo del coche')
    asientos = fields.Integer('Asientos', help='Introduzca el número de asientos del coche')
    #propietario_ids = fields.One2many('comodel_name', 'inverse_field_name', string='propietario')    
    reparandose = fields.Boolean('Reparandose', help='Indica si el coche está reparándose o no')
