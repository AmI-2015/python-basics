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
    # map each state to its abbreviation
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA'
    }
    print 'States:', states
    print '\nIs Oregon available?', 'Oregon' in states
    
    # add some more states
    states['New York'] = 'NY'
    states['Michigan'] = 'MI'
    
    # print two states
    print "New York's abbreviation is: ", states['New York']
    print "Florida's abbreviation is: ", states['Florida']

    # print every state abbreviations
    print '-' * 10
    for state, abbrev in states.items():
        print '%s is abbreviated %s' % (state, abbrev)
    
    print '-' * 10
    # safely get an abbreviation of a state that might not be there
    state = states.get('Texas', None)

    if not state:
        print 'Sorry, no Texas.'

    print '-' * 10
    # get a state abbreviation with a default value
    next_state = states.get('Massachusetts', 'Does Not Exist')
    print 'Massachusetts is abbreviated %s' % next_state
    
if __name__ == '__main__':
    main()
    