#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class hobi(models.Model):
    _name           = "cdn.hobi"
    _description    = "cdn.hobi"

    name            = fields.Char( required=True, string="Name",  help="")
    keterangan      = fields.Char( string="Keterangan",  help="")

    warga_ids       = fields.Many2many(comodel_name="cdn.warga",  string="Warga",  help="")
