spec_str = 'DATABASE_URL\nADMIN_EMAIL\nDEBUG'


def str_split(spec_str):
    """
    split input string by \n and returns strings into an array
    """
    field_array = []
    field_array = spec_str.split('\n')
    
    return field_array

def check_latin_chars(input_str):
    """
    function that checks if input_str consists of latin chars 
    (input_str can contain underscore and numeric digits)
    """

    try:
        input_str.encode('utf-8').decode('ascii')
    except Exception:
        return -1
    else:
        return 0


def check_symbols(input_str):
    """
    checks every char of input_str (must be digit/underscore/uppercase latin char)
    return -1 for error about specifications or 0 if correct
    """

    for i in input_str:   
        #given specifications
        if(i.isdigit() == True or i == '_' or (i >= 'A' and i <= 'Z')):
            continue
        else:
            return -1
        
    return 0


def check_input(field_array):
    for line in field_array:        #check syntax  if syntax error ret = -1 else ret = 0
        
        latin_chars = check_latin_chars(line)
        if((line.isupper() == False) and (latin_chars == -1)):
            print('1.SYNTAX ERROR: NOT UPPER OR LATIN CHAR!')
            return -1
        
        if(line[0].isdigit()):
            print('2.SYNTAX ERROR:STARTS WITH NUMBER!')
            return -1
        
        #syntax check for existing digits / underscore on string
        ret = check_symbols(line)

        if (ret == -1):
            print('3.SYNTAX ERROR:WRONG SYMBOLS!')
            return -1
    
    print('---Correct syntax of given specificarions---')
    return 0


def render_env_var_spec(env_var_name):
    ret_str = ''
    env_var_name_lower = env_var_name.lower()


    ret_str = '<label for="env_spec_'+ env_var_name_lower +'">' + env_var_name + '</label>'
    ret_str += '<input id="env_spec_' + env_var_name_lower + '" name="' + env_var_name_lower + '" />'

    return ret_str


def main():
    field_array = str_split(spec_str)
    ret = check_input(field_array)

    if (ret == 0):
        html_output = []
        for field in field_array:  
            html_output.append(render_env_var_spec(field))

        html_output = '\n'.join(html_output)
        print(html_output)

if __name__ == "__main__":
    main()
