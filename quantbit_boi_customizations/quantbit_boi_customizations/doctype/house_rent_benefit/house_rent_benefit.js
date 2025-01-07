// Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("House Rent Benefit Details", {
	amount: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_house_rent_total',
            doc: frm.doc
        });
    },
    rate: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_house_rent_total',
            doc: frm.doc
        });
    },
    benifit_details_remove: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_house_rent_total',
            doc: frm.doc
        });
    },
    duration: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_house_rent',
            doc: frm.doc
        });
    },
});
