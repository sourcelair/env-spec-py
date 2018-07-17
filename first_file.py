field_array = []

#perilambanei kai _ kai arithmous
#function that checks if input_str consists of latin chars
def check_latin_chars(input_str):
    try:
        input_str.encode('utf-8').decode('ascii')
    except Exception:
        return -1
    else:
        return 0

#def numeric_digit(input_str):


def check_input(file_object):
    for line in file_object:    #save lines at field_array
        print('in here: ', line)
        
        line = line.replace('\n','')       #remove \n char
        field_array.append(line)

    for line in field_array:        #check syntax  if syntax error ret = -1 else ret = 0
        latin_chars = check_latin_chars(line)
        
        if((line.isupper() == False) and (latin_chars == -1)):
            print('SYNTAX ERROR!')
            return -1
        
        if(line[0].isdigit()):
            print('SYNTAX ERROR!')
            return -1
        
        #syntax check for existing digits / underscore on string

       

        
        

        
        
       
        

        
      





env_filename = input('Give the env.spec file... ')     
file_object = open(env_filename, 'r')

check_input(file_object)
print(field_array)