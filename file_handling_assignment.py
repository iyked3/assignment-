def handle_file_operations():
    """Performs file creation, reading, appending, and error handling."""

    try:
        # Create and write to the file
        with open("my_file.txt", "w") as file:
            file.write("This is the first line of text.\n")
            file.write("This is the second line, containing a number: 123\n")
            file.write("And this is the final line of the initial content.\n")

        # Read and display the file contents
        with open("my_file.txt", "r") as file:
            print("File contents:")
            print(file.read())

        # Append to the file
        with open("my_file.txt", "a") as file:
            file.write("Appended line 1\n")
            file.write("Appended line 2, including a string and number: hello 456\n")
            file.write("This is the last appended line.\n")

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operations complete.")


if __name__ == "__main__":
    handle_file_operations()
