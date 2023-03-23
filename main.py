from Node import Node

def dfs(matrix, size):
    i=0
    j=0
    pathToReturn = []
    pathToReturn.append(Node(matrix[i][j],i,j))
    visited = set([(0,0)])
    while(True):
        if(matrix[i][j] == 'G' and (i,j) and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            return pathToReturn
        # right,down operator
        elif(matrix[i+1][j+1] == 'R' and i < size and j < size  and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i += 1
            j += 1
        # right,up operator
        elif(matrix[i+1][j-1] == 'R' and i < size and j > 0 and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i += 1
            j -= 1
        # left,down operator
        elif(matrix[i-1][j+1] == 'R' and i > 0 & j < size and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i -= 1
            j += 1
        # left,up operator
        elif(matrix[i-1][j-1] == 'R' and j > 0 & i > 0 and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i -= 1
            j -= 1
        # down operato
        elif(matrix[i][j+1] == 'R' and j < size and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            j += 1
        # up operator
        elif(matrix[i][j-1] == 'R' and j > 0 and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            j -= 1
        # right operator
        elif(matrix[i + 1][j] == 'R' and i < size and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i += 1
        # left operator
        elif(matrix[i-1][j] == 'R' and i > 0 and (i,j) not in visited):
            pathToReturn.append(Node(matrix[i][j],i,j,pathToReturn[-1]))
            visited.add((i,j))
            i -= 1
        else:
            popedNode = pathToReturn.pop()
            print(popedNode.i, popedNode.j)


def main():
    with open('input.txt', 'r') as file:
        # read the first line and convert to integer
        algorithmNum = int(file.readline().strip())
        
        # read the second line and convert to integer
        size = int(file.readline().strip())
        
        # create an empty matrix
        matrix = []
        
        # read the rest of the lines and append each row as a list to the matrix
        for line in file:
            matrix.append(list(line.strip()))
    print(dfs(matrix,size))

main()






