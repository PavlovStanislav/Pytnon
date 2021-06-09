str1 = 'This is a string. '
str2 = ' This is another string.'
print(str1 + str2);

print('Length of ', str1, 'is ', len(str1));

print(str1.title());

print(str2.lower());

print(str2.upper());

print(str1.rstrip());

print(str2.lstrip());

str3 = ' ABC '
print(str3.strip());  
 
str4 = '_ ABC _'
print(str4.strip('_'));

# cahrs

ch = str1[0:4]
print (ch);

ch1 = str1[:]
print (ch1);

ch2 = str1[10:]
print (ch2);

ch3 = str1[:7]
print (ch3);

str5 = 'A1-B2-C3-D4-'
ch4 = str5[3:10:2]
print (ch4);

# numbers

a = 5
b = 2

print(a//b);

print(a%b);

print(a**b);

var = "string" + "5"
print(var);

# data format

param = "string" + str(15)
print(param);

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3);

# string format

a = 1/3
print("{:7.3f}".format(a));

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b));

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("{:7.3s}".format(n1) + " plus " + "{:7.3s}".format(n2) + " = " + "{:7.3f}".format(n3));

# lists

list1 = [11,5,78,99,55,1,3]
dir(list1);

list1.sort(reverse=True)
print(list1);

list2 = [3,5,6,2,33,6,11]
list3 = sorted(list2)
print(list3);

# sorted lists

print(dir(tuple))
help(list3.count)
help(list3.index);

seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(listseq)
print(type(listseq))
listseq.append(100)
print(listseq)
listseq.sort(reverse=True)
print(listseq);

# dictionaries

D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D);

dp = {}
length = int(input("Input dictionary length: "))
for element in range(0,length):
 dp[input()] = input()
 print(dp);
 
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 25}

print('Full name: '+rec['name']['firstname']+' Lastname: '+ rec['name']['lastname'])
print('Name: '+rec['name']['firstname'])
print("Jobs: {job}".format(**rec));

rec['job'].append('janitor')
print(rec['job']);

print("Name: {0}: \n Jobs: {1} \n Age: {2}".format(rec['name'],rec['job'],rec['age'] ));




