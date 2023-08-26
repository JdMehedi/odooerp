# -*- coding: utf-8 -*-
# from odoo import http


# class RequestForQoutation(http.Controller):
#     @http.route('/request_for_qoutation/request_for_qoutation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/request_for_qoutation/request_for_qoutation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('request_for_qoutation.listing', {
#             'root': '/request_for_qoutation/request_for_qoutation',
#             'objects': http.request.env['request_for_qoutation.request_for_qoutation'].search([]),
#         })

#     @http.route('/request_for_qoutation/request_for_qoutation/objects/<model("request_for_qoutation.request_for_qoutation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('request_for_qoutation.object', {
#             'object': obj
#         })
