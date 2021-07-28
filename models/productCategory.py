from odoo import fields, models

class ProductCategory(models.Model):
    _name = 'supermarket.ProductCategory'
    _description = 'Product Category'

    name = fields.Char('Category')
