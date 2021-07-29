# -*- coding: utf-8 -*-
from odoo import fields, models
from .productCategory import ProductCategory


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'
    
    category = fields.Many2one("supermarket.ProductCategory",string = "Category")

    name = fields.Char('Name')
    unitPrice = fields.Float('Unit Price')
    

  