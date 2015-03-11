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
    letters = ['a', 'b', 'c']
    print 'The list is', letters
    letters.append('d')
    print 'The list now is', letters

    print 'The first element of the list is', letters[0]

    print 'The list length is', len(letters)

    letters[3] = 'e'
    print 'Finally, the list is', letters

if __name__ == '__main__':
    main()