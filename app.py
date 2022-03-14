#!/usr/bin/python3
import json, secrets, os
from toolcase import fillup, finder, validation

def main():

    ALLOWED_EXTENSIONS = ['docx', 'DOCX', 'json', 'JSON']

    inputfile = input("Give the full path and name of docx file (ex. /home/usr/test/sample_1.docx):  ")
    metadatafile = input("Give the full path and name of json file (ex. /home/usr/test/data_1.json):  ")
    
    if os.path.exists(inputfile) and os.path.exists(metadatafile):

        # define values
        final_dict = {}
        type_lists = []
        temp_list = []
        list_value = []
        temp_dict = {}

        outputfile = "./documents/" + secrets.token_hex(15) + '.docx'

        # Opening JSON file
        f = open(metadatafile)
        # returns JSON object as a dictionary
        data = json.load(f)

        # Iterating through the json list
        for item in data['metadata']:
            #print(item)
            if item['mergetype'] == 'object' or item['mergetype'].__contains__('object'):
                final_dict[item['mergename']] = item['mergevalue']
            else:
                if item['mergetype'] not in type_lists:
                    type_lists.append(item['mergetype'])

        if len(type_lists) == 0:
            print('there are no lists objects')
            exit()

        for the_type in type_lists:
            for item in data['metadata']:
                if item['mergetype'] == the_type:
                    list_name = str(the_type)
                    temp_list.append(item)

            # sort list by line key
            temp_list = sorted(temp_list, key = lambda x: x['line'])
            # find last record into the list
            last_record = temp_list[-1]
            last_work_line = int(last_record['line'])
            current_line = 1

            while current_line <= last_work_line:
                # read record for specific line into the list
                for x in temp_list:
                    if int(x['line']) == current_line:
                        temp_dict[x['mergename']] = x['mergevalue']
                list_value.append(dict(temp_dict))
                current_line += 1

            temp_list = []
            final_dict[list_name] = list_value
            list_name = ''
            list_value = []
            current_line = 0
            last_work_line = 0

            print(final_dict)
        # Closing file
        f.close()
        
        # find document merge fields
        merge_fields = finder.findDocument_MergeFields(inputfile)
        if merge_fields is not None or merge_fields != '':
            print()
            #print(merge_fields)
            print()
            for ml in merge_fields:
                print(ml)
        else:
            print('Error occured in mail merge finder procedure')

        # create docx document and merge content
        status_temp = fillup.createDocument(inputfile, final_dict, outputfile)
        if status_temp == True and os.path.exists(outputfile):
            print('Input file is ' + inputfile)
            print()
            print('Metadata file is ' + metadatafile)
            print()
            print('Output file is ' + outputfile)
        else:
            print('Error occured in mail merge fillup procedure')

    else:
        print('Input files docx or json not exist')


# called by command line to start the program
if __name__ == "__main__":
    print('Input paramteres are a docx file and a json file')
    print()
    main()
