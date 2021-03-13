#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class warga(models.Model):

    _name = "cdn.warga"
    _inherits = {'res.partner': 'partner_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Tabel warga - inherits res.partner"

    nama = fields.Char(required=True, string="Nama", index=True,  help="Nama Lengkap Warga")
    partner_id = fields.Many2one("res.partner", string='Partner ID', required=True, ondelete="cascade")
    
    # Tambahan data alamat - untuk melengkapi res.partner (street, street2, city, state, zip)
    rt_rw           = fields.Char(string="RT/RW")
    propinsi_id     = fields.Many2one(comodel_name='ref.propinsi', string='Propinsi')
    kota_id         = fields.Many2one(comodel_name='ref.kota', string='Kabupaten/Kota')
    kecamatan_id    = fields.Many2one(comodel_name='ref.kecamatan', string='Kecamatan')
    desa_id         = fields.Many2one(comodel_name='ref.desa', string='Desa/Kelurahan')
    
    
    nik             = fields.Char( string="NIK", required=True, index=True, help="Nomor Induk Keluarga sesuai KTP/KK")
    no_kk           = fields.Char( string="No Kartu Keluarga",  help="Nomor Kartu Keluarga")
    status_keluarga = fields.Selection(selection=[('kepala keluarga','Kepala Keluarga'),('suami','Suami'),('istri','Istri'),('anak','Anak'),('menantu','Menantu'),('cucu','Cucu'),('lainnya','Lainnya')],  string="Status Keluarga", required=True,  help="")
    jenis_kel       = fields.Selection(selection=[('pria','Pria'),('wanita','Wanita')],  string="Jenis Kelamin", required=True, help="")
    tmp_lahir       = fields.Char( string="Tempat Lahir",  help="Isikan dengan kota tempat kelahiran")
    tgl_lahir       = fields.Date( string="Tanggal Lahir",  help="Isikan dengan tanggal kelahiran")
    agama           = fields.Selection([('islam', 'Islam'), ('katolik', 'Katolik'), ('protestan', 'Protestan'), ('hindu', 'Hindu'), ('budha', 'Budha'),('konghucu','KongHu Chu')], string='Agama')
    kewarganegaraan = fields.Selection(selection=[('wni','WNI'),('wna','WNA')],  string="Kewarganegaraan", default="wni", help="Kewarganegaraan")
    gol_darah       = fields.Selection(selection=[('A','A'),('B','B'),('AB','AB'),('O','O'),('A+','A+'),('B+','B+'),('AB+','AB+'),('O+','O+'),('Tidak Tahu','TIDAK TAHU')],  string="Golongan Darah",  help="Isikan dengan golongan darah atau TIDAK TAHU jika Anda belum pernah periksa")
    bisa_baca       = fields.Boolean( string="Bisa Membaca ?", default=True, help="")
    is_cacat        = fields.Boolean( string="Kelainan Fisik Mental", default=False, help="")
    nama_ayah       = fields.Char( string="Nama Ayah",  help="")
    nama_ibu        = fields.Char( string="Nama Ibu",  help="")
    status_kawin    = fields.Selection(selection=[('belum kawin','BELUM KAWIN'),('kawin','KAWIN'),('cerai hidup','CERAI HIDUP'),('cerai mati','CERAI MATI')],  string="Status kawin",  help="")
    no_akte_kawin   = fields.Char( string="No Akte Perkawinan",  help="")
    no_akte_cerai   = fields.Char( string="No Akte Perceraian",  help="")
    ada_akte_kawin  = fields.Boolean( string="Akte Kawin", default=False, help="")
    ada_akte_cerai  = fields.Boolean( string="Akte Cerai", default=False, help="")
    status_tmp_tinggal = fields.Selection(selection=[('01','Milik Sendiri'),('02','Milik Orang Tua'),('03','Milik Keluarga'),('04','Sewa/Kontrak'),('05','Pinjam Pakai'),],  string="Status tmp tinggal",  help="")


    pendidikan_id   = fields.Many2one(comodel_name="cdn.pendidikan",  string="Pendidikan",  help="")
    pekerjaan_id    = fields.Many2one(comodel_name="cdn.pekerjaan",  string="Pekerjaan",  help="")
    suku_id         = fields.Many2one(comodel_name="cdn.suku",  string="Suku",  help="")
    hobi_ids        = fields.Many2many(comodel_name="cdn.hobi",  string="Hobi",  help="")
    ref_data_id     = fields.Many2one(comodel_name="cdn.ref_data",  string="Ref data",  help="")

    # Riwayat Pendidikan
    riwayat_pendidikan_ids      = fields.One2many(comodel_name='riwayat.pendidikan', inverse_name='warga_id', string='Riwayat Pendidikan')
    pendidikan_nonformal_ids    = fields.One2many(comodel_name='nonformal.pendidikan', inverse_name='warga_id', string='Pendidikan Non Formal')

    # Data Kesehatan
    peserta_kb      = fields.Boolean(string='Peserta KB')
    jenis_kb        = fields.Selection(string='Program KB', selection=[('iud', 'IUD'), ('pil', 'PIL KB'),('kondom', 'KONDOM'),('suntik', 'SUNTIK'),('implan', 'IMPLAN'),('tubektomi', 'TUBEKTOMI/VASEKTOMI'),('lainnya', 'LAINNYA'),])
    riwayat_sakit_ids   = fields.One2many(comodel_name='riwayat.sakit', inverse_name='warga_id', string='Riwayat Sakit')
    
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search([('nik',operator, name)] + args, limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return recs.name_get()
    

    @api.onchange('nama')
    def _onchange_nama(self):
        self.name = self.nama

    @api.onchange('kota_id')
    def _onchange_kota_id(self):
        self.city = self.kota_id.name
        
