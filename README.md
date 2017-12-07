# initial problem

Write a program that reads a list of csv(comma separated values) records and 
sort the list based on the first field. Use your language of choice, but write 
the sort method or function yourself.  Make sure the program compiles and 
executes. The program should use stdin and stdout for reading and writing the 
answers.

## some clarification on constraints/limits

It will be unsigned integers for the first column. 0 <= column value <=2000000

The list will not go  above 100000 entries

And the header will be included as part of the list.
e.g.

code,country,Color
203,China,Green
202,Japan,Blue
207,Korea,Red

# notes on solution

## testing the script

run shell script to run test
tested with random mock data from mockaroo (1000 rows)

## notes on performance

more data might require a higher recursion limit
there may be more efficient implementations

but the use of quicksort on just the numbers of the first
column provides an average of nlog(n) (at least in theory) and copying the
rest of the data for each row into an associative array (or dictionary, in python)
should reduce the amount of data actually being sorted quite significantly

## notes on implementation

though this implementation will only work if the data from the first column is numeric
i.e. it won't work if the data to sort with is on any other csv column (possible TODO...?)

other possible problems may include memory or CPU constraints, specially if csv file
is significantly big, in either amount of data per row, and amount of rows
