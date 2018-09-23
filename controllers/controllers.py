# -*- coding: utf-8 -*-
from odoo import http

# class OdooListViewButton(http.Controller):
#     @http.route('/odoo_list_view_button/odoo_list_view_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_list_view_button/odoo_list_view_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_list_view_button.listing', {
#             'root': '/odoo_list_view_button/odoo_list_view_button',
#             'objects': http.request.env['odoo_list_view_button.odoo_list_view_button'].search([]),
#         })

#     @http.route('/odoo_list_view_button/odoo_list_view_button/objects/<model("odoo_list_view_button.odoo_list_view_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_list_view_button.object', {
#             'object': obj
#         })