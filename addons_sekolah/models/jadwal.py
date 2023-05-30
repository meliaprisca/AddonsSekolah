from odoo import models, fields, api

class Jadwal(models.Model):
    _name = 'jadwal'

    name = fields.Char(string='name', default="/")
    hari = fields.Selection([
            ('Senin', 'Senin'),
            ('Selasa', 'Selasa'),
            ('Rabu', 'Rabu'),
            ('Kamis', 'Kamis'),
            ('Jumat', 'Jumat'),
        ], string='Hari',)
    kelas_id = fields.Many2one('kelas', string='Kelas')
    jam = fields.Selection([
        ('1', '07:00 - 08:00'),
        ('2', '08:00 - 09:00'),
        ('3', '09:00 - 10:00'),
        ('4', '11:00 - 12:00'),
        ('5', '13:00 - 14:00'),
        ('6', '14:00 - 15:00'),
    ], string='Jam',)
    mata_pelajaran_id = fields.Many2one('mata.pelajaran', string='Mata Pelajaran')


