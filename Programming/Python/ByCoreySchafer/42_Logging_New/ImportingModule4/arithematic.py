#run this file to get employee as logger
import logging
#When importing a file module the file executes first and makes employees
import employee

logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y

num_1=10
num_2=5

add_result=add(num_1,num_2)
logging.info("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.info("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.info("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.info("Div {}/{}={}.".format(num_1,num_2,div_result))
