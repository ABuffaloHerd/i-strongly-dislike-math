import math, playsound
import random as rng
    
def validateFloat(number):
    """Ensures that a number is float. Returns bool. Broken"""
    try:
        float(number)
    except ValueError:
        print("You must input a number.")
        return False
    finally: pass

def validate_int(question):
    """General validation function. Returns number"""
    while True:
        try:
            ans = int(input(question))
            return ans
        except ValueError: print("You must input an integer!")
            
def validate_int_withLimits(question, high, low):
    """General validation function but with compulsory limits. Returns number"""
    while True:
        try:
            ans = int(input(question)) #Asks question and recieves input
            if ans >= low and ans <= high: #Checks that input is within limits and returns if it is
                return ans
            else: print("Your number has to be between", low, "and", high) #Input is not within limits
        except ValueError: print("You must input an integer!") #Stupid poo poo user

def validate_int_v2(question, high = None, low = None):
    """
    General integer validation function version 2, with optional limits. Returns number. 
    Works well with programs that also use the menuLister function, because this can also be used to select menu items
    """
    while True:
        if high != None and low != None: #If both high and low are specified
            try:
                ans = int(input(question)) #Asks question and recieves input
                if ans >= low and ans <= high: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be between {} and {}" .format(low, high)) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user

        elif high == None and low == None: #If high and low unspecified
            try:
                ans = int(input(question))
                return ans

            except ValueError: print("You must input an integer!")    

        elif low == None: #If only HIGH is specified
            try:
                ans = int(input(question)) #Asks question and recieves input
                if ans <= high: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be below", high) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user          

        elif high == None: #If only LOW is specified
            try:
                ans = int(input(question)) #Asks question and recieves input
                if ans >= low: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be above", low) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user


 

def validate_float_v2(question, high = None, low = None, rounded = 4):
    """Float validation function, default rounding to 4dp, with limits. Returns number. Incomplete"""
    while True:
        if high != None and low != None: #If both high and low are specified
            try:
                ans = float(input(question)) #Asks question and recieves input
                if ans >= low and ans <= high: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be between {} and {}" .format(low, high)) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user

        elif high == None and low == None: #If high and low unspecified
            try:
                ans = float(input(question))
                return ans

            except ValueError: print("You must input an integer!")    

        elif low == None: #If only HIGH is specified
            try:
                ans = float(input(question)) #Asks question and recieves input
                if ans <= high: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be below", high) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user          

        elif high == None: #If only LOW is specified
            try:
                ans = float(input(question)) #Asks question and recieves input
                if ans >= low: #Checks that input is within limits and returns if it is
                    return ans

                else: print("Your number has to be above", low) #Input is not within limits
            except ValueError: print("You must input an integer!") #Stupid poo poo user


def menuLister(listToPrint):
    '''
    Lists objects that MUST HAVE A 'name' ATTRIBUTE from a list object that is accepted as a parameter
    Also prints index numbers. Cool aye?
    '''
    for (item, num) in zip(listToPrint, range(len(listToPrint))):
        print(num,"-", item.name)

def YesNo(question, *args):
    '''
    returns true if the answer to the question is Y
    If the user is poopoo stupid, and puts anything other than Y or N then it asks again
    Also supports any other phrase or letter
    '''
    #List all the arguments for the error message
    arguments = ', '.join((ar.upper()) for ar in args)

    #Now the actual loop    
    while True:
        ans = input(question)
        if ans.lower() == 'y' or ans.lower() in args:
            return True #return true if yes
        elif ans.lower() == 'n':
            return False #Return false if no
        else:
            print("Please input Y, {}, or N.".format(arguments))
            continue #Try again if anything else is there

def validate_str(question, limit = None):
    '''
    Asks a question and makes sure that the answer is alphabetical. Returns string
    '''
    while True:
        ans = input(question)
        if limit == None:  #If the limit has not been imposed
            if ans.isalpha():
                return ans
            else:
                print("Your input must be alphanumerical!")
        else: #If limit has been imposed
            if ans.isalpha() and len(ans) <= limit:
                return ans
            else:
                print("Your input must be alphanumerical and {} characters or less!".format(limit))

if __name__ == '__main__':
    print(validate_int.__name__, ":", validate_int.__doc__)
    print(validate_int_v2.__name__, ":", validate_int_v2.__doc__)
    print(validate_int_withLimits.__name__, ":", validate_int_withLimits.__doc__)
    print(validate_float_v2.__name__, ":" , validate_float_v2.__doc__)
    print(menuLister.__name__,":", menuLister.__doc__)

    test = YesNo("Try H or something idfk ", 'h', 'r','f')
    print(test)