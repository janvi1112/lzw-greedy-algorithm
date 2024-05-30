# Name: Janvisree Puligundla
# Student id: 801308951

import sys


# Function to encode the data
def encoder(data, bit_length):
    # Maximum table size = 2^bit_length
    Max_table_size = 2**bit_length  
     # Initializing the table with ASCII characters
    dictionary = {chr(i):i for i in range(256)} 
    output_code = []
    string = ""
    # When the file is empty
    if data=="":
        return output_code
    
    for current in data:
        current_string = string + current
        if current_string in dictionary:
            string = current_string
        else:
            print(dictionary[string])
            output_code.append(dictionary[string])
            if len(dictionary) < Max_table_size:
                dictionary[current_string] = len(dictionary)
            string = current
    # Adding the last encoded string
    if string:
        output_code.append(dictionary[string])
        print(dictionary[string])
    return output_code

# Fuction to store encoded data into lzw file
def store_encoded_data_in_file(file_name,  encoding_data):
    # Generating output file with .lzw extension
    byte_file_name = file_name.split('.')[0] + '.lzw'
    byte_file = open(byte_file_name, 'wb')
    # Writing data in two byte format
    for c in encoding_data:
        m=c.to_bytes(2,byteorder='big')
        byte_file.write(m)
        
    byte_file.close()
    
    
# Main function
def main():
    # Getting command line arguments and validating format and bit length
    
    if len(sys.argv) != 3:
        print("Please enter arguments in proper format:  <file-name> <bit-length>")
        sys.exit(1)
    if int(sys.argv[2])<8 or int(sys.argv[2])>16:
        print("Please enter bit length between 8 and 16")
        sys.exit(1)

    file_name = sys.argv[1]
    bit_length = int(sys.argv[2])
    data = open(file_name, 'r').read()

    # Encoding the data
    encoding_data = encoder(data, bit_length)
    # Storing the encoded data in a file
    store_encoded_data_in_file(file_name, encoding_data)
    

if __name__ == "__main__":
    main()