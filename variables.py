'''
Created on Mar 5, 2014
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
    cars = 100
    space_in_a_car = 4.0
    drivers = 30
    passengers = 90
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven
    
    print 'There are', cars, 'cars available.'
    print 'There are only', drivers, 'drivers available.'
    print 'There will be', cars_not_driven, 'empty cars today.'
    print 'We can transport', carpool_capacity, 'people today.'
    print 'We have', passengers, 'to carpool today.'
    print 'We need to put about', average_passengers_per_car, 'in each car.'

if __name__ == '__main__':
    main()