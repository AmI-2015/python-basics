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
    name = 'Anthony "Tony" Stark'
    age = 45 # not a lie
    height = 174 # cm
    weight = 78 # kg
    eyes = 'brown'
    teeth = 'white'
    hair = 'brown'
    
    print "Let's talk about %s." % name
    print "He's %d cm tall." % height
    print "He's %d kg heavy." % weight
    print "Actually that's not too heavy."
    print "He's got %s eyes and %s hair." % (eyes, hair)
    print "His teeth are usually %s depending on the coffee." % teeth
    # this line is tricky, try to get it exactly right
    print "If I add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight)


if __name__ == '__main__':
    main()