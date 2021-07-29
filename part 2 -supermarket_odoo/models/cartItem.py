from odoo import fields, models, api
from .cart import Cart
from .product import Product


class CartItem(models.Model):
    _name = 'supermarket.cartItem'
    _description = 'cartItem'

    product = fields.Many2one('supermarket.product',string = "product" )
    cart = fields.Many2one("supermarket.cart",string = "cart" )
    price = fields.Float(related = "supermarket.product.unitPrice",store = True,depends = ["supermarket.product"])
    premium = fields.Boolean(related = 'supermarket.cart.premium',store = True, depends = ['supermarket.cart'])

    
    quantity = fields.Integer("quantity")
    total = fields.Float(compute='_compute_total')


    #self: model CartItem

    @api.depends('quantity','price','discount')
    def _compute_total(self, product):
        for record in self:
            if self.premium:
                discount = record.price * record.discount
                record.total = record.quantity *  record.discount
            else:
                record.total = record.quantity *  record.price

    