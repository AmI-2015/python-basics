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
    print 'How old are you?',
    age = raw_input()
    print 'How tall are you?',
    height = raw_input()
    print 'You are %s years old, and you are about %s cm tall.' % (age, height)


if __name__ == '__main__':
    main()
