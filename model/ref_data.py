#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class ref_data(models.Model):
    _name           = "cdn.ref_data"
    _description    = "cdn.ref_data"

    name            = fields.Char( required=True, string="Name",  help="")
    jns_ref         = fields.Char( string="Jns ref",  help="")
    keterangan      = fields.Char( string="Keterangan",  help="")
    active          = fields.Boolean( string="Active",  help="")


