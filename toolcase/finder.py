from __future__ import print_function
from mailmerge import MailMerge  # Attention: pip3 install docx-mailmerge

def findDocument_MergeFields(document):
    """this function creates a new docx document based on 
    a template with Merge fields and a JSON content"""      
    the_document = MailMerge(document)
    all_fields = the_document.get_merge_fields()
    res = {element:'' for element in all_fields}
    return res