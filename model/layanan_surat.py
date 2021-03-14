STATES = [('draft','Pengajuan'),('diperiksa','Diperiksa'),('disetujui','Disetujui'),('selesai','Selesai')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class layanan_surat(models.Model):

    _name           = "cdn.layanan_surat"
    _description    = "Template Model untuk Layanan Surat - di inherits berdasarkan jenis suratnya"

    name            = fields.Char( required=True, default="New", readonly=True,  string="Nomor Pengajuan",  help="")
    sr_no_surat     = fields.Char( string="No Surat",   index=True,   help="")
    sr_nik          = fields.Char( string="NIK Pemohon",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    #sr_nama         = fields.Char( string="Nama Pemohon",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_tmp_lahir    = fields.Char( string="Tempat Lahir",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_tgl_lahir    = fields.Date( string="Tanggal Lahir",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_agama        = fields.Selection([('islam', 'Islam'), ('katolik', 'Katolik'), ('protestan', 'Protestan'), ('hindu', 'Hindu'), ('budha', 'Budha'),('konghucu','KongHu Chu')], string='Agama', readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_jenis_kel    = fields.Selection(selection=[('pria','Pria'),('wanita','Wanita')],  string="Jenis Kelamin", required=True, readonly=True, states={"draft" : [("readonly",False)]}, help="")
    sr_pekerjaan_id = fields.Many2one(comodel_name="cdn.pekerjaan",  string="Pekerjaan", readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_alamat       = fields.Char( string="Alamat Lengkap",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_keperluan    = fields.Char( string="Keperluan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_note         = fields.Text( string="Note / Catatan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_ttd          = fields.Char( string="Tanda Tangan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    state           = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string="State",  help="")


    warga_id        = fields.Many2one(comodel_name="cdn.warga",  string="Nama Pemohon",  readonly=True, states={"draft" : [("readonly",False)]},  help="")

    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("cdn.layanan_surat") or "Error Number!!!"
        return super(layanan_surat, self).create(vals)

    def action_diperiksa(self):
        self.state = STATES[1][0]

    def action_disetujui(self):
        self.state = STATES[2][0]
    
    def action_selesai(self):
        self.state = STATES[3][0]


    def action_draft(self):
        self.state = STATES[0][0]

    def unlink(self):
        # for me_id in self :
        #     if me_id.state != STATES[0][0]:
        #         raise UserError("Cannot delete non draft record!")
        return super(layanan_surat, self).unlink()

    @api.onchange('warga_id')
    def onchange_warga_id(self):
        for rec in self:
            alamat = ""
            if rec.warga_id:
                rec.sr_nik          = rec.warga_id.nik
                #rec.sr_nama         = rec.warga_id.nama
                rec.sr_tmp_lahir    = rec.warga_id.tmp_lahir
                rec.sr_tgl_lahir    = rec.warga_id.tgl_lahir
                rec.sr_agama        = rec.warga_id.agama
                rec.sr_jenis_kel    = rec.warga_id.jenis_kel
                rec.sr_pekerjaan_id = rec.warga_id.pekerjaan_id
                if rec.warga_id.street: 
                  alamat = rec.warga_id.street
                if rec.warga_id.street2:
                    alamat = alamat+" "+rec.warga_id.street2
                if rec.warga_id.rt_rw:
                    alamat = alamat+" "+rec.warga_id.rt_rw
                rec.sr_alamat       = alamat


                


        

    
                
