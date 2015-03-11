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
    a = [1, 2, 3]
    print 'The first list is', a

    b = [4, 5, 6]
    print 'The second list is', b

    c = a + b
    print 'List concatenation:', c

    d = c[1:3]
    print '1-3 slicing of the concatenated list', d

    e = c[:3]
    print '0-3 slicing of the concatenated list', e

    f = c[:]
    print 'Full slicing of the concatenated list', f
    
    
if __name__ == '__main__':
    main()