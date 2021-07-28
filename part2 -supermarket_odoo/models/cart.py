from odoo import fields, models,api
from .customer import Customer


class Cart(models.Model):
    _name = 'supermarket.cart'
    _description = 'Product'

    customer = fields.Many2one('supermarket.customer',string = "Customer" )
    dateOfCreation = fields.create_date("date Of Creation")
    premium  = fields.Boolean(compute = 'isPrem')
    customerLastVisited = "supermarket.customer.lastVisited",store = True,depends = ["supermarket.customer"]
    customerVistings = "supermarket.customer.visitingTimes",store = True,depends = ["supermarket.customer"]
    discount_value = fields.Float(compute='_apply_discount')


    @api.depends('customerLastVisited','customerVistings')
    def isPrem(self):
        if self.dateOfCreation - self.customerLastVisited == 7 and self.customerVistings > 1:
            return True
        return False











    