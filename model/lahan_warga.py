#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class lahan_warga(models.Model):
    _name           = "cdn.lahan_warga"
    _description    = "cdn.lahan_warga"

    name            = fields.Char( required=True, string="Name",  help="")
    jenis_lahan     = fields.Selection(selection=[('pangan','LAHAN TANAMAN PANGAN'),('kebun','LAHAN TANAMAN PERKEBUNAN'),('hutan','LAHAN HUTAN')],  string="Jenis lahan",  help="")


