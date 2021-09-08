Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  import os
>>> list_dir = os.listdir('.')
>>> list_dir = [f.lower() for f in list_dir]   # Convert to lower case
>>> sorted(list_dir)
['dlls', 'doc', 'etc', 'include', 'lib', 'libs', 'license.txt', 'news.txt', 'python.exe', 'pythonw.exe', 'readme.txt', 'scripts', 'share', 'tcl', 'tools', 'w9xpopen.exe']