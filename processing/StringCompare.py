def compare_strings(str1:str=None, str2:str=None) -> int:
    """
    Compares two strings alphabetically. (Not case sensitive)
    
    Parameters:
        str1 (str): 1st String to compare
        str2 (str): 2nd String to compare
        
    Returns:
        int: String which should come first. -1 for str1, 1 for str2, 0 for indeterminate
    """
    if str1 == None or str2 == None:
        return 0
    sort = sorted([str1.upper(), str2.upper()])
    if sort[0] == sort[1]:
        return 0
    if sort[0] == str1.upper():
        return -1
    return 1

def compare_alphanum(str1:str=None, str2:str=None):
    """
    Compares two strings alphabetically and numerically. (Not case sensitive)
    
    Parameters:
        str1 (str): 1st String to compare
        str2 (str): 2nd String to compare
        
    Returns:
        int: String which should come first. -1 for str1, 1 for str2, 0 for indeterminate
    """
    if str1 == None or str2 == None:
        return 0
    result = 0
    end1 = str1
    end2 = str2
    while (result == 0 and (not end1 == "" or not end2 == "")):
        section1 = get_section(end1)
        section2 = get_section(end2)
        end1 = end1[len(section1):]
        end2 = end2[len(section2):]
        result = compare_sections(section1, section2)
    return result

def get_section(input_str:str=None) -> str:
    """
    Returns the first section from a given string.
    Section will contain either only string data or only numerical data.
    
    Parameters:
        input_str (str): Given string
        
    Returns:
        str: First section of input_str
    """
    if input_str == None or input_str == "":
        return ""
    end = 1
    is_num = is_number_string(input_str)
    while (end < len(input_str) and (
           (is_num == False and not is_number_string(input_str[end:])) or
           (is_num == True and is_digit(input_str[end])))):
        end = end + 1
    return input_str[0:end]

def is_digit(char_str:str=None) -> bool:
    """
    Returns whether a single character string is a digit (0-9)
    
    Parameters:
        char_str (str): String of a single character
        
    Returns:
        bool: Whether char_string is a digit
    """
    if char_str == None or not len(char_str) == 1:
        return False
    asc = ord(char_str)
    if asc > 47 and asc < 58:
        return True
    return False

def is_number_string(input_str:str=None) -> bool:
    """
    Returns whether a given string starts with numerical information.
    Returns True if first character is a digit or a decimal point/comma.
    
    Parameters:
        input_str (str): Given string
        
    Returns:
        bool: Whether input_string starts with numerical information.
    """
    if input_str == None:
        return False
    start_char = input_str[0:1]
    if len(input_str) > 1 and (start_char == "." or start_char == ",") and is_digit(input_str[1]):
        return True
    return is_digit(start_char)
    
def compare_sections(str1:str=None, str2:str=None) -> int:
    """
    Compares two string sections.
    Sections should contain either only string information or only numerical information.
    
    Parameters:
        str1 (str): 1st String to compare
        str2 (str): 2nd String to compare
        
    Returns:
        int: String which should come first. -1 for str1, 1 for str2, 0 for indeterminate
    """
    if not str1 == None and not str2 == None:
        digit1 = is_number_string(str1)
        digit2 = is_number_string(str2)
        if digit1 == True and digit2 == True and len(str1) < 11 and len(str2) < 11:
            try:
                val1 = float(str1.replace(",", "."))
                val2 = float(str2.replace(",", "."))
                if val1 < val2:
                    return -1
                elif val1 > val2:
                    return 1
            except ValueError as e:
                print("Invalid number caught: " + str(e))
        else:
            return compare_strings(str1, str2)
    return 0