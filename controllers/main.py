import odoo
import logging
_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foot_handler(self):
        return "welcome to 'foot' API!";