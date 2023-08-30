# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Developer(models.Model):
    _name = "developers.management.developer"
    _description = "Developers"

    TYPE_SELECTION = [
        ('front-end', 'Front-end'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out-stuff')
    ]

    name = fields.Char(string='Name', required=True)
    type = fields.Selection(selection=TYPE_SELECTION, string='Type', required=True)
    global_identification = fields.Char(string='Global Identification', compute='_compute_global_identification',
                                        store=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    birthdate = fields.Date(string='Birthdate')

    company_id = fields.Many2one('developers.management.company', string='Company')

    _sql_constraints = [('uniq_name', 'unique(name)', 'Choose another name - it has to be unique!')]

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for developer in self:
            if developer.name and developer.type:
                developer.global_identification = f"{developer.name}-{developer.type}"

    def action_save(self):
        if self:
            self.create({
                'name': self.name,
                'type': self.type,
                'company_id': self.company_id,
                'phone': self.phone,
                'email': self.email,
                'address': self.address,
                'birthdate': self.birthdate,
            })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'developers.management.company',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }


class Company(models.Model):
    _name = "developers.management.company"
    _description = "Companies with Developers relation"

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    developer_ids = fields.One2many('developers.management.developer', 'company_id', string='Developers')

    def action_save(self):
        if self:
            self.create({
                'name': self.name,
                'address': self.address,
            })
        for developer in self.developer_ids:
            developer.write({'company_id': self.id})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'developers.management.company',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
