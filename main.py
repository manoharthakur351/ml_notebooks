print("loading....\nplease wait")
import os
import numpy as np
from sklearn import linear_model

os.system('clear')
# FUNCTIONS


def getFloatLst (lst):
	"""
	convert string or in array into float arrey
	"""
	float_lst = []
	for a in lst:
		float_lst.append(float(a))
	return float_lst

def twoDArr ():
	'''
	returns 2D array of the data'''
	with open("data.txt") as f:
		data = f.read()
	required_data = data.split("\n")
	required_data.pop()

	main_list = []
	for element in required_data[1:]:
		list = element.split(" ")
		float_sub_lst = getFloatLst(list)
		main_list.append(float_sub_lst)
	required_array = np.array(main_list)
	return required_array

# FUNCTIONS TO GET TRAINING DATA
def getTrainX():
	arr = twoDArr ()
	transpose = arr.T
	lst = []
	for a in transpose[:-1]:
		lst.append(a)
	
	arr = np.array(lst)
	return arr.T


def getTrainY():
	arr = twoDArr ()
	transpose = arr.T
	lst = []
	for a in transpose[-1:]:
		lst.append(a)
	
	arr = np.array(lst)
	return arr.T

# FUNCTION TO UPDATED DATA
def update_data (lst):
	strng = f"{float(lst[0])} {float(lst[1])} {float(lst[2])} {float(lst[3])} {float(lst[4])}\n"
	s = strng
	with open("data.txt",'a') as f:
		f.write(strng)
		


# FUNCTION TO TEST.
def test ():
	x = getTrainX()
	y = getTrainY()
#	print(x)
#	print(y)
	m = linear_model.LinearRegression()
	m.fit(x,y)
	
	with open("data.txt") as f:
		data = f.read(33)
		lst = data.split(" ")
	lst.pop()
	entriesF = []
	entriesS = []
	for a in lst:
		inp = input(a+": ")
		entriesF.append(float(inp))
		entriesS.append(inp)
#	print(entriesS)
#	print(entriesF)
	pridiction = m.predict([entriesF])
#	print(pridiction)
	return pridiction,entriesS
	
	


# MAIN FUNCTION
def main ():
	n= test()
	entriesS = n[1]
	pridiction = n[0]
	print("\n according to model the price of the notebook is\n\t:", pridiction,'\n')
	msg = input('do you want to to update data ?[y/n] ')
	if msg in 'Yy':
		 msg1 = input ("what was the right Price of the notebook.?_\n\t:")
		 entriesS.append(msg1)
		 print("adding ",*entriesS,"to the data.")
		 update_data(entriesS)
	input('PRESS ENTER TO EXIT.')
	os.system('clear')
	return

if __name__ == "__main__":
	while True:
		main()