from odoo import fields, models, api, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # @api.depends("sale_line_ids")
    def _get_delivery_picking_id(self):
        """
        """
        for line in self:
            delivery_notes = list()
            sale_line_id = line.mapped('sale_line_ids')
            # import pdb;pdb.set_trace()
            for move in sale_line_id.move_ids.filtered(lambda x:x.state == 'done'):
                delivery_notes.append(move.picking_id.id)
            
            line.update({
                    'stock_pickings_line_ids':[(6, 0, delivery_notes)],
                }) 


    stock_pickings_line_ids = fields.Many2many('stock.picking', string='Delivery Note', compute="_get_delivery_picking_id")


    def get_picking_distribution(self):
        """
        """
        result = str()
        for picking in self.stock_pickings_line_ids:
            result += "{}\n".format(picking.name)
        return result

    def get_picking_distribution_with_qty(self):
        """
        """
        result = str()
        for picking in self.stock_pickings_line_ids:
            count = 0
            for move in picking.move_ids_without_package:
                if move.product_id.id == self.product_id.id:
                    count += move.quantity_done

            result += "{} : {}\n".format(picking.name, count)
        return result