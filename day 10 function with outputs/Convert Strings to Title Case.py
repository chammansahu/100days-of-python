def titleCase(str):
     ls = str.split(' ')
     result=""
     for item in ls:
         result+=(item[0].upper()+item[1:])+" "
     return result  
print(titleCase('chammman sahu Gullo'))    