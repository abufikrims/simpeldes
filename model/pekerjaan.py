#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class pekerjaan(models.Model):
    _name           = "cdn.pekerjaan"
    _description    = "cdn.pekerjaan"

    name            = fields.Char( required=True, string="Name",  help="")
    keterangan      = fields.Char( string="Keterangan",  help="")
    active          = fields.Boolean( string="Active",  help="")


