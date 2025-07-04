# app/cache.py
import frappe

def clear_cache():
    frappe.logger().info("✅ CLEAR CACHE: Custom clear_cache hook triggered.")
    frappe.log_error("CLEAR CACHE Hook Triggered", "clear_cache")
    print("Clear Cache -------------------------------------------------")

    # Add any cache-clearing custom logic here
    frappe.clear_cache()

