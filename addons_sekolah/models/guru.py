from odoo import models, fields, api

class Guru(models.Model):
    _name = 'guru'

    name = fields.Char(string='Nama Guru')
    nip = fields.Char(string='NIP', required=True)
    jns_kelamin = fields.Selection([
        ('p','Perempuan'),
        ('l','Laki-laki')
        ], string='Jenis Kelamin')
    mata_pelajaran_id = fields.Many2one('mata.pelajaran', string='Mata Pelajaran')
    usia = fields.Char(string='Usia')
    no_telp = fields.Char(string='Telepon')
    alamat = fields.Text(string='Alamat')

    _sql_constraints = [
        ('kode_uniq', 'unique(nip)', 'NIP harus unik !')
    ]