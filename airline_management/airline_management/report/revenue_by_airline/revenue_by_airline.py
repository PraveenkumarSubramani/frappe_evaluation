from frappe import _
import frappe

def execute(filters=None):
    columns = [
        {
            'fieldname': 'airline',
            'label': _('Airline'),
            'fieldtype': 'Link',
            'options': 'Airline'
        },
        {
            'fieldname': 'revenue',
            'label': _('Revenue'),
            'fieldtype': 'Currency',
            'options': 'Currency'
        }
    ]
    data = frappe.db.sql("""
        SELECT
            airline.name AS 'airline',
            IFNULL(SUM(ticket.total_amount), 0) AS 'revenue'
        FROM
            `tabAirline` AS airline
        LEFT JOIN
            `tabAirplane` AS airplane ON airline.name = airplane.airline
        LEFT JOIN
            `tabAirplane Flight` AS flight ON airplane.name = flight.airplane
        LEFT JOIN
            `tabAirplane Ticket` AS ticket ON flight.name = ticket.flight
        GROUP BY
            airline.name
    """, as_dict=True)
    
    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{
                "name": "Value",
                "values": [d["revenue"] for d in data]
            }]
        },
        "type": "donut",
        "colors": ["#7cd6fd"]
    }
    frappe.errprint(data)
    return columns,data,None,chart