#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class suku(models.Model):
    _name           = "cdn.suku"
    _description    = "cdn.suku"

    name        = fields.Char( required=True, string="Name",  help="")
    keterangan  = fields.Char( string="Keterangan",  help="")
    active      = fields.Boolean( string="Active",  help="", default=True)


