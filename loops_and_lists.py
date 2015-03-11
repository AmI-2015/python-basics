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
	the_count = [1, 2, 3, 4, 5]
	fruits = ['apples', 'oranges', 'pears', 'apricots']
	change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

	# this first kind of for-loop goes through a list
	for number in the_count:
		print 'This is count %d' % number

	# same as above
	for fruit in fruits:
		print 'A fruit of type: %s' % fruit

	# we can go through mixed lists too
	# notice that we have to use %r since we don't know what's in it
	for i in change:
		print 'I got %r' % i
	
if __name__ == '__main__':
	main()