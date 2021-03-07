from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class riwayat_pendidikan(models.Model):
    _name           = "riwayat.pendidikan"
    _description    = "Data Riwayat Pendidikan Warga"

    name            = fields.Char(string='Nama Sekolah')
    pendidikan_id   = fields.Many2one(comodel_name='cdn.pendidikan', string='Jenjang')
    tahun_lulus     = fields.Char(string='Tahun Lulus')
    jurusan         = fields.Char(string='Jurusan')

    warga_id        = fields.Many2one(comodel_name='cdn.warga', string='Nama Warga')
    
    
    
    
    
    