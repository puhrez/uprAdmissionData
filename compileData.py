# -*- coding: utf-8 -*-
import sys
import json
import pprint

#function: load_data
#parameter: json file
#process: opens the file and loads it
#output: the loaded json dicect
def load_data(json_fl):
    data_file = open(json_fl)
    return json.load(data_file)

#function: extract_by
#parameter: a key, the desired value, a list of dictionaries, and optional extraValue
#process: iterates through the list of dicts checking to see if the dict's key has the desired value
# if so it appeneds it to the resulting lisay
#output: the lisay of all the dicts with the desired value for the specified key
def extract_by(key, value, list_of_dict, extra_value = None):
    result = []
    for dic in list_of_dict:
        if type(dic[key] == str):
            dic[key] = dic[key].lower()
        if extra_value:
            if value or extra_value in dic[key]:
                #print dic
                result.append(dic)
        elif value in dic[key]:
            #print dic
            result.append(dic)
    return result

#function: assignDate
#parameter: a list of dictionaries
#process: assigns to each dictionary a "year" key whose value is the academic year
#output: modifies the object
def assignDate(list_of_dict):
    for dic in list_of_dict:
        if dic["CALENDARIO"]:
            dic["year"] = dic["CALENDARIO"][-5:]

#function: count_by
#parameter: a key to count by, a list of dictionaries
#process: similiar to a GROUP BY ($group), this sums the distinct occurence of key values
#output: a dictionary of the key values with their frequency
def count_by(key, list_of_dict):
    result = {}
    for dic in list_of_dict:
        category = dic[key].lower()
        if category not in result:
            result[category] = 1
        else:
            result[category] += 1
    return result

#function:
#parameter:
#process:
#output:
def find_city(list_of_dict):
    result = []
    for dic in list_of_dict:
        location = dic['Location 1'].lower()
        to_splice = location.index('\n')
        dic['city'] = location[:to_splice]
        if dic['city'] not in result:
            result.append(dic['city'])
    return result

#function: mean
#parameter: a list 
#process: it sums the list and divides it by the list's length
#output: returns the mean of the list
sum()
def mean (lis):
    return sum(lis)/len(lis)

#function: calc_dics_avg
#parameter: a key to average by, a list of dicts
#process: it iterates through the dicts and appends the value of the key
#output: returns the mean of the list of key values
def calc_dics_avg(key, list_of_dict):
    lis = []
    for dic in list_of_dict:
        if dic[key]:
            lis.append(dic[key])
    return round(mean(lis),2)

#function:
#parameter:
#process:
#output:
def print_cities(population):
    city_count = count_by('city', population)
    print "Cities students came from:"
    for tup in city_count.items():
        print tup[0], tup[1]

#function: sortByValue
#parameter: a dictionary
#process: sorts the keys by their values
#output: returns an asending (by value) list of keys
def sortByValue(dic):
   return sorted(dic, key= dic.get)

#function: printDic
#parameter: a list of keys for sort, a dictionary to iterate through, a limit (int), and whether ascending (False) or descending (True)
#process:prints the key and its value for the order specified by keys under the specified limit
#output: prints the dict
def printDic(keys, dic, limit, inversed):
    #print dic #for debugging
    count = 0
    if inversed:
        for key in reversed(keys):
            if count > limit:
                break;
            print key, dic[key]
            count += 1
    else:
        for key in keys:
            if count > limit:
                break;
            print key, dic[key]
            count += 1

def print_stats(total, subset):
    assignDate(subset)
    total_length = len(total)
    subset_length = len(subset)
    perc_subset = round(float(subset_length) / total_length * 100, 2)
    genders = count_by("GENERO", subset)
    perc_male = round(float(genders["masculino"]) / subset_length * 100, 2)
    perc_female = round(float(genders["femenino"]) / subset_length * 100, 2)
    avg_gpa =  calc_dics_avg("GPA", subset)
    years = count_by("year", subset)
    sorted_year = sorted(years)
    dest_campus =  count_by("CAMPUS", subset)
    campuses = sortByValue(dest_campus)
    print "Total students: %d" % (total_length)
    print "Total Computer Science students: %d" % (subset_length)
    print "Percentage of Computer Science students:", perc_subset, "%"
    print "Percentage of Male Computer Science students:", perc_male, "%"
    print "Percentage Female Computer Science students: ", perc_female, "%"
    print "Average GPA:", avg_gpa
    print "Admissions by Academic Year:"
    printDic(sorted_year, years, len(sorted_year), False)
    print "Destination Campus:"
    printDic(campuses, dest_campus, len(campuses), True)


def main ():
    data_lisay = load_data(sys.argv[1])
    comp_sci = extract_by("PROGRAM", "compu", data_lisay) + extract_by("PROGRAM", u"cómp", data_lisay)
    pprint.pprint(comp_sci[:10])
    print_stats(data_lisay, comp_sci)

    places = find_city(comp_sci)

    print_cities(comp_sci)

if __name__ == '__main__':
    main()