Matrix Validation

1. Problem statement

Given two matrice , check whether both matrices are valid or not 

A matrix is considered valid when ------

* Both matrices contain at least one row
* Both matrices have the equal number of row 
* Both matrices have the same number of columns 
* Every row has the same number of columns .
* And any matrix should not contain None

Return True if both matrices are valid  else  return False .

2. Example

Input:

m1 = [
    [5, 23, 64],
    [53, 64, 12],
    [3, 53, 53]
]
m2 = [
    [1, 2, 4],
    [5, 3, 6],
    [64, 42, 53]
]

Output:
True

Both matrices have 3 rows and 3 columns , and neither contain None .

3. Approach

* Check whether both matrices have equal number of row
* Find the first elements number of column/element
* Iterate over every row and check its column count
* check whether any row contains None
* If all conditions are satisfied return True

4. Code Explanation

* len() checks the number of rows and columns
* for loop to visit every row
* None in row checks whether a row contains a None or not
* return False immediately stops validation when an invalid condition is found
* return True executes when all validation conditions are True
