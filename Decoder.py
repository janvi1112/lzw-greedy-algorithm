# Name: Janvisree Puligundla
# Student ID: 801308951

import sys
# Function to decode the data encoded 
def decoder(encoded_data, bit_length):
    Max_table_size = 2**bit_length  
    #Creating a dictionary with 0 to 255 characters
    dictionary = {i:chr(i) for i in range(256)}

    # When the file is empty
    if len(encoded_data)==0:
        return " "
    
    string = dictionary[encoded_data[0]]
    output_data = string
    print(string)

 
    for current in encoded_data[1:]:
        if current in dictionary:
            current_string = dictionary[current]
        else:
            current_string = string + string[0]
            
        output_data += current_string
        if len(dictionary) < Max_table_size:
            dictionary[len(dictionary)] = string + current_string[0]
        
        string = current_string
        print(current_string)
        
    return output_data
# Function to read byte data from lzw file
def reading_encoded_data(file_name):
    encoded_data = []
    two_byte = file_name.split('.')[0] + '.lzw'
    two_byte_file = open(two_byte, 'rb')
    while True:
        data =two_byte_file.read(2)
        if not data:
            break
        encoded_data.append(int.from_bytes(data,byteorder='big'))
    two_byte_file.close()
    return encoded_data

#Funtion to store decoded into text file
def store_decoded_data_in_file(file_name, decoding_data):
    # Generating output file with _decoded.txt extension
    decoded_file_name = file_name.split('.')[0] + '_decoded.txt'
    decoded_file = open(decoded_file_name, 'w')
    decoded_file.write(decoding_data)
    decoded_file.close()

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
    data = reading_encoded_data(file_name)

    # Decoding the encoded data
    decoding_data = decoder(data, bit_length)
    # Storing decoded data in a file
    store_decoded_data_in_file(file_name, decoding_data)

if __name__ == "__main__":
    main()