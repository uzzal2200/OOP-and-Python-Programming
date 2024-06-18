# program to know about * args ans ** key args of python

def args(*arguments):
    sum = 0
    for number in arguments:
        sum += number
    return sum

def kargs(**args):
    for key, value in args.items():
        print(key, value)



sum = args(10,20,30,40)
print(sum)

kargs(name = 'Jhankar Mahbub', profession = 'teacher', respect_of_phitron_team = '100 %')