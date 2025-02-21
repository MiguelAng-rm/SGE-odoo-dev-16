# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'mrm_conductores.servicio'
    _description = 'Servicio'
    
    
    name = fields.Char('Codigo del servicio', required=True, help='Muestra el código del servicio actual')
    distancia = fields.Float('Distancia',required=True, help='Indique la distancia del servicio')
    precio = fields.Float('Precio',required=True, help='Indique el coste del servicio')
    duracion_minutos = fields.Integer('Duracion_minutos', help='Introduce el tiempo aproximado en minutos de la duración del trayecto')
    clientes_ids = fields.One2many('mrm_conductores.cliente', 'servicio_id', string='Clientes')
    