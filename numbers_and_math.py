'''
Created on Mar 5, 2014
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
    print "I will now count my chickens:"
    print "Hens", 25 + 30 / 6
    print "Roosters", 100 - 25 * 3 % 4
    print "Now I will count the eggs:"
    print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
    print "Is it true that 3 + 2 < 5 - 7?"
    print 3 + 2 < 5 - 7
    print "What is 3 + 2?", 3 + 2
    print "What is 5 - 7?", 5 - 7
    print "Oh, that's why it's False."
    print "How about some more."
    print "Is it greater?", 5 > -2

if __name__ == '__main__':
    main()