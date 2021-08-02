from data import data 

#data
products = data 


def test1():
    print("print each product title")

    for  prod in products:
        print(prod["title"])

 #test 2

# print the sum of all prices
def test2():
    print("---sum of all prices")
    sum = 0
  
    for prod in products:
         price= prod["price"]
         sum+= price
         print(f" the sum is:{sum}")

def test3():
    print(f" is greater ")

    for prod in products:
        if(prod["price"] > 13):
            print(prod["title"])

     
#test 4 
# print the total stock value (prince *stock)
def test4():
    print("-- total stock value")

    for prod in products:
       total= prod["price"] * prod["stock"]
       sum += total
       print(f"the total of stock {sum}")

def test5():
    
    print("list of unique categories")
    unique_Category = []
    for  prod in products:
        cat = prod["category"]

        if cat not in unique_categories:
            unique_categories.append(cat)
            print(cat)




def run_tests():
    print("**Starting tests")

    test1()
    test2()
    test3()
    test5()

run_tests()






        


