import os
from shutil import copyfile
import string

cite_fn = 'Citations.bib'
out_tex_file = 'pull_citetation.tex'
base_dir = '.'

def pull_all_cite():    
    cite_file = file(cite_fn,'r')
    cite_lines = cite_file.readlines()
    out_file = file(out_tex_file,'w')
    for l1 in cite_lines:
        if l1.find('@') == 0:
            key1 = l1.split('{')[1]
            key2 = key1.split(',')[0]
            outline = "\\section{ \\citefield{"+key2+"}{title} \\cite{"+key2+"}  } \n  \\citefield{"+key2+"}{abstract} \n"
            out_file.write(outline) 
    out_file.flush()
    out_file.close()
    
def rename_files():
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    file_list = os.listdir(base_dir)
    pdf_name_list =[]
    for f_name in file_list:
        if f_name.find('.pdf') > 0:
            fname_2 = f_name.strip('.pdf')
            pdf_name_list.append(fname_2)
    cite_file = file(cite_fn,'r')
    cite_lines = cite_file.readlines()
    for l1 in cite_lines:
        if l1.find('@') == 0:
            key1 = l1.split('{')[1]
            key2 = key1.split(',')[0]
        if l1.find('title') == 0:
            key3 = l1.split('{')[1].strip('\n').strip(',').strip('}')
            for pdf_fn in pdf_name_list:
                if pdf_fn.find(key2) >= 0:
                    print key2,key3
                    out_fn = key3+'.pdf'
                    out_fn2 = ''.join(c for c in out_fn if c in valid_chars)
                    copyfile(pdf_fn+'.pdf',out_fn2)
                    
                
    
    print pdf_name_list
        
