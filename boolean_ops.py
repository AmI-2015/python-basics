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
    print '2 == 1 and True is', 2 == 1 and True # False
    print '2 == 2 or True is', 2 == 2 or True # True
    print '10 >= 2 and 2 != 1 is', 10 >= 2 and 2 != 1 # True
    print 'not True is', not True # False
    print '10 > 5 and 10 == 10 or 5 < 2 is', 10 > 5 and 10 == 10 or 5 < 2 # True
    print 'not False and True is', not False and True # True
    
    
if __name__ == '__main__':
    main()