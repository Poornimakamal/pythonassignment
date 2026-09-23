def change_strings(s):
   s='c'+s[1:]
   print('Inside the functions',s)
my_s='Tap'
print("Before function",my_s)
change_strings(my_s)
print('After function',my_s)