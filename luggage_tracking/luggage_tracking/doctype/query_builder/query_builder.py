# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.query_builder import DocType, Table
from frappe.query_builder.functions import Count
from pypika import CustomFunction
from frappe.query_builder.custom import ConstantColumn



class QueryBuilder(Document):
	def before_save(self):
		# self.rawQuery()
		# self.usingQB1()
		# self.usingQB2()
		# self.usingQB3()
		# self.usingQB4()
		# self.usingQB5()
		# self.usingQB6()
		# self.usingQB7()
		# self.usingQB8()
		# self.usingQB9()
		# self.usingQB10()
		# self.usingQB11()	
		# self.usingQB12()
		# self.usingQB13()
		# self.usingQB14()
		self.usingQB15()

	# Raw Query
	def rawQuery(self):
		result = frappe.db.sql(
			f"""
			SELECT *
			FROM `tabQuery Builder`;
			"""
		)
		for r in result:
			print(r,"Raw Query")

	# Using frappe.qb.from_(doctype) 
	def usingQB1(self):
		QueryBuilder = DocType("Query Builder")
		result = (frappe.qb.from_(QueryBuilder).select("*")).run()
		for r in result:
			print(r,"UsingQB1")	

	# Using frappe.qb.Doctype(name_of_table) # Not Working ---------------------
	def usingQB2(self):
		result = (frappe.qb.Doctype("QueryBuilder").select("*")).run()
		for r in result:
			print(r,"UsingQB2")	
	
	# Alternative for frappe.qb.Doctype(name_of_table)
	def usingQB3(self):
		doctype = frappe.qb.DocType("Query Builder") 
		result = (frappe.qb.from_(doctype).select(doctype.name1, doctype.owner)).run()
		for row in result:
			print(row,"UsingQB3")

	# Using frappe.qb.Table(name_of_table) # Not Workig ---------------
	def usingQB4(self):
		result = (frappe.qb.Table("tabQuery Builder").select("*")).run()
		for r in result:
			print(r,"UsingQB4")	

	# Alternative for frappe.qb.Table(name_of_table)
	def usingQB5(self):
		my_table = frappe.qb.Table("tabQuery Builder") 
		result = (frappe.qb.from_(my_table).select(my_table.name1, my_table.owner)).run()
		for row in result:
			print(row,"UsingQB5")

	# Using frappe.qb.Field(name_of_coloum) 
	def usingQB6(self):
		name = frappe.qb.Field("name1")
		result = (frappe.qb.from_("Query Builder").select("name1").where(name == 'a')).run()
		for r in result:
			print(r,"UsingQB6")

	# Differentiating Run() and Walk()
	def usingQB7(self):
		QueryBuilder = DocType("Query Builder")
		query = frappe.qb.from_(QueryBuilder).select("name1")
		query1 = (frappe.qb.from_(QueryBuilder).select("name1")).run()
		query2 = (frappe.qb.select("name1").from_(QueryBuilder)).walk()
		print(str(query),"Using Query-------------------")
		print(query.get_sql(),"Using Query-------------------")
		print(str(query)==query.get_sql(),"===========")
		print(query1,"UsingQB7 Query1")
		print(query2,"UsingQB7 Query2")

	# Using Frappe.qb.sql
	def usingQB8(self):
		query3 = frappe.qb.from_('Query Builder').select('name1')
		frappe.db.sql(query3) # This ignores permisions and paramaterisation of queries.

	# Joining Tables using USING
	def usingQB9(self):
		Passenger = DocType("Passenger Verification")
		Luggage = DocType("Luggage")
		query4 = (frappe.qb.from_(Passenger).join(Luggage).using("passenger_name").select(Passenger.passenger_name,Luggage.status)).run()
		print(query4,"UsingQB9")

	# Joining Tables using on_field
	def usingQB10(self):
		Passenger = DocType("Passenger Verification")
		Luggage = DocType("Luggage")
		query5 = (frappe.qb.from_(Passenger).join(Luggage).on_field("passenger_name").select(Passenger.passenger_name,Luggage.status)).run()
		print(query5,"UsingQB10")

	# Joining Tables using on
	def usingQB11(self):
		Passenger = DocType("Passenger Verification")
		Luggage = DocType("Luggage")
		query6 = (frappe.qb.from_(Passenger).join(Luggage).on(Passenger.passenger_name == Luggage.passenger_name).select(Passenger.passenger_name,Luggage.status)).run()
		print(query6,"UsingQB11")
			
	# Subquery
	def usingQB12(self):
		Passenger = DocType("Passenger Verification")
		query7 = frappe.qb.from_(Passenger).select("passenger_name").where(Passenger.passenger_name == "Mohammed Hashim")
		query8 = (frappe.qb.from_(Passenger).select(query7,"email").where(Passenger.passenger_name == "Mohammed Hashim")).run()
		print(query8,"UsingQB12")

	# Simple Function
	def usingQB13(self):
		Passenger = DocType("Passenger Verification")
		query9 = (frappe.qb.from_(Passenger).select(Count(Passenger.name))).run()
		print(query9,"UsingQB13")

	# Custom Functions
	def usingQB14(self):
			Passenger = DocType("Passenger Verification")
			TimeDiff = CustomFunction("TIMEDIFF", ["departure_time", "arrival_time"])

			query = (frappe.qb.from_(Passenger).select(TimeDiff(Passenger.departure_time, Passenger.arrival_time))).run()

			print(query, "UsingQB14")

	def usingQB15(self):
		Passenger = DocType("Passenger Verification")
		query11 = (frappe.qb.from_(Passenger).select("passenger_name", ConstantColumn("John").as_("User"))).run()

		print(query11, "UsingQB15")

	# def usingQB15(self):
	# 	# Get a query builder instance for the 'User' DocType
	# 	query = frappe.qb.get_query("Example")

	# 	# Execute the query and fetch results
	# 	example = query.run()

	# 	print(example,"UsingQB15")
