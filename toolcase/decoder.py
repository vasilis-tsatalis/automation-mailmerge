import os
from base64 import b64decode

def base64_convert_to_docx(input_file, output_file):
    """this function convert a base64 string to docx document"""
    with open(input_file, 'r') as open_file_1:
        content = open_file_1.read()
        bbytes = b64decode(content, validate=True)
    open_file_1.close()
    with open(output_file, 'wb') as open_file_2:
        open_file_2.write(bbytes)
    open_file_2.close()    
    if os.path.isfile(output_file):
        status = True
    else:
        status = False
    return status
