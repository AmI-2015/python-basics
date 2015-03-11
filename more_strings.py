'''
Created on Mar 6, 2014
Copyright 2014-2015 Dario Bonino 
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
   
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

@author: bonino
'''

def main():
    x = "There are %d types of people." % 10
    binary = "binary"
    do_not = "don't"
    y = "Those who know %s and those who %s." % (binary, do_not)
    print x
    print y
    print "I said: %r." % x
    print "I also said: '%s'." % y
    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! %r"
    print joke_evaluation % hilarious
    w = "This is the left side of..."
    e = "a string with a right side."
    print w + e


if __name__ == '__main__':
    main()