from Node import Node
import networkx as nx

def discardNode(nodes, i, j):
    for node in nodes:
        if node.i == i and node.j == j:
            nodes.discard(node)
            break

def dfs(matrix, size, i=0, j=0, currentNode=Node('S',0,0,0), pathToReturn=set([Node('S',0,0,0)]), visited=set([(0,0)])):
    # down,right operator
    try:
        if( matrix[i+1][j+1]!='X' and matrix[i][j+1]!='X' and matrix[i+1][j]!='X' and i < size-1 and j < size-1 and (i+1,j+1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i+1 and node.j == j+1]
            if(not nextNode):
                nextNode = Node(matrix[i+1][j+1], i+1, j+1, currentNode.distance+1, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+1):
                discardNode(pathToReturn, i+1, j+1)
                nextNode.parent = currentNode
            visited.add((i+1,j+1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i+1,j+1,nextNode,pathToReturn,visited)
    except:
        {}
    # down,left operator
    try:
        if(matrix[i+1][j-1] != 'X' and matrix[i+1][j] != 'X' and matrix[i][j-1] != 'X' and i < size-1 and j > 0 and (i+1,j-1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i+1 and node.j == j-1]
            if(not nextNode):
                nextNode = Node(matrix[i+1][j+1], i+1, j-1, currentNode.distance+1, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+1):
                discardNode(pathToReturn, i+1, j-1)
                nextNode.parent = currentNode
            visited.add((i+1,j-1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i+1,j-1,nextNode,pathToReturn,visited)   
    except:
        {}
    # up,right operator
    try:
        if(matrix[i-1][j+1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j+1] != 'X' and i > 0 & j < size-1 and (i-1,j+1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i-1 and node.j == j+1]
            if(not nextNode):
                nextNode = Node(matrix[i-1][j+1], i-1, j+1, currentNode.distance+1, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+1):
                discardNode(pathToReturn, i-1, j+1)
                nextNode.parent = currentNode
            visited.add((i-1,j+1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i-1,j+1,nextNode,pathToReturn,visited)
    except:
        {}
    # left,up operator
    try:
        if(matrix[i-1][j-1] != 'X' and matrix[i-1][j] != 'X' and matrix[i][j-1] != 'X' and j > 0 & i > 0 and (i-1,j-1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i-1 and node.j == j-1]
            if(not nextNode):
                nextNode = Node(matrix[i-1][j-1], i-1, j-1, currentNode.distance+1, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+1):
                discardNode(pathToReturn, i-1, j-1)
                nextNode.parent = currentNode
            visited.add((i-1,j-1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i-1,j-1,nextNode,pathToReturn,visited)
    except:
        {}
    # right operato
    try:
        if(matrix[i][j+1] != 'X' and j < size-1 and (i,j+1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i and node.j == j+1]
            if(not nextNode):
                nextNode = Node(matrix[i][j+1], i, j+1, currentNode.distance +2, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+2):
                discardNode(pathToReturn, i, j+1)
                nextNode.parent = currentNode
            visited.add((i,j+1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i,j+1,nextNode,pathToReturn,visited)
    except:
        {}    
    # left operator
    try:
        if(matrix[i][j-1] != 'X' and j > 0 and (i,j-1) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i and node.j == j-1]
            if(not nextNode):
                nextNode = Node(matrix[i][j-1], i, j-1, currentNode.distance +2, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+2):
                discardNode(pathToReturn, i, j-1)
                nextNode.parent = currentNode
            visited.add((i,j-1))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i,j-1,nextNode,pathToReturn,visited)
    except:
        {}
    # down operator
    try:
        if(matrix[i+1][j] != 'X' and i < size-1 and (i+1,j) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i+1 and node.j == j]
            if(not nextNode):
                nextNode = Node(matrix[i+1][j], i+1, j, currentNode.distance +2, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+2):
                discardNode(pathToReturn, i+1, j)
                nextNode.parent = currentNode
            visited.add((i+1,j))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i+1,j,nextNode,pathToReturn,visited)
    except:
        {}
    # up operator
    try:
        if(matrix[i-1][j] != 'X' and i > 0 and (i-1,j) not in visited):
            nextNode = [node for node in pathToReturn if node.i == i-1 and node.j == j]
            if(not nextNode):
                nextNode = Node(matrix[i][j+1], i-1, j, currentNode.distance +2, currentNode)
            else:
                nextNode = nextNode[0]
            if(nextNode.distance > currentNode.distance+2):
                discardNode(pathToReturn, i-1, j)
                nextNode.parent = currentNode
            visited.add((i-1,j))
            pathToReturn.add(nextNode)
            dfs(matrix,size,i-1,j,nextNode,pathToReturn,visited)
    except:
        {}
    return pathToReturn, visited

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
    
    nodes, visited = dfs(matrix,size)
    goalNode = [node for node in nodes if node.cell == 'G']
    goalNode = goalNode[0]

    path = ''

    while(goalNode != None):
        path = ' => ' + '(' + str(goalNode.i) + ',' + str(goalNode.j) + ')' + path
        goalNode = goalNode.parent


    print(path)
    

main()






