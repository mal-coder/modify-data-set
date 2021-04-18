import re
from datetime import datetime, timezone


def clean_cust_no(cust_no: str, cust_no_pattern: str, cust_no_int_fixes: list[tuple]) -> str:
    # Remove characters other than alphanumerical
    cust_no = re.search(pattern=cust_no_pattern, string=cust_no).group(0)
    # Fix customer's number int part char misspellings
    for pair in cust_no_int_fixes:
        cust_no = f"{cust_no[0]}{cust_no[1:].replace(pair[0], pair[1])}"
    return cust_no


def format_date_to_utc(input_date: str, datetime_format: str) -> str:
    input_date = datetime.strptime(input_date, datetime_format).replace(tzinfo=timezone.utc)
    return input_date.isoformat()


def convert_data_to_string(data: list) -> str:
    str_data = str()
    for row in data:
        current_row = '\t'.join(row) + '\n'
        str_data += current_row
    return str_data


def convert_data_to_html(columns: list, content: list) -> str:
    html_header = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<table>'
    html_footer = '</table>\n</body>\n</html>'
    # Build table header
    table_columns = '<tr>\n'
    for column in columns:
        table_columns += f'<th>{column}</th>\n'
    table_columns += '</tr>\n'
    # Build table body
    table_rows = str()
    for row in content:
        current_row = '<tr>\n'
        for element in row:
            current_row += f'<td>{element}</td>\n'
        current_row += '</tr>\n'
        table_rows += current_row

    html_data = f'{html_header}{table_columns}{table_rows}{html_footer}'
    return html_data
