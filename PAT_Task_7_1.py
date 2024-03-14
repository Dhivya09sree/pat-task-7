import datetime
def create_text_file_with_timestamp():
    # Generate current timestamp
    current_time = datetime.datetime.now().strftime("%d-%m-%y_%H-%M-%S")
    
    # Create a text file with the current timestamp
    filename = f"D:/timestamp_{current_time}.txt"
    # Write current timestamp to the file
    with open(filename, 'w') as file:
        file.write(current_time)

    print(f"Text file '{filename}' created with the current timestamp.")

# Call the function to create the text file with the current timestamp
create_text_file_with_timestamp()
