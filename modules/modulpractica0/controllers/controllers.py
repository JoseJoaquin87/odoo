# -*- coding: utf-8 -*-
from odoo import http

# class Modulpractica0(http.Controller):
#     @http.route('/modulpractica0/modulpractica0/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulpractica0/modulpractica0/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulpractica0.listing', {
#             'root': '/modulpractica0/modulpractica0',
#             'objects': http.request.env['modulpractica0.modulpractica0'].search([]),
#         })

#     @http.route('/modulpractica0/modulpractica0/objects/<model("modulpractica0.modulpractica0"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulpractica0.object', {
#             'object': obj
#         })