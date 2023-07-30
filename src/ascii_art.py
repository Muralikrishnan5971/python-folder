def print_ascii(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))

print_ascii('007.txt')
