import os
from base64 import b64encode

def document_convert_to_base64(encoding, the_file):
    """this function convert a pdf file to base64 format"""

    with open(the_file, 'rb') as open_file:
        byte_content = open_file.read()
    base64_bytes = b64encode(byte_content)
    base64_string = base64_bytes.decode(encoding)  
    return base64_string
