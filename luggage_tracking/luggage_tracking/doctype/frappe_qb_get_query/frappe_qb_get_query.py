# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from pypika.functions import Count, Sum, Avg, Max, Min, Abs, Concat



class FrappeQBGetQuery(Document):
	def validate(self):
		# self.basicQueryStructure()
		# self.fieldSelectionAndUsingAlias()
		# self.linkedDocumentFields()
		# self.childTableFields()
		# self.fetchingChildTableRecords()
		# self.aggregateFunctions()
		self.scalarFunctions()
		# pass
	
	# Basic Query Structure and Example
	def basicQueryStructure(self):
		# Selecting specific fields. Note: fields are optional. If Field is not specified, it returns name column.
		query = frappe.qb.get_query("Query Builder", fields=["name1"])
		examples = query.run(as_dict=True)
		# print(examples,"---------")

	# Field Selection and Using Aliases(as)
	def fieldSelectionAndUsingAlias(self):
		# Passing fields as a comma-separated string
		query1 = (frappe.qb.get_query("Form API", fields=["name1, status"])).run(as_dict=True)

		# Selecting all fields using '*'
		query2 = (frappe.qb.get_query("Form API", fields=["*"])).run(as_dict=True)

		# Using as
		query3 = (frappe.qb.get_query("Form API", fields=["name1 as Username, status as Nilamai"])).run(as_dict=True)

		# print(query1,"---------")
		# print(query2,"---------")
		# print(query3,"----------")

	# Using Linked Document Field
	def linkedDocumentFields(self):
		query = (frappe.qb.get_query("Form API", fields=["name1","link_field.name1 as FRM_Name"])).run(as_dict = True)
		print(query)

	# Using Child Table Field
	def childTableFields(self):
		query = (frappe.qb.get_query("Form API", fields=["name1","form_api_child_table.weight as Luggage Weight"])).run(as_dict = True)
		print(query)

	"""
	Important: When selecting fields from child tables this way, the query performs a LEFT JOIN, 
	potentially resulting in multiple rows for each parent document if the child table has multiple entries.
	"""

	# Fetching Child Table Records -  more structured way to fetch child table data.
	def fetchingChildTableRecords(self):
		query = frappe.qb.get_query(
			"Form API",
			fields=[
				# "name",
				"name1",
				{"form_api_child_table": ["luggage_type","weight"]}
			],
			filters={"docstatus": 0},
			limit=1
		)
		results = query.run(as_dict=True)
		print(results,"------------")

	# Aggregate Functions
	def aggregateFunctions(self):

		#  --------------------------------------------------------------------------------------------------------------------

		# Count

		# Working
		# query1 = (frappe.qb.get_query("Form API", fields=["name1",Count("name1")])).run()
		# print(query1,"---------Count 1----------")

		# Not Working
		# query1 = (frappe.qb.get_query("Form API", fields=["name", {"COUNT": "name1", "as": "total_users"}])).run(as_dict = True)
		# print(query1,"---------Count 2----------")

		# Working
		# query1 = (frappe.qb.get_query("Form API", fields=[{"COUNT(name1) as total_users"}])).run(as_dict = True)
		# print(query1,""---------Count 3----------"")

		# ---------------------------------------------------------------------------------------------------------------------

		# Sum 
		
		# Not Working
		# query2 = (frappe.qb.get_query("Form API", fields=["name1",Sum("weight")])).run(as_dict = True)
		# print(query2,"-----------sum 1-----------")

		# Not working
		# query2 = (frappe.qb.get_query("Form API", fields=[{"SUM": "weight", "as": "total_weight"}])).run(as_dict = True)
		# print(query2, "-----------sum 2-----------")

		# Working
		# query2 = (frappe.qb.get_query("Form API", fields=["SUM(weight) as total_weight"])).run(as_dict = True)
		# print(query2,"-----------sum 3-----------")

		# ---------------------------------------------------------------------------------------------------------------------
		
		# Avg 
		
		# Not Working
		# query3 = (frappe.qb.get_query("Form API", fields=["name1", Avg('weight')])).run(as_dict = True)
		# print(query3,"---------avg 1----------")

		# Not Working
		# query3 = (frappe.qb.get_query("Form API", fields=[{"AVG": "weight", "as": "total_weight"}])).run(as_dict= True)
		# print(query3,"-----------avg 2----------")

		# Working
		# query3 = (frappe.qb.get_query("Form API", fields=["AVG(weight) as total_weight"])).run(as_dict = True)
		# print(query3,"---------avg 3----------")

		# ---------------------------------------------------------------------------------------------------------------------

		# Max

		# Not Working
		# query4 = (frappe.qb.get_query("Form API", fields=["name1", Max('weight')])).run(as_dict = True)
		# print(query4,"----------Max 1----------")

		# Not Working
		# query4 = (frappe.qb.get_query("Form API", fields=[{"MAX": "weight", "as": "max_weight"}])).run(as_dict = True)
		# print(query4,"---------Max 2----------")

		# Working
		# query4 = (frappe.qb.get_query("Form API", fields=["Max(weight) as max_weight"])).run(as_dict = True)
		# print(query4,"---------Max 3--------")

		# ---------------------------------------------------------------------------------------------------------------------

		# Min

		# Not Working
		# query5 = (frappe.qb.get_query("Form API", fields=["name1", Min('weight')])).run(as_dict = True)
		# print(query5,"----------Min 1----------")

		# Not Working
		# query5 = (frappe.qb.get_query("Form API", fields=[{"MIN": "weight", "as": "min_weight"}])).run(as_dict = True)
		# print(query5,"---------Min 2----------")

		# Working
		query5 = (frappe.qb.get_query("Form API", fields=["Min(weight) as min_weight"])).run(as_dict = True)
		print(query5,"---------Min 3--------")

		# ---------------------------------------------------------------------------------------------------------------------

	# Scalar Functions
	def scalarFunctions(self):

		# ABS

		# Not Working
		# query1 = (frappe.qb.get_query("Form API", fields=[{"ABS": "weight", "as": "positive_weights"}])).run(as_dict=True)
		# print(query1,"------------ABS 1--------------")

		# Working
		# query1 = (frappe.qb.get_query("Form API", fields=["Abs(weight) as positive_weight"])).run(as_dict = True)
		# print(query1,"---------ABS 2--------")

		# ---------------------------------------------------------------------------------------------------------------------

		# If Null (Coalesce)

		# Not Working
		# query2 = (frappe.qb.get_query("Form API", fields=[{"Coalesce": "weight", "as": "Values_without_null"}])).run(as_dict=True)
		# print(query2,"------------Coalesce 1--------------")

		# Not Working
		# query2 = (frappe.qb.get_query("Form API",  fields=["Coalesce(weight,'onumilla') as all_weight"])).walk()     #.run(as_dict = True)
		# print(query2,"---------Coalesce 2--------")

		# ---------------------------------------------------------------------------------------------------------------------

		# Concat

		# Not Working
		# query = frappe.qb.get_query("User", fields=[{"CONCAT": ["first_name", "' '", "last_name"], "as": "full_name"}])
		# print(query3,"------------Concat 1---------------")

		doc = frappe.get_list("Form API", fields=["name1", "link_field"])

		print(doc)

		query3 = (frappe.qb.get_query("Form API", fields=[Concat(doc.name1,doc.link_field)])).walk() #.run(as_dict = True)
		print(query3,"--------------Concat 2-------------")
