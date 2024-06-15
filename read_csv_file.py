import csv
import os

def read_csv_file(filename):
  """Reads data from a CSV file and returns a list of lists."""
  if not os.path.exists(filename):
    raise FileNotFoundError(f"File '{filename}' does not exist.")

  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
      data.append(row)

  return data

if __name__ == '__main__':
  filename = 'input.csv'
  data = read_csv_file(filename)

  print(data)
