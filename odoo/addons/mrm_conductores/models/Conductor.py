# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Conductor(models.Model):
    _name = 'mrm_conductores.conductor'
    _description = 'Conductor'
    
    dni = fields.Char('DNI', required=True, help='Introduzca el DNI del conductor')
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre')
    edad = fields.Integer('Edad', required=True, help='Introduzca la edad del conductor')
    grupo = fields.Selection([
        ('1', 'Grupo 1'),
        ('2', 'Grupo 2'),
        ('3', 'Grupo 3'),
        ('4', 'Grupo 4'),
        ('5', 'Grupo 5'),
    ], string='Grupo perteneciente')
    salario = fields.Float('Salario', help='Introduzca el salario del conductor')
    fecha_incorporacion = fields.Datetime('Fecha_incorporacion', help='Introduzca la fecha en la que se incorporó el conductor')
    disponible = fields.Boolean('Disponible', help='Marque si el conductor está o no trabajando')
    valoracion = fields.Integer('Valoracion', help='Indique el puntaje que le da al conductor del 1 al 5')
    horas_trabajadas = fields.Integer('Horas_trabajadas', help='Indice el número de horas trabajadas')
    ganado_dia = fields.Float('ganado_dia', help='Indique cuanto ha ganado el conductor al final del dia')
    
    
        
    