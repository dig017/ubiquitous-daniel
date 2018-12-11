import string
import random


def creditcard(number):
    """This function checks a True Credit Card by verifying that the input is an integer and subsequently checks if that 
    input's length is 16 characters.
    
    Parameters:
    -----------
    number: list
        list of strings, for it to run the first string must be a integers otherwise nothing is returned.
        if string is a integer it returns True if it is 16 chars long, and False if not
    """
    if number[0].isdigit() == True:
        if len(number[0]) == 16:
            return True
        else:
            return False
        
def selector(input_list, check_list, return_list):
    """This function is checking for inputs from the chatbox. Initially, it is checking for the word no and then for
    a potential subsequent input from the input_list. If the word is not no, then the input is taken from its respective
    input_list.
    
    Parameters: input_list, check_list, return_list
    -----------
    element: list
        for this function to run you must input no and if another word is followed by no, it checks both words and
        pulls it from the respective list. 
        if the input does not contain no, the output will come from the respective list where that input is located
   
    """
    output = None
    for index, word in enumerate(input_list):
        if word in check_list:
            #Checks input for no and subsquent input to return a particular list
            if word == 'no' and input_list[index +1] in check_list:
                output = random.choice(return_list)
                break
            elif word != 'no':
                output = random.choice(return_list)
                break

    return output


def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise.
     
    Parameters: list_one, list_two
    -----------
    list_one: list
        list of objects
    list_two: list
        A differnt list of objets
    
    Returns:
    --------
    element: int, float, or string
        Item that is in both list_one and list_two, if none exist then None returned
        
    Examples:
    ---------
    
    >>> list1 = [1,2,3,4]
    >>> list2 =  [5,2,6,3,8]
    >>> find_in_lihttp://localhost:8889/notebooks/Desktop/BurritoBot/FinalProjectFinalCopy.ipynb#nst(list1, list2)
    2
    
    """
    
    for element in list_one:
        if element in list_two:
            return element
    return None


def is_in_list(list_one, list_two):
    """The following function is checking to see if any element in list_one is in list_two
    
    Parameters: list_one, list_two
    
    
    """
    
    for element in list_one:
        if element in list_two:
            return True
    return False


def question_asked(input_string):
    """This function is checking the input of the chat box for ? in order to output the appropiate list. 
    
    Parameters: input_string
    
    """
    
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output


def string_concatenator(string1, string2, separator):
    
    result = string1 + separator + string2
    
    return result


def remove_punctuation(input_string):

    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
            
    return out_string

def prepare_text(input_string):
 
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list


def defined_output(input_list, check_list, return_list, questionNumber):

    output = None
    for word in input_list:
        if word in check_list:
            output = return_list[questionNumber]
            break

    return output


def list_to_string(input_list, separator):
    
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output


def end_chat(input_list):
    
    if 'bye' in input_list:
        output = True
        
    elif 'cancel' in input_list:
        output = True
        
    elif 'goodbye' in input_list:
        output = True
        
    else:
        output = False
        
    return output






