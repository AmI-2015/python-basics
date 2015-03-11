'''
Created on Mar 10, 2015
Copyright 2015 Luigi De Russis
 
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
    course_name = 'Ambient Intelligence'
    
    string_len = len(course_name)
    print string_len # 20
    
    print course_name.lower() # ambient intelligence
    
    print course_name.upper() # AMBIENT INTELLIGENCE

    pi = 3.14
    print 'The value of pi is around ' + str(pi)


if __name__ == '__main__':
    main()