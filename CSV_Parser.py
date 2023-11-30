import csv


def find_and_save_lines(file_path, search_values, output_file):
    found_lines = set()  # Use a set to store unique rows

    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for column_value in row:
                for search_value in search_values:
                    if search_value in column_value:
                        found_lines.add(tuple(row))  # Convert row to tuple to make it hashable
                        break  # Break out of inner loop once the value is found in a row
                else:
                    continue
                break  # Break out of outer loop once the value is found in a row

    if found_lines:
        with open(output_file, 'a', newline='') as output_csv:  # Use 'a' for append mode
            writer = csv.writer(output_csv)
            writer.writerows(found_lines)
        print(f"Unique lines containing {search_values} saved to {output_file}")
    else:
        print(f"No lines containing {search_values} found")


file_path = 'Minerva_123.csv'
output_file = 'output.csv'
# Can search for multiple values
search_values = []

find_and_save_lines(file_path, search_values, output_file)
