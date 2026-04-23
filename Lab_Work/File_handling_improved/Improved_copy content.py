#imolementing exception handling to avoid exception
try:
    with open("source.txt", "r") as source_file:
        file_content = source_file.read() #opening file in read mode

    with open("destination.txt", "w") as destination_file:
        destination_file.write(file_content)#opening file in write mode

    print("File copied successfully") #printing the message 

except FileNotFoundError:
    print("source.txt not found")

except Exception as e:
    print("Error:", e)