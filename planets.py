def weight_on_planets():
   # write your code here
    earth_weight = int(input("What do you weigh on earth? "))
    print("On Mars you would weigh " + str(round(earth_weight * .37, 2)) + " pounds.\n" +
    "On Jupiter you would weigh " + str(round(earth_weight * 2.34, 2)) + " pounds.")
    
   
   
if __name__ == '__main__':
   weight_on_planets()
