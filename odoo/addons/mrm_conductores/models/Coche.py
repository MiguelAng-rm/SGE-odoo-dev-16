# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Coche(models.Model):
    _name = 'mrm_conductores.coche'
    _description = 'Coche'
    
    name = fields.Char('Matricula', required=True, help='Introduzca la matrícula del coche')
    marca = fields.Char('Marca', help='Introduzca la marca del coche')
    modelo = fields.Char('Modelo', help='Introduzca el modelo del coche')
    asientos = fields.Integer('Asientos', help='Introduzca el número de asientos del coche')
    conductores_ids = fields.Many2many('mrm_conductores.conductor', string='Conductores' ,relation="mrm_conductores_coche_conductor_rel")   
    reparandose = fields.Boolean('Reparandose', help='Indica si el coche está reparándose o no')
    imagen = fields.Image('Imagen', max_width=150, max_height=150)
