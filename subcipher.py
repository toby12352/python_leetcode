import sys 
from string import digits, ascii_letters 
from random import sample

# use this for your original alphabet string 
ALL_LETTERS_DIGITS = digits + ascii_letters 
# use this random key if none is provided, try printing it out to see what it is 
# RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))
RANDOM_KEY = 'cHzd9PDMSpWJrT5RVOXyNlb0AEmKkG8tjwUe7CF34B2s6oYh1qiaIvfLnZxQgu'

# add your functions here

def split_str(msg, lst):
    for i in range(len(msg)):
        lst.append(msg[i])
    return lst

def add_str(lst):
    converted_msg = ''
    for i in lst:
        converted_msg += i
    return converted_msg


def encrypt(msg, ekey = RANDOM_KEY):
    lst = []
    split_str(msg, lst)

    for i in range(len(lst)):
        if ALL_LETTERS_DIGITS.count(lst[i]) > 0:
            index_key = ALL_LETTERS_DIGITS.index(lst[i])
            print(index_key)
            lst[i] = ekey[index_key]
        else:
            pass

    return add_str(lst)

def decrypt(msg, key):
    lst = []
    split_str(msg, lst)

    for i in range(len(lst)):
        if key.count(lst[i]) > 0:
            index_key = key.index(lst[i])
            lst[i] = ALL_LETTERS_DIGITS[index_key]
        else:
            pass
    
    return add_str(lst)


# Do not modify the arguments for main, we will call it directly 
def main(action: str, msg: str, key: str): 
    if(len(key) == 0):
        key = RANDOM_KEY
    
    print(ALL_LETTERS_DIGITS)
    print(key)

    # print(encrypt('HLA HTOO', RANDOM_KEY))
    if action == 'encrypt':
        encrypted = encrypt(msg, key)
        print(f"Encrypted={encrypted}")
        print(f"Key={key}")
    elif action == 'decrypt':
        decrypted = decrypt(msg, key)
        print(f"Decrypted Message is: {decrypted}")

    """ Starting point of your program. You must start here.
    print(ALL_LETTERS_DIGITS)
    print(RANDOM_KEY)
    print(encrypt('HLA HTOO  @#'))
    print(decrypt('sh7 sLii  @#', RANDOM_KEY))"""
    pass  # replace with your code


# The following allows us to run various features from the command line 
# do not modify. 
# If you wish to run the program from the command line 
# You could do the following 
# > python subcipher.py "Aloha, World" 
# that will encrypt this is my message and return both message and key 
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the message 
# > python subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO" 
if __name__ == "__main__": 
    # check to see if there are command line arguments 
    _action = 'encrypt' 
    _msg = '' 
    _key = '' 
    if len(sys.argv) > 1: 
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt': 
            _action = 'decrypt' 
            remainder = sys.argv[2:] 
        else: 
            remainder = sys.argv[1:] 
        if len(remainder) > 0: 
            _msg = remainder[0] 
            if len(remainder) > 1: 
                _key = remainder[1] 
    main(_action, _msg, _key) 
