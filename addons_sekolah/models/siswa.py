from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
class Siswa(models.Model):
    _name = 'siswa'

    name = fields.Char(string='Nama Siswa', required=True, )
    nis = fields.Char(string='NIS', required=True, )
    jns_kelamin = fields.Selection([
        ('p','Perempuan'),
        ('l','Laki-laki')
        ], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Selection([
        ('islam','Islam'),
        ('katolik','Katolik'),
        ('protestan','Protestan'),
        ('hindu','Hindu'),
        ('budha','Budha'),
        ('konghucu','Konghucu'),
        ], string='Agama')
    nm_ayah = fields.Char(string='Nama Ayah')
    nm_ibu = fields.Char(string='Nama Ibu')
    usia = fields.Char(string="Usia", compute="age_calc", store=True)
    alamat = fields.Text(string='Alamat')
    kelas_id = fields.Many2one('kelas', string='Kelas')

    _sql_constraints = [
        ('kode_uniq', 'unique(nis)', 'NIS harus unik !')
    ]
    # @api.depends('tgl_lahir')
    # def age_calc(self):
    #     if self.tgl_lahir is not False:
    #         self.USIA = (datetime.today().date() - datetime.strptime(str(self.tgl_lahir), '%Y-%m-%d').date())
    #         timedelta(days=365)

    @api.depends('tgl_lahir')
    def age_calc(self):
        for rec in self:
            if rec.tgl_lahir:
                current_date = date.today()
                date_in_your_field = rec.tgl_lahir
                rd = relativedelta(current_date, date_in_your_field)

                rec.usia = str(rd.years) + " Tahun"
                # rec.usia = current_date - date_in_your_field
                # print(str(rec.etaw_age))