import json


print("--------------------------------------------------")
print("           Employee Management System             ")
print("--------------------------------------------------")
def add_data():

	no = input("Enter your employee number: ")
	name = input("Enter your name: ")
	position = input("Enter your job position: ")

	dic = {
		"Employee Number: " : no,
		"Name: " : name,
		"Job Position: " : position 
	}


	with open("employee.json", "r") as getdata:
		data = json.load(getdata) # convert json to python

		data[no] = dic

		with open("employee.json", "w") as save:
			json.dump(data, save)  # convert python to json
			print("Successfully Added!")


def view_data():

	with open("employee.json", "r") as view:
		data = json.load(view)

		for i, m in data.items():
			for x, n in m.items():
				print(x, n)
			print("\n")	

def delete_data():
	no = input("Enter your employee number: ")

	with open("employee.json", "r") as getdata:
		data = json.load(getdata)

		if no in data:
			data.pop(no)

			with open("employee.json", "w") as delete:
				data1 = json.dump(data, delete)
				print("Successfully Deleted")

def update_data():

	no = input("Enter your employee number: ")

	with open("employee.json", "r") as getdata:
		data = json.load(getdata)	

		if no in data:
			name = input("Enter new name: ")
			position = input("Enter new job position: ")

			dic = {
				"Employee Number: " : no,
				"Name: " : name,
				"Job Position: " : position 
			}

			data[no] = dic
			with open("employee.json", "w") as update:
				json.dump(data, update)
				print("Successfully Updated!")

def main():

	print("\n1. Add Data")
	print("\n2. View Data")				
	print("\n3. Delete Data")	
	print("\n4. Update Data")
	print("\n5. Exit")		

	enter = int(input("Enter Choice: "))

	if enter == 1:
		add_data()
		main()
	elif enter == 2:	
		view_data()
		main()
	elif enter == 3:	
		delete_data()
		main()
	elif enter == 4:	
		update_data()
		main()
	else:
		print("Thank You! and Come Again")
main()					
