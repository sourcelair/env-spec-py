spec_str = 'DATABASE_URL\nADMIN_EMAIL\nDEBUG'
field_array = []

#split input string by \n 
def str_split(spec_str):
    global field_array

    field_array = spec_str.split('\n')


#perilambanei kai _ kai arithmous
#function that checks if input_str consists of latin chars
def check_latin_chars(input_str):
    try:
        input_str.encode('utf-8').decode('ascii')
    except Exception:
        return -1
    else:
        return 0

#checks every char of input_str
def check_syntax(input_str):
    for i in input_str:
        if(i.isdigit() == False or i != '_' or (i <= 'A' and i>= 'Z')):
            return -1  
        
    return 0

def check_input(file_object):
    for line in field_array:        #check syntax  if syntax error ret = -1 else ret = 0
        latin_chars = check_latin_chars(line)
        
        if((line.isupper() == False) and (latin_chars == -1)):
            print('SYNTAX ERROR!')
            return -1
        
        if(line[0].isdigit()):
            print('SYNTAX ERROR!')
            return -1
        
        #syntax check for existing digits / underscore on string
        ret = check_syntax(line)

        if (ret == -1):
            print('SYNTAX ERROR!')
            return -1

str_split(spec_str)
#check_input(file_object)
print(field_array)