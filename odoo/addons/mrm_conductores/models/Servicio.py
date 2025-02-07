# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'mrm_conductores.servicio'
    _description = 'Servicio'
    
    distancia = fields.Float('Distancia',required=True help='Indique la distancia del servicio')
    precio = fields.Float('Precio',required=True help='Indique el coste del servicio')
    duracion_minutos = fields.Integer('Duracion_minutos', help='Introduce el tiempo aproximado en minutos de la duración del trayecto')
    
    