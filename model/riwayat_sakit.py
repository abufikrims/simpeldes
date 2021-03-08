from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class riwayat_sakit(models.Model):
    _name           = "riwayat.sakit"
    _description    = "Data Riwayat Sakit Warga"
    _rec_name       = "penyakit_id"

    #name            = fields.Char(string='Nama Sekolah')
    penyakit_id     = fields.Many2one(comodel_name='ref.penyakit', string='Jenis Penyakit')
    tahun_sakit     = fields.Char(string='Tahun Sakit')
    lama_sakit      = fields.Integer(string='Lama Sakit (hari)')
    dirawat         = fields.Char(string='Dirawat di')
    keterangan      = fields.Char(string='Keterangan')
    
    warga_id        = fields.Many2one(comodel_name='cdn.warga', string='Nama Warga')
    