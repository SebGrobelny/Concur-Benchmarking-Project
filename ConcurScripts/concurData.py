from expenseDataTrial import expense_data
import random
import csv
# coding=utf-8

with open('concurData.csv', 'wb') as fp:
	csv_writer = csv.writer(fp, delimiter = ',')

	#Q1 Dates Q2 Q3 Q4
	month_num =1
	day_num = 0

	expense_object = expense_data('Expense')

	#attribute fields
	attr_list = ['Expense_Record', 'Transaction_Date', 'Expense_Type', 'Vendor_Name', 'Department', 'Industry', 'Origin_Location', 'Destination', 'Amount_Paid']
	#write this row into the file
	csv_writer.writerow(attr_list)

	year_num = 2013

	for expense_id in range(0,500000):
		row_list = []
		#adding the expense record
		row_list.append(expense_id)
		#adding the transaction date
		if(expense_id % 100 == 0):
			if(day_num == 30):
				day_num = 0
				if(month_num == 12):
					month_num = 0
					year_num+=1
				month_num += 1
			day_num+=1

		
		row_list.append(str(month_num).zfill(2)+'/'+str(day_num)+'/'+str(year_num))
		#adding in the expense type
		expense_selector = int(random.uniform(expense_data.expense_min, expense_data.expense_max))
		row_list.append(expense_data.expenseType[expense_selector])

		#adding in the vendor name
		if expense_selector == 0:
			hotel_selector = int(random.uniform(expense_data.hotel_min,expense_data.hotel_max))
			row_list.append(expense_data.hotelList[hotel_selector])

		if expense_selector == 1:
			car_selector = int(random.uniform(expense_data.carRental_min, expense_data.carRental_max))
			row_list.append(expense_data.carRentalList[car_selector])

		if expense_selector == 2:
			air_selector = int(random.uniform(expense_data.airline_min, expense_data.airline_max))
			row_list.append(expense_data.airlineList[air_selector])

		#adding in the department
		department_selector = int(random.uniform(expense_data.department_min,expense_data.department_max))
		row_list.append(expense_data.employeeDepartment[department_selector])

		#adding in the industry
		industry_selector = int(random.uniform(expense_data.industry_min, expense_data.industry_max))

		row_list.append(expense_data.industryName[industry_selector])

		#adding in the source location
		location_selector = int(random.uniform(expense_data.location_min, expense_data.location_max))
		row_list.append(expense_data.locationList[location_selector])

		#adding in the destination location
		location_selector = int(random.uniform(expense_data.location_min, expense_data.location_max))
		row_list.append(expense_data.locationList[location_selector])

		#amount paid
		row_list.append('{0:.2f}'.format(random.uniform(expense_data.amount_min,expense_data.amount_max)))

		#write the row in 
		csv_writer.writerow(row_list)

	print expense_data.locationList
		#adding in the reservation number ExpenseType-LocationNo-Transaction Date-Expense Reco



# hotel = len(expense_object.hotelList)
# print "Hotel list: "
# print hotel
# carrentallen = len(expense_object.carRentalList)
# print "Car Rental List: "
# print carrentallen
# airlinelen = len(expense_object.airlineList)
# print "Airline List: "
# print airlinelen
# locationlen = len(expense_object.locationList)
# print "Location List: "
# print locationlen
# industryname = len(expense_object.industryName)
# print "Industry Name: "
# print industryname


