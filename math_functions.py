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

import math

def main():
    signal_power = 10.0
    noise_power = 0.01
    ratio = signal_power / noise_power
    print "ratio:", ratio
    
    decibels = 10 * math.log10(ratio)
    print "decibels:", decibels
    
    radians = 0.7
    height = math.sin(radians)
    print height

if __name__ == '__main__':
    main()