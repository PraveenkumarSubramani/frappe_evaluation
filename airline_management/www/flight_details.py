import frappe
def get_context(context):
    flight_id = frappe.request.path.split('/')[-1]
    flight = frappe.get_doc('Airplane Flight', flight_id)
    context.flight = flight