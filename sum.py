def sum(num1,num2):
	num1_int = convert_integer(num1)
	num2_int = convert_integer(num2)
	result = num1_int +num2_int
	return result
def convert_integer(number_string):
	converted_integer = int(number_string)
	return converted_integer
answer = sum("1","2")
print (answer)