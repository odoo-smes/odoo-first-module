from odoo import models,api,tools,fields
from odoo.exceptions import UserError,ValidationError
class MyCar(models.Model):
    _name = "my.car"
    _description = "My Car Model"

    name = fields.Char('Car Name', required=True)
    number_door = fields.Integer('Number Door')
    description = fields.Text("Car Description")
    car_image = fields.Binary("Car Image")
    color = fields.Selection([
        ('red','Red'),
        ('white','White'),
        ('black','Black'),
        ('blue','Blue')
    ],string="Color", default='red')
    car_type = fields.Selection([
        ('new','New'),
        ('old','Old')
    ], string="Car Type", default='new')
    owner_id = fields.Many2one('res.partner', string="owner")
