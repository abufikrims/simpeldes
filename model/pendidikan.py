#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class pendidikan(models.Model):
    _name           = "cdn.pendidikan"
    _description    = "cdn.pendidikan"

    name            = fields.Char( required=True, string="Name",  help="")
    kategori        = fields.Selection(string='Kategori', selection=[('dasar', 'Dasar'), ('menengah', 'Menengah Umum'), ('kejuruan', 'Menengah Kejuruan'),  ('tinggi', 'Tinggi'),])
    
    keterangan      = fields.Char( string="Keterangan",  help="")
    active          = fields.Boolean( string="Active",  help="")

