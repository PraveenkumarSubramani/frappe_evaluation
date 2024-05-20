# Copyright (c) 2024, praveenkumar and contributors
# For license information, please see license.txt

import frappe
import random
import string
import re
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        flight = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
        airplane = frappe.db.get_value("Airplane", flight, "no_of_seats")
        random_letter = random.choice(string.ascii_uppercase[:5])
        random_number = random.randint(1,airplane)
        self.seat = random_letter + str(random_number)
        add_on = []
        child = self.add_ons
        tot_price = 0
        for price in child:
            if price.item not in add_on:
                add_on.append(price.item)
                tot_price += price.amount
            else:
                child.remove(price)
        self.total_amount = self.flight_price + tot_price
        ticket_list = frappe.db.get_list("Airplane Ticket",filters={"flight": self.flight})
        airplane_flight = frappe.db.get_value("Airplane Flight", self.flight, "airplane")
        no_of_seats = frappe.db.get_value("Airplane",airplane_flight, "no_of_seats")
        if len(ticket_list) >  no_of_seats:
            frappe.throw("Tickets are full")
        
    def on_submit(self):
        if self.status != "Boarded":
            frappe.throw("Status is not Boarded")