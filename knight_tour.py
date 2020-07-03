import time
from queueing import myQueue

def existsOnBoard(square,boardSize):#test if a certain (i,j) position does exist on the board or not
  (i,j)=square
  return ((i<=boardSize) and (j<=boardSize) and (i>0) and (j>0))

def getNeighbors(position,boardSize,memo):#return a list of squares to where the knight can go
  x,y=(position)
  key = str(x)+str(y)
  if key in memo :
    neighbors = memo[key]
  else:
    neighbors=[]
    (i,j)=position
    neighborSquares=[(i+2,j+1),(i+2,j-1),(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2),(i-2,j+1),(i-2,j-1)]
    for square in neighborSquares:
      if existsOnBoard(square,boardSize):
        neighbors.append(square)
      memo[key] = neighbors  
  return neighbors

def allNeighborsAreVisited(visited,neighbors):#check if all neighboring squares have been visited
  for neighbor in neighbors:
    if neighbor not in visited:
      return False
  return True

def update(visited,visitedPaths,queue,currentPath):
  for element, elementPath in zip(visited,visitedPaths):
    lengthOfElementPath=len(elementPath)
    lengthOfCurrentPath=len(currentPath)
    if ((element not in currentPath) and (lengthOfCurrentPath<=lengthOfElementPath)):
      visited.remove(element)


def dfs(boardSize,initialPosition):
  start_time=time.time()#set the start time
  initialState=initialPosition
  visited=[]    # Start with an empty list of visited states
  visitedPaths=[]
  path=[]
  queue=myQueue()
  queue.enqueue((initialState,[initialState])) # Put the initial state in the queue
  memo = {}
  while(not queue.isEmpty()): # Keep looping dequeueing til the queue is empty
      (state,path)=queue.dequeue() # Remove the last element from the queue
      if (len(path)==pow(boardSize,2)):
        execution_time=time.time()-start_time 
        return (path,execution_time)
      else:  #if state not in visited:  # Checks if the state has already been visited 
        visited.append(state) # Add the state to the list of visited states
        visitedPaths.append(path)
        neighbors=getNeighbors(state,boardSize,memo)
        neighbors.sort(key=lambda neighbor: getNeighbors(neighbor,boardSize,memo), reverse=True)
        if ((len(neighbors)>0) and (not allNeighborsAreVisited(visited,neighbors))):
          for neighbor in neighbors: #checks all neighoring states
              if neighbor not in visited: #If neighbor is not visited
                queue.enqueue((neighbor,path+[neighbor])) #add node to the stack
      update(visited,visitedPaths,queue,path)        
  print ("No path covering all cells found from this initial position!")        
  execution_time=time.time()-start_time 
  return ([],execution_time)

if __name__ == "__main__":
  boardSize=int(input("Enter the size of the board (bigger than 4): "))
  print("------------------------\nEnter the initial position")
  x=input("Enter the row number: ")
  y=input("Enter the column number: ")
  initialPosition=(x,y)
  knightTour,execution_time=dfs(boardSize,initialPosition)
  print(knightTour)
  print(len(knightTour))
  print(execution_time)




