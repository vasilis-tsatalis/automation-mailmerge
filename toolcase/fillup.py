from __future__ import print_function
import os
from mailmerge import MailMerge  # Attention: pip3 install docx-mailmerge

def createDocument(template, metadata, document):
    """this function creates a new docx document based on 
    a template with Merge fields and a JSON content"""      
    the_document = MailMerge(template)
    # the_document.merge_pages([metadata]) # use for json replicas
    the_document.merge(**metadata)

    for item in metadata: # check all the keys
        myitem = metadata[item]
        if isinstance(myitem, list): # check if there are lists in content
            the_document.merge_rows(next(iter(metadata[item][0])), myitem)
    the_document.write(document)

    if os.path.isfile(document):
        status = True
    else:
        status = False
    return status
