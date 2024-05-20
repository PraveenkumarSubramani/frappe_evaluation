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