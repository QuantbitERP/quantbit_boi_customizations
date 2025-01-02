// Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Bonus Payroll", {
	setup: function(frm) {
		frm.set_query("payroll_entry", function() {
			return {
				filters: [
                    ["Payroll Entry","docstatus","=",0],
					["Payroll Entry","custom_is_bonus","=",1],
                ]
				
			};
		});

    },

});
