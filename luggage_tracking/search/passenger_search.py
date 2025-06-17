from frappe.search.full_text_search import FullTextSearch
import frappe

class PassengerSearch(FullTextSearch):
    def get_items_to_index(self):
        docs = []
        passengers = frappe.get_all("Passenger Verification", fields=["name", "passenger_name"])
        for p in passengers:
            docs.append(self.get_document_to_index(p.name))
        return docs

    def get_document_to_index(self, name):
        doc = frappe.get_doc("Passenger Verification", name)
        return frappe._dict(
            name=doc.name,
            content=f"{doc.passenger_name}"
        )

    def parse_result(self, result):
        print(result,"---------------------------------------------------------------------")
        return {
            "name": result["name"],  # Store just the name (not the whole Whoosh result)
        }
