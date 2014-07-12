# -*- coding: utf-8 -*-
import sys
import json
import pprint

def load_data(json_fl):
    data_file = open(json_fl)
    return json.load(data_file)

def extract_by(key, value, arr_of_obj, extra_value = None):
    result = []
    for obj in arr:
        if type(obj[key] == str):
            obj[key] = obj[key].lower()
        if extra_value:
            if value or extra_value in obj[key]:
                #print obj
                result.append(obj)
        elif value in obj[key]:
            #print obj
            result.append(obj)
    return result
def count_by(key, arr_of_obj):
    result = {}
    for obj in arr:
        if obj[key] not in result:
            result[obj[key]] = 1
        else:
            result[obj[key]] += 1
    return result


def print_stats(total, subset):
    total_length = len(total)
    subset_length = len(subset)
    perc_subset = float(subset_length) / total_length * 100
    print "Total students: %d" % (total_length)
    print "Total Computer Science students: %d" % (subset_length)
    print "Percentage of Computer Science students:", round(perc_subset, 2), "%"


def main ():
    data_array = load_data(sys.argv[1])
    comp_sci = extract_by("PROGRAM", "compu", data_array) + extract_by("PROGRAM", u"cómp", data_array)
    pprint.pprint(comp_sci[:10])
    print_stats(data_array, comp_sci)

if __name__ == '__main__':
    main()