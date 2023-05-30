from odoo import models, fields, api

class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'

    name = fields.Char(string='Mata Pelajaran')
    jurusan = fields.Selection([
            ('ipa', 'IPA'),
            ('ips', 'IPS'),
            ('bahasa', 'Bahasa'),
        ], string='Jurusan')