with open('currencydata.txt') as f:
    lines=f.readlines()

currencydict={}
for line in lines:
    parsed= line.split("\t")
    currencydict[parsed[0]]=parsed[1]

print(currencydict)
print("enter indian currency to convert with expected currency");
num=int(input("enter indian currency")) 
currency_list=list(currencydict.keys())
print(currency_list)
print("enter the currency which u want to use")
n=int(input("enter the curancy number"))
req=0
if n<10:
    req=float(currencydict[currency_list[n]])*num
    print(req)

x=currency_list[n]
print(f"the price of indan ruppess  in {x} is {req} ")      

#print(currencydict)    
#print(a)