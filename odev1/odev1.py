sayi1=8
sayi2=8.3
sayi3=2022
sayi4="50"

print(type(sayi1)) #<class 'int'>

print(type(sayi2)) #<class 'float'>

print(type(sayi4)) #<class 'str'>

print(type(str(sayi1))) #<class 'str'>

sayi1_str=str(sayi1)
print(sayi1_str) #8
print(type(sayi1_str)) #<class 'str'>

sayi1_float=float(sayi1)
print(sayi1_float) #8.0
print(type(sayi1_float)) #<class 'float'>

sayi2_str=str(sayi2)
print(sayi2_str) #8.3
print(type(sayi2_str)) #<class 'str'>

sayi2_int=int(sayi2)
print(sayi2_int) #8
print(type(sayi2_int)) #<class 'int'>

sayi3_str=str(sayi3)
print(sayi3_str) #2022
print(type(sayi3_str)) #<class 'str'>

sayi3_float=float(sayi3)
print(sayi3_float) #2022.0
print(type(sayi3_float)) #<class 'float'>

sayi4_int=int(sayi4)
print(sayi4_int) #50
print(type(sayi4_int)) #<class 'int'>

sayi4_float=float(sayi4)
print(sayi4_float) #50.0
print(type(sayi4_float)) #<class 'float'>