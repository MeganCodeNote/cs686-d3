#!/usr/bin/env python
# sample.py
__author__ = "megan_lee"

""" Sample a portion of the data from a larger file and reformat them
    for the splom.js to use
"""
import csv
import random
import math

def readin_data(filepath):
    '''read in the csv file'''
    fobj = open(filepath, 'rbU')
    lines = []
    reader = csv.reader(fobj)
    for line in reader:
        lines.append(line)
    fobj.close()
    return lines

def sample_lines(lines, percentage):
    '''select a portion of lines'''
    total_lines = int(len(lines) * percentage)
    line_no = []
    for i in range(total_lines):
        num = int(math.floor(random.random() * total_lines))
        if num not in line_no and num != 0:
            line_no.append(num)
    return [lines[k] for k in line_no]

def reformat_data(keys, lines):
    '''reformat data for the splom script to use'''
    res = []
    for line in lines:
        reformated_line = {}
        for i in range(len(keys)):
            # print keys[i]
            # print line[i]
            key, val = keys[i], float(line[i])
            # print key, val
            if key == 'longitude':
                continue
            if key == 'latitude':
                val = 'color_' + str(int((val - 32) / 2))
            reformated_line[key] = val
        res.append(reformated_line)
    return res

def gen_file(output_path, values, traits):
    f = open('out.json', 'w')
    res = {}
    res['traits'] = ["median income", "housing median age", "median house value", "households", "total bedrooms", "total rooms", "population"]
    res['values'] = values
    print len(values)
    res['latitude'] = ['color_0', 'color_1', 'color_2', 'color_3', 'color_4']
    res = str(res).replace("'", '"')
    f.write(res)
    f.close()

if __name__ == '__main__':
    lines = readin_data('houses.csv')
    slines = sample_lines(lines, 0.042)
    rlines = reformat_data(lines[0], slines)
    gen_file('out.json', rlines, lines[0])
     
