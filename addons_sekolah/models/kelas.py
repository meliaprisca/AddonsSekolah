from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'kelas'

    name = fields.Char(string='Nama Kelas')
    guru_id = fields.Many2one('guru', string='Wali Kelas')
    siswa_ids = fields.One2many('siswa', 'kelas_id', string='Siswa')