#!/usr/bin/python3
import json, secrets, os
from toolcase import fillup, finder, validation

def main():

    ALLOWED_EXTENSIONS = ['docx', 'DOCX', 'json', 'JSON']

    inputfile = input("Give the full path and name of docx file (ex. /home/usr/test/sample_1.docx):  ")
    metadatafile = input("Give the full path and name of json file (ex. /home/usr/test/data_1.json):  ")
    
    if os.path.exists(inputfile) and os.path.exists(metadatafile):

        outputfile = "./documents/" + secrets.token_hex(15) + '.docx'

        # Opening JSON file
        f = open(metadatafile)
        # returns JSON object as a dictionary
        metadata = json.load(f)
        # Iterating through the json list
        for i in metadata['metadata']:
            #print(i)
            pass
        # Closing file
        f.close()
        # print(metadata['metadata'])

        # find document merge fields
        merge_fields = finder.findDocument_MergeFields(inputfile)
        if merge_fields is not None or merge_fields != '':
            print()
            #print(merge_fields)
            print()
            for l in merge_fields:
                print(l)
        else:
            print('Error occured in mail merge finder procedure')

        # create docx document and merge content
        status_temp = fillup.createDocument(inputfile, metadata['metadata'], outputfile)
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


if __name__ == "__main__":
    print('Input paramteres are a docx file and a json file')
    print()
    main()
