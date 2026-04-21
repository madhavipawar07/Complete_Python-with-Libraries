import argparse
parser = argparse.ArgumentParser()

parser.add_argument("arg1",help ="Description of argument 1")

parser.add_argument("arg2",help="Description of argument 2")

#parse the arguments because we have to use the values of arguments in our code
args= parser.parse_args()
print(args.arg1)
print(args.arg2)

#Adding Optional arguments

parser = argparse.ArgumentParser()

parser.add_argument("-o1", "--optional1", help="Description of optional argument 1", default="default value")
parser.add_argument("-o2", "--optional2", help="Description of optional argument 2", default="default value")

args = parser.parse_args()

print(args.optional1)
print(args.optional2)

#Adding arguments with types
parser = argparse.ArgumentParser()

parser.add_argument("-n",type=int,help="Description of integer argument")
args= parser.parse_args()
print(args.n)