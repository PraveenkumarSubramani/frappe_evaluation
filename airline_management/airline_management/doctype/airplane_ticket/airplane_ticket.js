// Copyright (c) 2024, praveenkumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button('Assign Seat', () => {
            d = new frappe.ui.Dialog({
                title: 'Assign Seat',
                fields: [
                {
                    fieldname: 'assign_seat',
                    fieldtype: 'Data',
                    label: 'Enter Seat Number',
                }
                ],
                size: 'small',
                primary_action_label: 'Assign',
                primary_action(values) {
                        frm.set_value('seat', values.assign_seat);
                    d.hide();
                }
            });
            d.show();
        },__("Actions"));
	},
    onload: function(frm){
        if(frm.doc.docstatus == 1){
            frm.set_df_property('gate_number', 'read_only', 1);
            frm.refresh_field('gate_number');
        }
    }
});
