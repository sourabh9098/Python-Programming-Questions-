# Find the Second Largest Number in a List

## 1 Problem Statement

Given a list of numbers , find the second largest distinct number without sorting the list

**Example:**

```python
a = [54, 54, -float('inf'), 20, 10, 543, 121]

##Output 121
```

Explanation:
- Largest number = 543
- Second-largest number = 121

## 2 Approach

We use two variables:

- `largest` :- Stores the largest number.
- `sec` :- Stores the second largest distinct number 

We traverse the list using a single `for` loop and update these variables whenever we find a larger or second largest number 

## 3 Python Code

```python
a = [54, 54, -float('inf'), 20, 10, 543, 121]

def second_large(n):

    if len(n) > 1:
        largest = n[0]
        sec = None

        for ele in n:
            if ele > largest:
                sec = largest
                largest = ele

            elif sec != None and largest > ele > sec:
                sec = ele

            elif sec == None and ele < largest:
                sec = ele

        return sec

    return "Collection Not Valid"


print(second_large(a))

```

## 4 Code Explanation

Step 1: Initialize variables

largest = n[0]
sec = None


Initially  we assume the first element is the largest We set {sec} to {None} because we havent found the second largest number yet 

Step 2 : Traverse the list

for ele in n:

This loop visits every element in the list one by one.

Step 3: Find a new largest number

if ele > largest :
    sec =  largest
    largest = ele


If the current element is greater than the largest number , the previous largest becomes the second largest and the current element becomes the new largest

Step 4 : Update the second largest number


elif sec != None and largest > ele > sec:
    sec = ele


If the current element is smaller than the largest but greater than the second largest , we update {sec}

Step 5 : Handle the initial second-largest number

elif sec == None and ele < largest:
    sec = ele

If we have not found a second-largest number yet , the first element smaller than the largest becomes the second-largest.

After completing the loop we return the second largest distinct number

## 5 Dry Run

Input:

a = [54, 54, -float('inf'), 20, 10, 543, 121]


| Current element | largest | sec |
|---:|---:|---:|
| 54 | 54 | None |
| 54 | 54 | None |
| -∞ | 54 | -∞ |
| 20 | 54 | 20 |
| 10 | 54 | 20 |
| 543 | 543 | 54 |
| 121 | 543 | 121 |

Final Output
121