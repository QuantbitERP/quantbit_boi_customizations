// Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Key Allowance Details", {
	to_date: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_total_days',
            doc: frm.doc
        });
    },
    key_details_remove: function(frm, cdt, cdn) {
        frm.call({
            method: 'calculate_total_days',
            doc: frm.doc
        });
    },
});


frappe.ui.form.on('Key Allowance', {
    refresh(frm) {
        frm.trigger("make_additional_salary");
    },
    
    make_additional_salary(frm) {
        console.log("Docstatus:", frm.doc.docstatus);
        
        // Check if the document is submitted (docstatus = 1)
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("Additional Salary"), () => {
                frappe.model.open_mapped_doc({
                    method: "quantbit_boi_customizations.quantbit_boi_customizations.doctype.key_allowance.key_allowance.make_additional_salary",
                    frm: frm
                });
            }, __("Create"));
        }
    },
    rate: function(frm) {
        if (frm.doc.total_days && frm.doc.rate) {
            amount = frm.doc.total_days * frm.doc.rate;
            frm.set_value('amount', amount);
        } else {
            frm.set_value('amount', 0);
        }
    },
    
   

});