#!C:\Users\suraj\Desktop\Project\Code\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'img2pdf==0.3.6','console_scripts','img2pdf'
__requires__ = 'img2pdf==0.3.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('img2pdf==0.3.6', 'console_scripts', 'img2pdf')()
    )
