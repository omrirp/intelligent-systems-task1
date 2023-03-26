from Node import Node

def manhattanDistance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)

def moveNode(open, closed, i, j):
    for node in open:
        if node.i == i and node.j == j:
            open.remove(node)
            closed.append(node)
            break

def gbfs(matrix, size):
    open = list([Node('S',0,0,0)])
    closed = list()
    visited = set([(0,0)])
    i = 0
    j = 0
    goalCordinates = (size-1,size-1)
    
    while(len(open) != 0):
        
        # find the Node with the closest manhattan distance to the goal
        currentNode = None
        closestDistance = float('inf')
        for node in open:
            distance = manhattanDistance(node.i, node.j, goalCordinates[0], goalCordinates[1])
            if distance < closestDistance:
                currentNode = node
                closestDistance = distance

        # down,right operator
        try:
            if( matrix[i+1][j+1]!='X' and matrix[i][j+1]!='X' and matrix[i+1][j]!='X' and i < size-1 and j < size-1 and (i+1,j+1) not in visited):
                open.append(Node(matrix[i+1][j+1], i+1, j+1, currentNode.distance+1, currentNode))
                visited.add((i+1,j+1))
        except:
            {}
         # down,left operator
        try:
            if(matrix[i+1][j-1] != 'X' and matrix[i+1][j] != 'X' and matrix[i][j-1] != 'X' and i < size-1 and j > 0 and (i+1,j-1) not in visited):
                open.append(Node(matrix[i+1][j-1], i+1, j-1, currentNode.distance+1, currentNode))
                visited.add((i+1,j-1))
        except:
            {}
        # up,right operator
        try:
            if(matrix[i-1][j+1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j+1] != 'X' and i > 0 & j < size-1 and (i-1,j+1) not in visited):
                open.append(Node(matrix[i-1][j+1], i-1, j+1, currentNode.distance+1, currentNode))
                visited.add((i-1,j-1))
        except:
            {}
         # left,up operator
        try:
            if(matrix[i-1][j-1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j-1] != 'X' and j > 0 & i > 0 and (i-1,j-1) not in visited):
                open.append(Node(matrix[i-1][j-1], i-1, j-1, currentNode.distance+1, currentNode))
                visited.add((i-1,j-1))
        except:
            {}
        # right operato
        try:
            if(matrix[i][j+1] != 'X' and j < size-1 and (i,j+1) not in visited):
                open.append(Node(matrix[i][j+1], i, j+1, currentNode.distance+2, currentNode))
                visited.add((i,j+1))
        except:
            {}    
        # left operator
        try:
            if(matrix[i][j-1] != 'X' and j > 0 and (i,j-1) not in visited):
                open.append(Node(matrix[i][j-1], i, j-1, currentNode.distance+2, currentNode))
                visited.add((i,j-1))
        except:
            {}
        # down operator
        try:
            if(matrix[i+1][j] != 'X' and i < size-1 and (i+1,j) not in visited):
                open.append(Node(matrix[i+1][j], i+1, j, currentNode.distance+2, currentNode))
                visited.add((i+1,j))
        except:
            {}
        # up operator
        try:
            if(matrix[i-1][j] != 'X' and i > 0 and (i-1,j) not in visited):
                open.append(Node(matrix[i-1][j], i-1, j, currentNode.distance+2, currentNode))
                visited.add((i-1,j))
        except:
            {}
        # move the current node from open to closed
        moveNode(open, closed, i, j)
        i = currentNode.i
        j = currentNode.j
    # end of while loop
    return closed, visited 

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
        
        gbfs(matrix,size)

main()
