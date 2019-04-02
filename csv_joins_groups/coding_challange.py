import csv
import codecs

import collections

def read_my_csv(file):
	with codecs.open(file,encoding='utf8') as csvfile:
		data = csv.reader(csvfile, delimiter=',')
		rows = []
		for row in data:
			rows.append(row)
		return rows

def my_code(file1,file2,header):
	p_file = file1
	p_data = read_my_csv(p_file)
	p_header = p_data[0]
	p_records = p_data[1:]

	o_file = file2
	o_data = read_my_csv(o_file)
	o_header = o_data[0]
	o_records = o_data[1:]

	pid_in = p_header.index('product_id')
	opid_in = o_header.index('product_id')	

	header_joined = p_header+o_header
	record_joined = [product+order for order in o_records for product in p_records if order[opid_in]==product[pid_in]]

	dep_id = header_joined.index('department_id')
	dep_ids = sorted([int(x[dep_id]) for x in record_joined])
	num_orders = dict(collections.Counter(dep_ids))

	reord_id = header_joined.index('reordered')
	first_orders = [int(x[dep_id]) for x in record_joined if int(x[reord_id])==0]
	first_order_counter = dict(collections.Counter(first_orders))

	output = open('report.csv','w')
	output.write(header)

	for order in num_orders:
		# department_id ',' number_of_orders
		if order in first_order_counter.keys():
			record = str(order)+','+str(num_orders[order]) +','+str(first_order_counter[order]) +','+str(format(first_order_counter[order]/num_orders[order], '.2f'))
			output = open('report.csv','a')
			output.write('\n'+record)

		else:
			record = str(order)+','+str(num_orders[order]) +',0,0.00'
			output = open('report.csv','a')
			output.write('\n'+record)


if __name__=="__main__":

	header='department_id,number_of_orders,number_of_first_orders,percentage'
	my_code('data/products.csv','data/order_products.csv',header)
