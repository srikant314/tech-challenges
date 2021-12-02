import json
import sys

def get_value(object,input_key,tmp):
    key_array = [ x.strip() for x in input_key.split('/') ]
    #print(key_array)
    #json_object = json.loads(object)
    #print("The type is : ", type(object))
    #print("The value is : ", object)
    for key, value in (object.items()):
         if tmp == 0:
             #print("Temp value recursive tracking is:", tmp)
             #print("Value of keep_array is:", key_array[tmp] )
             #print("Dict Value 1st entry tracking recursively: ", list(object.keys())[0])
             if (key_array[tmp] != list(object.keys())[0]):
                 sys.exit('Alert !!!!!!! There is no value available for provided key.Please recheck !!!!!! ')
             tmp = tmp + 1
         if type(value) is dict:
            if tmp != 0:
                #print("Temp value recursive tracking is:", tmp)
                #print("Value of keep_array is:", key_array[tmp] )
                #print("Dict Value entries tracking recursively: ", list(value.keys())[0])
                if (key_array[tmp] != list(value.keys())[0]):
                    sys.exit('Alert !!!!!!! There is no value available for provided key.Please recheck !!!!!! ')
            get_value(value,input_key,tmp+1)
         else:
            print("Output Value fetched from the Object: ", value)



#if __name__ == '__main__':
#pass values for nested json object and key
#   object = input("Please enter the nestesd json object for which value needs to be extracted\n")
#   key = input("Please enter the key for which value needs to be extracted\n")
#   print(get_value(object,key))

#test case1
print("**********************************************")
print("******LIST OF EXECUTED USECASES***************")
print("**********************************************")
print("*****USECASE-1********************************")
print("**********************************************")
object={"a":{"b":{"c":"d"}}}
#object={"dict1": {"a": 1},"dict2": {"b": 2}}
input_key="a/b/c"
print("Input object provided for usecase1: ", object)
print("Input Key provided for usecase1: ", input_key)
tmp=0
get_value(object,input_key,tmp)

#test case2
print("**********************************************")
print("*****USECASE-2********************************")
print("**********************************************")
object={"x":{"y":{"z":"a"}}}
input_key="x/y/z"
print("Input object provided for usecase2: ", object)
print("Input Key provided for usecase2: ", input_key)
tmp=0
get_value(object,input_key,tmp)


#test case3
print("**********************************************")
print("*****USECASE-3********************************")
print("**********************************************")
object={"a":{"b":{"c":"d"}}}
#object={"dict1": {"a": 1},"dict2": {"b": 2}}
input_key="a/c/b"
print("Input object provided for usecase1: ", object)
print("Input Key provided for usecase1: ", input_key)
tmp=0
get_value(object,input_key,tmp)


print("**********************************************")
print("******END OF USECASES*************************")
print("**********************************************")
