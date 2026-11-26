m1 = [ [ 5, 23, 64 ] ,
       [53, 64 , 12] ,
       [3 , 53, 53]]

m2 = [ [ 1 ,2 ,4] ,
       [5 ,3 ,6 ] ,
       [64 ,42 ,53]]

m2 = [[ 1, 2, 4 ] ,
      [ 5, 3, 6] ,
      [ 64, 42 ]]

m2 = [[5, 23, 64 ] ,
      [53, 64, 5] ,
      [3 , 53, None]]

m2 = [ [ 5, 23, 64 ] ,
      [53, 64, 5] ,
      None]


## Check both matrix for matrix addition 
def valid_matrix(m1 , m2):
      # check  both matrice have equal rows , matrices are non empty ,also checked any have None 
      if len(m1) == len(m2) and len(m1)>0 and not ( None in m1 or None in m2) :

            # Get the number of columns/elment in first row
            length = len(m2[0])

            for row in range(len(m1)):

                  # Check whether any row contains None
                  if None in  m1[row] or None in m2[row]:
                        return False
                  
                  # Check whether the both matrix's row have equal columns/no element
                  elif len(m1[row]) != length or length != len(m2[row]) :
                        return False
            # matrices are valid
            return True
      return False

print(valid_matrix(m1 , m2))