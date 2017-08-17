# -*- coding: utf-8 -*-
from openerp import http

# class /opt/odoo/customAddons/frontEnd(http.Controller):
#     @http.route('//opt/odoo/custom_addons/front_end//opt/odoo/custom_addons/front_end/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/custom_addons/front_end//opt/odoo/custom_addons/front_end/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/custom_addons/front_end.listing', {
#             'root': '//opt/odoo/custom_addons/front_end//opt/odoo/custom_addons/front_end',
#             'objects': http.request.env['/opt/odoo/custom_addons/front_end./opt/odoo/custom_addons/front_end'].search([]),
#         })

#     @http.route('//opt/odoo/custom_addons/front_end//opt/odoo/custom_addons/front_end/objects/<model("/opt/odoo/custom_addons/front_end./opt/odoo/custom_addons/front_end"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/custom_addons/front_end.object', {
#             'object': obj
#         })