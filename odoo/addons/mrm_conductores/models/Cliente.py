# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'mrm_conductores.cliente'
    _description = 'Cliente'
    
    nombre = fields.Char('Nombre',required=True, help='Indique el nombre del cliente')
    correo = fields.Char('Correo',required=True, help='Indique el correo del cliente')
    tarjeta_bancaria = fields.Char('Tarjeta_bancaria', help='Indique los números de la tarjeta bancaria')
    edad = fields.Integer('Edad',required=True, help='Indique la edad del cliente')
    disponible = fields.Boolean('Disponible', help='Indique si el cliente está disponible para solicitar un servicio')
    
    
    