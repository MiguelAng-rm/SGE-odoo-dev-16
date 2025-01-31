# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'
    
    name = fields.Char('Nombre', required=True, help='Introduce tu nombre')
    precio = fields.Float('Precio', help='Introduce el precio')
    ejemplares = fields.Integer('Ejemplares', help='Introduce los ejemplares disponibles')
    fecha_compra = fields.Date('Fecha_compra', help='Introduce la fecha de la compra del libro')
    segmano = fields.Boolean('Segunda mano', help='Muestra si es o no de segunda mano')
    estado = fields.Selection([
        ('0', 'Mal estado'),
        ('1', 'Aceptable'),
        ('2', 'Buen estado'),
        ('3', 'En perfecto estado')
    ], string='Estado del libro', default='0')
        