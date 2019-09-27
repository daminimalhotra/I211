import csv
#question 1
##companies = csv.DictReader(open("companies.csv", "r"))
##IN_companies = []
##for entry in companies:
##    if entry["state"] == "IN":
##        IN_companies.append(entry["company_name"])
##IN_companies.sort()
##print(IN_companies)


#question 2 // formatting
import csv

data = csv.DictReader(open("companies.csv","r"))
data_format = "{}\t\t{}"
companies = []

user_in = input("Search for companies in what state? ")
print("-----------------------------------------------------")

for entry in data:
    if  entry["state"] == user_in:
            companies.append((entry["company_name"],entry["web"]))
for company in sorted(companies):
    name, web = company
    name_space = 40 - len(name)
    print(name, name_space*" ", web)
