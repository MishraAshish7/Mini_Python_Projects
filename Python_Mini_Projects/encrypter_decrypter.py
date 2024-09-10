# Function 1: This function will store all salt values
def salts():
    import random

    # Salt which is basically the main ingredient of our recipe
    salt = ["*@($12$", "423h4", "ewj7", "jlsow3", "3h2","ash", "ish", "1%@", "HSs", "a2a", "ksam&", "%@lc", "mko", "s03",
            "*@%S", "vAI", "q9#", "lauA", "Y!617",",wso.2(", "ka8", ")-1m", "ka^2", "ba%2", "ksi(@", "bdu4", "au3", "ja",
            "neu3", "nj23r", "iuo", "nkj409", "ayu", "sh", "BJ@", "&*(", "kj*", "@#(", "mk", "pos", "wqd9", "a7ha", "js",
            "o*@*", "*@HS", "ka9", "ns8", "(@Js", "nsU*#", "lsis", "nxus", "pwie", "os*", "@j", "ks9[", "!`", "jsus", "hs"
            "SUBX", "ius", "*()", "jis", "i91", "nx7", "ow8", "o9", "2js", "jwq", "iue", "9i3", "32k", "dwj", "ijd", "q89",
            "rc3", "UKxB", "84Cp", "RB+", "N5c", "NZw", "$I1", "iyM", "SCi", "XsC", "7cH", "D1B", "/2g", "twb", "hE2",
            "3q5", "NVa", "eXp", "6t0I", "w+x4","jxE", "bMh", "UnX", "BrT", "8eB", "OEy", "KBS", "g$U", "OvS", "Uql",
            "Ptc", "QX/", "U2I", "mvv", "vWG","TXC", "W1Z", "T2N", "8/E", "qSX", "SI4", "RpM", "Ifc","82r","ENH","2JD",
            "oKC","TYs","38A","$ZI","4b/","YcV","DfQ","3uG","l38","6id","B+t","GT3","L1C","Ddw","RlV","PzR","bQX","BQ"
            "sxY","vt6","1Vj","DQm","ajy","uUX","Qe5","uzu","12g","CiB","55L","OMm","dSP","j9Q","sE9","xKF","OFI","e6",
            "9dz", "THZ", "d5F", "Kwp", "zii", "MTH", "LB.", "ua8", "Iar", "wvu", "JNk", "PN1", "3Ii", "5J/", "lk.",
            "2wZ", "/pi", "nq", "vXt","Dm9","1.A","qBg","N18","4fw","qn4",".j.","N0D","A0B","8oe","0Xk","bqg","tXj",
            "1GC","LeT","rVB","ae", "/Bl","Jg.","8mM","2kZ","Mer","mdW","qU.","F0T","ckL","DXW","7hB","LwY","xOO","2qB",
            "gfj","rpY","4mde", "FFV","G3W","EtC","LKg","kwO","3BI","Ghb","eTd","JNu","1go","Z9c","ykq","HeG","nzK","MQC",
            "m0L","GtD","K", "uVz","TQw","wa/","qO3","QVu","C7V","AuW","eBr","c01","Fsw","YNf","UK8","Ung","F3z",".RI",
            "rCS","h7t","1G"]

    # Shuffling salt
    random.shuffle(salt)

    return salt


# Function 2: This function will store all possible characters that user can include in their password
def characters():

    import string as st

    # Normal encryption characters
    chars = " " + st.digits + st.ascii_letters + st.punctuation

    # converted the characters into list
    char_to_list = list(chars)

    return char_to_list


# Function 3: This function will store all keys for the characters that we created earlier/before
def chars_keys():
    # Based on normal characters list, we created an keys  list to provide each value a key
    keys = ['(', 'T', '`', '{', 'v', '!', '$', 'z', '_', '^', 'p', 'e', 'V', '0', '6', 'o', '&', '-', '"', 'w', 'R', "'", 'O', '<', '.', 'L',
            'b', 'm', 'U', '>', 'i', 'G', 'k', 'd', ' ', 'h', 'c', ',', 'q', '3', 'X', 'M', '[', '|', 'g', 'Q', '2', 'C', 's', 'N', 'H', 'S',
            'P', '7', 'D', '@', '9', 'j', '?', 'K', 't', 'F', '8', '%', 'A', '~', '5', '/', 'y', '1', 'J', 'W', '=', 'B', ')', 'f', 'E',
            'u', 'Y', '*', '+', 'x', ']', ';', 'a', '4', '#', 'I', '}', 'l', ':', 'n', 'r', 'Z']
    return keys


# Function 4: Encrypter
def encrypter():

    #Taking user inputs to encrypt
    user_input = input("Enter password to encrypt: ")

    # Importing salt values from salts() function
    salt = salts()

    # Importing character values from characters() function
    char_to_list = characters()

    # Importing keys values of characters from char_keys() function
    keys = chars_keys()

    # The string where we will store the encrypted password
    encrypted_value = ""

    # Main loop to convert our password into encrypted password
    #Level 1: Encryption
    for i in user_input:
        index = char_to_list.index(i)
        encrypted_value += keys[index]
    print("Encrypted password: ", encrypted_value)


    #Level 2: Adding some salt to our Encrypted password
    after_salt = ""

    for i in range(0, len(encrypted_value), 2):
        after_salt += salt[i]
    after_salt += (salt[6] + encrypted_value[:3] + salt[4] + salt[7] + salt[1] + encrypted_value[3:6] + salt[2] + salt[8] +
                   encrypted_value[6:] + salt[3] + salt[11] + salt[13] + salt[12])


    print("Password after adding salt: ",after_salt)

    # Level 3: Adding some masala
    after_masala = ""

encrypter()


# Function 5: Decrypter
def decrypter():

    # Importing salt values from salts() function
    salt = salts()

    # Importing character values from characters() function
    char_to_list = characters()

    # Importing keys values of characters from char_keys() function
    keys = chars_keys()

    # Taking hashed values from the user to decrypt
    pass_2_decrypt = input("Enter hashed value to Decrypt: ")

    # Removing all salts from our hashed password
    for i in salt:
        pass_2_decrypt = pass_2_decrypt.replace(i, "")

    print("Password after removing salt: ",pass_2_decrypt)

    # Decrypting
    decrypted = ""

    for i in pass_2_decrypt:
        index = keys.index(i)
        decrypted += char_to_list[index]
    print("Decrypted password: ", decrypted)

decrypter()
