STATES = [('draft','Draft'),('confirm','Confirm'),('done','Done')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class layanan_surat(models.Model):

    _name           = "cdn.layanan_surat"
    _description    = "cdn.layanan_surat"

    name            = fields.Char( required=True, default="New", readonly=True,  string="Name",  help="")
    sr_nik         = fields.Char( string="NIK Pemohon",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_tmp_lahir    = fields.Char( string="Tempat Lahir",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_tgl_lahir    = fields.Date( string="Tanggal Lahir",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_agama        = fields.Char( string="Agama",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_jenis_kel    = fields.Selection(selection=[('pria','Pria'),('wanita','Wanita')],  string="Jenis Kelamin", required=True, help="")
    sr_pekerjaan    = fields.Char( string="Pekerjaan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_alamat       = fields.Char( string="Alamat Lengkap",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_keperluan    = fields.Char( string="Keperluan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_note         = fields.Text( string="Note / Catatan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    sr_ttd          = fields.Char( string="Tanda Tangan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    state           = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string="State",  help="")


    warga_id = fields.Many2one(comodel_name="cdn.warga",  string="Nama Pemohon",  readonly=True, states={"draft" : [("readonly",False)]},  help="")

    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]

    def action_draft(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(layanan_surat, self).unlink()