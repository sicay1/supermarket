# -*- coding: utf-8 -*-
from odoo import fields, models
from .productCategory import ProductCategory


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'

    name = fields.Char('Name')
    category = fields.Many2one("supermarket.ProductCategory",string = "Category")
    unitPrice = fields.Float('Unit Price')
    

  