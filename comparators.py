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

def main():
    print '2 == 1 is', 2 == 1 # False
    print '2 == 2 is', 2 == 2 # True
    print '10 >= 2 is', 10 >= 2 # True
    print '2 < 10 is', 2 < 10 # True
    print '5 != 5 is', 5 != 5 # False
    print "'string' == \"string\" is", 'string' == "string" # True

    number = 123
    print 'The variable "number" is greater than 100?', number > 100 # True


if __name__ == '__main__':
    main()