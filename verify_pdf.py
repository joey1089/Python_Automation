#Verify if the given PDF file is complete or not or its corrupt or clean
import os


def isFullPdf(f):
    ''' Function to detect a pdf file is completed or not. '''
    end_content = ''
    start_content = ''
    size = os.path.getsize(f)
    if size < 1024: return False 
    with open(f, 'rb') as fin: 
        #start content 
        fin.seek(0, 0)
        start_content = fin.read(1024)
        start_content = start_content.decode("ascii", 'ignore' )
        fin.seek(-1024, 2)
        end_content = fin.read()
        end_content = end_content.decode("ascii", 'ignore' )
    start_flag = False
    #%PDF
    if start_content.count('%PDF') > 0:
        start_flag = True
    
        
    if end_content.count('%%EOF') and start_flag > 0:
        return True
    eof = bytes([0])
    eof = eof.decode("ascii")
    if end_content.endswith(eof) and start_flag:
        return True
    return False

print("============================= PDF file complete or not! ===============================")
