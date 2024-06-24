# Copyright (c) 2024, praveenkumar and contributors
# For license information, please see license.txt

import frappe
import string
import random
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.status = "Completed"
    
@frappe.whitelist(allow_guest=True)
def gate_no_update(flight, gate_no):
    frappe.errprint(gate_no)
    flights = frappe.get_all("Airplane Ticket", filters={'flight': flight})
    for plane in flights:
        flight1 = frappe.get_doc("Airplane Ticket", plane.name)
        flight1.gate_number = gate_no
        flight1.save()
   