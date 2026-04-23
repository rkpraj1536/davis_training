# Open the input file in read mode
with open("students.txt", "r") as student_file:

    # Read all lines from the file and store them in a list
    student_records = student_file.readlines()

# Open the output file in write mode
# If the file already exists, its old content will be removed
with open("top_students.txt", "w") as output_file:

    # Go through each line one by one
    for record in student_records:

        # Remove extra spaces and newline characters from the line
        record = record.strip()

        # Skip the line if it is empty
        if record == "":
            continue

        # Split the line using comma
        # Example:
        # "Rahul,82,Meerut" becomes ["Rahul", "82", "Meerut"]
        student_data = record.split(",")

        # Check whether the line contains exactly 3 values:
        # name, marks, city
        if len(student_data) == 3:

            try:
                # Store each value in separate variables
                name = student_data[0]      # Student name
                marks = int(student_data[1])  # Convert marks from string to integer
                city = student_data[2]      # Student city

                # Check if the student's marks are greater than 75
                if marks > 75:

                    # Write the student record into the output file
                    output_file.write(f"{name},{marks},{city}\n")

            # This block runs if marks cannot be converted to integer
            # Example: "Rahul,abc,Meerut"
            except ValueError:

                # Print an error message for invalid records
                print("Invalid marks found in record:", record)

# Display a final success message after all processing is complete
print("Filtered student records saved in top_students.txt")