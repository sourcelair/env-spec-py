import re

def check_latin_chars(input_str):
    """
    function that checks if input_str consists of latin chars 
    (input_str can contain underscore and numeric digits)
    """
    try:
        input_str.encode('utf-8').decode('ascii')
    except Exception:
        return False
    else:
        return True


def check_symbols(input_str):
    """
    checks input_str (must be digit/underscore/uppercase latin char)
    return False for error about specifications or True if correct
    """
    alphanumeric_that_does_not_start_with_digit = r'^[A-Z_][0-9A-Z_]*$'

    ret = re.match(alphanumeric_that_does_not_start_with_digit, input_str)

    if ret == None:
        return False
    else:
        return True


def check_input(field_array):
    """
    Checks syntax of input(uppercase latin chrars,numeric digits, underscores).
    Returns False for error or True for correct syntax.
    """
    for line in field_array:       
        
        latin_chars = check_latin_chars(line)
        if(latin_chars == -1):
            print('1.SYNTAX ERROR: NOT LATIN CHARS!')
            return False
        
        #syntax check for existing digits / underscore on string
        ret = check_symbols(line)
        if (ret == False):
            print('2.SYNTAX ERROR:WRONG SYMBOLS!')
            return False
    
    print('---Correct syntax of given specificarions---')
    return True


def render_env_var_spec(env_var_name):
    ret_str = ''
    env_var_name_lower = env_var_name.lower()

    ret_str = f'<label for="env_spec_{env_var_name_lower}"> {env_var_name}</label>'
    ret_str += '\n'
    ret_str += f'<input id="env_spec_{env_var_name_lower}" name="{env_var_name_lower}" />'

    return ret_str

def render_env_spec_to_html(field_array):
    html_output = []
    ret = check_input(field_array)  #check syntax

    if (ret == True):
        for field in field_array:  
            html_output.append(render_env_var_spec(field))  #create html output

        html_output = '\n'.join(html_output)
   
    return html_output


def main():
    field_array = []
    field_array = spec_str.split('\n')
   
    html_output = render_env_spec_to_html(field_array)

    return html_output

if __name__ == "__main__":
    spec_str = 'DATABASE_URL\nADMIN_EMAIL\nDEBUG'

    print(main())
