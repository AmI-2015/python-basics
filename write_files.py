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
    filename = argv[1]

    print "We're going to erase %r." % filename

    print "Opening the file..."
    target = open(filename, 'w')

    print "... truncating the file.  Goodbye!"
    target.truncate()

    print "\nNow I'm going to ask you for two lines."
    line1 = raw_input("line 1: ")
    line2 = raw_input("line 2: ")

    print "I'm going to write these to the file..."
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")

    print "And finally, we close it."
    target.close()
    
if __name__ == '__main__':
    main()