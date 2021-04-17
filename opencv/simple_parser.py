"""
Implementation: 

Run the following command: 

python simple_parser.py -n YourName      

"""
# import libraries
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required = True, help = 'name of the user.')
args = vars(ap.parse_args())

''' vars  on the object to turn the parsed command line
 arguments into a Python dictionary where the key to the 
 dictionary is the name of the command line argument and 
 the value is value of the dictionary supplied for the 
 command line argument.
 '''
print(args)
print('*' * 51)
print(f"Hi there {args['name']}, nice to see you here!")
