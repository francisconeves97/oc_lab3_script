import argparse 
import csv

parser = argparse.ArgumentParser(description="Create CSV from cm1.out.")
parser.add_argument('-f', type=str)

args = parser.parse_args()

""" Receives line, returns dict of line info"""
def treat_line(line):
    info = {}
    info['Array Size'] = line[0].split('array_size=')[1]
    info['Stride'] = line[1].split('STRIDE=')[1][:-1]
    info['Avg Misses'] = line[2].split('avgMISSES=')[1]
    info['Avg Cycl Time'] = line[3].split('avgTIME=')[1][:-1]

    return info

with open(args.f) as f:
    content = f.readlines()

first_line = content[0].split('\t')

current_size = first_line[0].split("array_size=")[1]

csv_file = args.f[:-4]+".csv"

with open(csv_file, 'w') as csvfile:
    field_names = ['Array Size', 'Stride', 'Avg Misses', 'Avg Cycl Time']
    
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    for line in content[1:]:
        line = line.split('\t')
        info = treat_line(line)
        writer.writerow(info)