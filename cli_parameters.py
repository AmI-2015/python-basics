'''
Created on Mar 6, 2014
Copyright 2014-2015 Dario Bonino and Luigi De Russis
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
   
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

@author: bonino, derussis
'''

from sys import argv

if __name__ == '__main__':
    script, first, second, third = argv #argv unpacking
    
    print 'The script is called:', script
    print 'Your first variable is:', first 
    print 'Your second variable is:', second
    print 'Your third variable is:', third 