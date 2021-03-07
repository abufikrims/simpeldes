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
    active          = fields.Boolean( string="Active",  help="", default=True)

class nonformal_pendidikan(models.Model):
    _name           = "nonformal.pendidikan"
    _description    = "Data Riwayat Pendidikan Non Formal Warga"

    name            = fields.Char(string='Pendidikan/Kursus')
    lembaga         = fields.Char(string='Lembaga Penyelenggara')
    tahun_lulus     = fields.Char(string='Tahun Lulus')
    kota            = fields.Char(string='Kota')
    sertifikat      = fields.Boolean(string='Sertifikat?')

    warga_id        = fields.Many2one(comodel_name='cdn.warga', string='Nama Warga')
    
    
    
    


