## The Curry Wholesaler problem
You run a Curry Wholesaler, and there are a few different types of Curry you can
prepare for take-away customers. Each Curry can be either "vegetarian" or "meat".\
You have a number of customers, and each have some Curries that they like, either
veggie or meat.\
No customer will like more than one Curry with meat.\
You want to mix the Curries, so that:\
There is just one batch for each type of Curry, and it's either Vegetarian or Meat.\
For each customer, there is at least one Curry they like.\
You make as few Meat Curries as possible (because they are more expensive).\
Your program should accept an input file as a command line argument, and print a
result to standard out. An example input file is:

5\
1 M 3 V 5 V\
2 V 3 M 4 V\
5 M

The first line specifies how many Curries there are (5 in this case).\
Each subsequent line describes a customer. For example, the first customer likes
Curry 1 with Meat, Curry 3 as Veggie and Curry 5 as Veggie .\
Your program should read an input file like this, and print out either that it is
impossible to satisfy all the customers, or describe, for each of the Curries, whether
it should be made Vegetarian or Meat.\

The output for the above file should be:\
`V V V V M`

...because all customers can be made happy by every Curry being prepared as
Veggie except number 5.\

An example of a file with no solution is:\
1\
1 V\
1 M
Your program should print:\
`No solution exists`

A slightly richer example is:\
5\
2 M\
5 V\
1 V\
5 V 1 V 4 M\
3 V\
5 V\
3 V 5 V 1 V\
3 V\
2 M\
5 V 1 V\
2 M\
5 V\
4 M\
5 V 4 M

...which should print:\
`V M V M V`

One more example. The input:\
2\
1 V 2 M\
1 M

...should produce\
`M M`


