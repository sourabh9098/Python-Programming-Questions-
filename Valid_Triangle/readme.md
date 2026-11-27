# Triangle Validation and Type

## 1. Problem Statement

Given three sides of a triangle , check they can form a valid triangle ?

If the triangle is valid , check its type 

- Equilateral Triangle : All three side are equal 
- Isosceles Triangle : Any two sides are equal 
- Scalene Triangle : All three sides are different 

## 2. Example

**Input:**
a = 5
b = 6
c = 7

**Output:**
Scalene Triangle


## 3. Approach

First , check whether all three sides are positive

Next  apply the Triangle Inequality Theorem . The sum of any two sides must be greater than the third side 

If the triangle is valid , compare the three sides to identify its type