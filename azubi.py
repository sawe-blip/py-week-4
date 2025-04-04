def read_and_modify_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Open the file for reading
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify the content (e.g., make all text uppercase)
        modified_content = [line.upper() for line in content]

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()