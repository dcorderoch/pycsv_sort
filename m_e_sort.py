import sys # handle stdin
import csv # read csv with csv.reader ( stdin )

sys.setrecursionlimit(10000)

# parse command line
raw_csv = sys.stdin

# initialize a dictionary to use the first column value as a key,
# and the rest as the value

row_dict = {}

# initialize a list to store the first column values,
# to use quicksort on
codes = []

# initialize header, and fill the dictionary and codes list
is_it_first = False
for row in csv.reader ( raw_csv ):
    if is_it_first == False:
        is_it_first = True
        header = row
    else:
        code = int ( row[0] )
        codes.append ( code )
        row_dict[code] = row[1:]

# quicksort implementation for a list (as opposed to an array)
# there may be a more efficient way to implement
def quicksort ( lst ):
    if lst == []:
        return []
    else:
        pivot = lst[0]
        lesser = quicksort([x for x in lst[1:] if x < pivot])
        greater = quicksort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater

# sort the codes, store in another variable to use to traverse the dictionary
sorted_codes = quicksort ( codes )

# print the header as csv to stdout
print ( ','.join ( header ) )

# print the registers of the dictionary as csv
for i in sorted_codes:
    print ( str ( i ) + ',' + ','.join ( row_dict[i] ) )
