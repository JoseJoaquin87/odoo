# -*- coding: utf-8 -*-
from odoo import http

# class Modulpractica(http.Controller):
#     @http.route('/modulpractica/modulpractica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulpractica/modulpractica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulpractica.listing', {
#             'root': '/modulpractica/modulpractica',
#             'objects': http.request.env['modulpractica.modulpractica'].search([]),
#         })

#     @http.route('/modulpractica/modulpractica/objects/<model("modulpractica.modulpractica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulpractica.object', {
#             'object': obj
#         })