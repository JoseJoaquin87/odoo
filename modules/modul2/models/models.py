
# -*- coding: utf-8 -*-

from odoo import models, fields, api
class modul2(models.Model):
	_name = 'modul2.modul2'

	name = fields.Char()
	start_date = fields.Datetime()
	done = fields.Boolean()
