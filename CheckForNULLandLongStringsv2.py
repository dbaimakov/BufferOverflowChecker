import PyPDF2

def check_for_null_and_longstrings(filename):
    try:
        has_null = False
        long_string_flag = False
        with open(filename, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                text = page.extract_text()
                if '\0' in text:
                    has_null = True
                for word in text.split():
                    if len(word) > 1000:
                        long_string_flag = True
                        break
        return has_null, long_string_flag
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

filename = input("Please enter the full path to the PDF file: ")
has_null, has_long_string = check_for_null_and_longstrings(filename)

if has_null is None and has_long_string is None:
    print("There was an error checking the file.")
else:
    if has_null:
        print("File contains NULL characters.")
    else:
        print("File does not contain NULL characters.")
    if has_long_string:
        print("File contains strings longer than 1000 characters.")
    else:
        print("File does not contain any strings longer than 1000 characters.")
