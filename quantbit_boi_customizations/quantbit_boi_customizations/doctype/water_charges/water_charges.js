// Copyright (c) 2025, Quantbit Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Water Charges", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Water Charges Details", {
	bill_submitted: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_charges',
            doc: frm.doc
        });
    },
    rate: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_charges',
            doc: frm.doc
        });
    },
    charges_details_remove: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_charges',
            doc: frm.doc
        });
    },
});