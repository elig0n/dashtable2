
import subprocess
import os

from dashtable import html2rst, html2md
from dashtable.utils.files import read_text

CWD = os.getcwd()


for file in os.listdir(CWD + '/test_files'):
    if file.endswith('.html'):
        path = os.path.join(CWD, 'test_files', file)

        with open(path, 'r') as f:
            lines = f.readlines()
        string = ''.join(lines)

        converted_rst = html2rst(string)
        converted_md = html2md(string)

        md_name = os.path.splitext(path)[0] + '.md'
        with open(md_name, 'r') as md_file:
            md_lines = md_file.readlines()
        md_string = ''.join(md_lines).rstrip()

        if not md_string == converted_md:
            print('MarkDown Error: ' + file)

        rst_name = os.path.splitext(path)[0] + '.rst'
        with open(rst_name, 'r') as rst_file:
            rst_lines = rst_file.readlines()
        rst_string = ''.join(rst_lines).rstrip()

        if not rst_string == converted_rst:
            print('reStructered Error: ' + file)

path = os.path.join(CWD, 'test_files', 'main_example.html')
md_outfile = os.path.join(CWD, 'test.md')
rst_outfile = os.path.join(CWD, 'test.rst')
html2md = os.path.join(CWD, 'dashtable', 'html2md.py')
html2rst = os.path.join(CWD, 'dashtable', 'html2rst.py')
command_1 = ['python', html2md, path, md_outfile]
command_2 = ['python', html2rst, path, rst_outfile]
subprocess.call(command_1)
subprocess.call(command_2)

f = open(md_outfile, 'r')
md_string = ''.join(f.readlines())
f.close()

f = open(os.path.join(CWD, 'test_files', 'main_example.md'), 'r')
converted_md = ''.join(f.readlines())
f.close()

if not md_string == converted_md:
    print('Command Line Error for MarkDown')

f = open(rst_outfile, 'r')
rst_string = ''.join(f.readlines())
f.close()

f = open(os.path.join(CWD, 'test_files', 'main_example.rst'), 'r')
converted_rst = ''.join(f.readlines())
f.close()

if not rst_string == converted_rst:
    print('Command Line Error for reStructered')

os.remove(md_outfile)
os.remove(rst_outfile)



