def weight_on_planets():
   # write your code here
    earth_weight = (float(input("What do you weigh on earth? ")), end='')
    print("On Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(round(earth_weight * .38, 2), round(earth_weight * 2.34, 2)))
    
   
   
if __name__ == '__main__':
   weight_on_planets()
