'''
Created on Mar 12, 2014
Copyright 2014-2015 Luigi De Russis
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
   
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

@author: derussis
'''

from sys import argv

def main():
    filename = argv[1] #argv unpacking, take the second element

    txt = open(filename)
    print "Here's your file %r:" % filename
    print txt.read()

    print "\nType the filename again:"
    file_again = raw_input("> ")

    txt_again = open(file_again)

    print txt_again.read()
    
    
if __name__ == '__main__':
    main() 