# -*- coding: utf-8 -*-
import sys
import json
import pprint

def load_data(json_fl):
    data_file = open(json_fl)
    return json.load(data_file)

def extract_by(key, value, arr_of_obj, extra_value = None):
    result = []
    for obj in arr_of_obj:
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
def assignDate(arr_of_obj):
    for obj in arr_of_obj:
        if obj["CALENDARIO"]:
            obj["year"] = obj["CALENDARIO"][-5:]

def count_by(key, arr_of_obj):
    result = {}
    for obj in arr_of_obj:
        category = obj[key].lower()
        if category not in result:
            result[category] = 1
        else:
            result[category] += 1
    return result

def mean (arr):
    total = 0
    for num in arr:
        total += num
    return total/len(arr)
def calc_objs_avg(key, arr_of_obj):
    arr = []
    for obj in arr_of_obj:
        if obj[key]:
            arr.append(obj[key])
    return round(mean(arr),2)

def print_stats(total, subset):
    assignDate(subset)
    total_length = len(total)
    subset_length = len(subset)
    perc_subset = round(float(subset_length) / total_length * 100, 2)
    genders = count_by("GENERO", subset)
    perc_male = round(float(genders["masculino"]) / subset_length * 100, 2)
    perc_female = round(float(genders["femenino"]) / subset_length * 100, 2)
    avg_gpa =  calc_objs_avg("GPA", subset)
    years = count_by("year", subset)
    print "Total students: %d" % (total_length)
    print "Total Computer Science students: %d" % (subset_length)
    print "Percentage of Computer Science students:", perc_subset, "%"
    print "Percentage of Male Computer Science students:", perc_male, "%"
    print "Percentage Female Computer Science students: ", perc_female, "%"
    print "Average GPA:", avg_gpa
    print "Admissions by Year:"
    for tup in years.items():
        print tup[0], tup[1]


def main ():
    data_array = load_data(sys.argv[1])
    comp_sci = extract_by("PROGRAM", "compu", data_array) + extract_by("PROGRAM", u"cómp", data_array)
    pprint.pprint(comp_sci[:10])
    print_stats(data_array, comp_sci)

if __name__ == '__main__':
    main()