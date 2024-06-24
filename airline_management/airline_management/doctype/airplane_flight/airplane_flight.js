// Copyright (c) 2024, praveenkumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	gate:function(frm){
        frappe.call({
            method: 'airline_management.airline_management.doctype.airplane_flight.airplane_flight.gate_no_update',
            args: {
                'gate_no': frm.doc.gate,
                'flight': frm.doc.name
            },
        })
	}
});
