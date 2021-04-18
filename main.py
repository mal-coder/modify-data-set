"""
Task 1
Read data in the provided file, modify and output the modified data
Requirements:
1. Load and read the file (from the file, do not put data into a variable)
2. Sort the data by the customer number
3. Update the modified date to the current date
4. Change the format of created date to UTC
5. Return the data as string
6. Provide option to output the data as HTML
"""

from datetime import datetime

from helpers import clean_cust_no, format_date_to_utc, convert_data_to_string, convert_data_to_html

# Data file path
file_path = './example.txt'
# Regex pattern where we search for substring starting with a capital letter followed by
# one or more number or capital letter
cust_no_pattern = '[A-Z][\dA-Z]+'
# Known possible misspellings in the customer number int part
cust_no_int_fixes = [('O', '0'), ]
# Default datetime format
datetime_format = '%d/%m/%Y %H:%M'


def main(html: bool = False) -> str:
    columns = None
    content = list()
    now = datetime.now().strftime(datetime_format)
    with open(file_path) as input_file:
        for row_number, row_content in enumerate(input_file):
            row = [element.strip() for element in row_content.split('\t')]
            if row_number == 0:
                columns = row
            else:
                row[0] = clean_cust_no(row[0], cust_no_pattern, cust_no_int_fixes)
                row[5] = format_date_to_utc(row[5], datetime_format)
                row[6] = now
                content.append(row)
    # Sort list by customer number: first letter then number
    content.sort(key=lambda x: (x[0][0], int(x[0][1:])))

    if html:
        print(convert_data_to_html(columns, content))
        return convert_data_to_html(columns, content)
    else:
        # Add column names to the rest of data
        content.insert(0, columns)
        print(convert_data_to_string(content))
        return convert_data_to_string(content)


if __name__ == '__main__':
    main(html=True)
