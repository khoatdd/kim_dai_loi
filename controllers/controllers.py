# -*- coding: utf-8 -*-
from odoo import http

# class Odoocustomization(http.Controller):
#     @http.route('/odoocustomization/odoocustomization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoocustomization/odoocustomization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoocustomization.listing', {
#             'root': '/odoocustomization/odoocustomization',
#             'objects': http.request.env['odoocustomization.odoocustomization'].search([]),
#         })

#     @http.route('/odoocustomization/odoocustomization/objects/<model("odoocustomization.odoocustomization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoocustomization.object', {
#             'object': obj
#         })