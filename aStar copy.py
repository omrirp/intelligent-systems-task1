from Node import Node

def manhattanDistance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)

def moveNode(open, closed, i, j):
    for node in open:
        if node.i == i and node.j == j:
            open.remove(node)
            closed.append(node)
            break

def discardNode(nodes, i, j):
    for node in nodes:
        if node.i == i and node.j == j:
            nodes.discard(node)
            break

def aStarMove(matrix, size, open, closed, currentNode, visited, i, j, distanceToAdd):
    nextNode = [node for node in closed if node.i == i and node.j == j]
    if(not nextNode):
        nextNode = Node(matrix[i][j], i, j, currentNode.distance+distanceToAdd, currentNode)
    else:
        nextNode = nextNode[0]
    if(nextNode.distance + manhattanDistance(nextNode.i,nextNode.j,size-1,size-1) > currentNode.distance+1+manhattanDistance(currentNode.i,currentNode.j,size-1,size-1)):
        discardNode(open, i, j)
        nextNode.parent = currentNode
    open.append(nextNode)
    visited.add((i,j))
    return

def aStar(matrix, size):
    open = list([Node('S',0,0,0)])
    closed = list()
    visited = set([(0,0)])
    
    while(len(open) != 0):
        
        # find the Node with the minimum value of total distance from the start
        # pluse the  heuristic value as manhattan distance
        currentNode = None
        closestDistance = float('inf')
        for node in open:
            manDistance = manhattanDistance(node.i, node.j, size-1, size-1)
            distance =  manDistance + node.distance
            if distance < closestDistance:
                currentNode = node
                closestDistance = distance
        i = currentNode.i
        j = currentNode.j

        # down,right operator
        try:
            if( matrix[i+1][j+1]!='X' and matrix[i][j+1]!='X' and matrix[i+1][j]!='X' and i < size-1 and j < size-1 and (i+1,j+1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i+1,j+1,1)
        except:
            {}
         # down,left operator
        try:
            if(matrix[i+1][j-1] != 'X' and matrix[i+1][j] != 'X' and matrix[i][j-1] != 'X' and i < size-1 and j > 0 and (i+1,j-1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i+1,j-1,1)
        except:
            {}
        # up,right operator
        try:
            if(matrix[i-1][j+1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j+1] != 'X' and i > 0 & j < size-1 and (i-1,j+1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i-1,j+1,1)
        except:
            {}
         # left,up operator
        try:
            if(matrix[i-1][j-1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j-1] != 'X' and j > 0 & i > 0 and (i-1,j-1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i-1,j-1,1)
        except:
            {}
        # right operator
        try:
            if(matrix[i][j+1] != 'X' and j < size-1 and (i,j+1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i,j+1,2)
        except:
            {}    
        # left operator
        try:
            if(matrix[i][j-1] != 'X' and j > 0 and (i,j-1) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i,j-1,2)
        except:
            {}
        # down operator
        try:
            if(matrix[i+1][j] != 'X' and i < size-1 and (i+1,j) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i+1,j,2)
        except:
            {}
        # up operator
        try:
            if(matrix[i-1][j] != 'X' and i > 0 and (i-1,j) not in visited):
                aStarMove(matrix,size,open,closed,currentNode,visited,i-1,j,2)
        except:
            {}
        # move the current node from open to closed
        moveNode(open, closed, i, j)
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
        
        aStar(matrix,size)

main()
