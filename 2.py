code=float(input("enter the code value"))
name=str(input("enter the name"))
desg=str(input("enter the desg"))
company=str(input("enter the company name"))
salary=float(input("enter the salary"))
#allowances
ta=int('salary of 3%')
da=float('4% of salary*100')
hra=float('5% of salar*100')
gross=salary+allowances
#deducts
pf=float(input("enter the value"))
it=int(input("enter the value"))
hi=int(input("enter the value"))
net=gross-deductors
print("code\t name\t des\t com\t salary\t net-salary")
print("code,'\t',name,'\t', desg,'\t',comp,'\t',net salary")
