

class Puzzle:
  def __init__(self,startPuzzle):
    #Initializing the grid
    self.cells=[]
    self.blankTile=0,0


    k=0
    for i in range(3):
      row=[]
      for j in range(3):
        row.append(startPuzzle[k])
        #setting the blank tile index
        if startPuzzle[k]==0:
          self.blankTile=i,j
        k +=1

      self.cells.append(row)

  def isGoal(self):

    #check if the state is goal state

    curr1=0
    for i in range(3):
      for j in range(3):
        if curr1 !=self.cells[i][j]:
          return False
        curr1 +=1

    return True


  def legalMoves(self):

    row,col=self.blankTile
    legalMoves=[]
    if row!=0:
      legalMoves.append("up")
    if row!=2:
      legalMoves.append("down")
    if col !=0:
      legalMoves.append("left")
    if col !=2:
      legalMoves.append("right")
    return legalMoves


  def resultState(self,move):
    row,col = self.blankTile
    if move=="up":
      newrow=row-1
      newcol=col
    elif move== "down":
      newrow=row+1
      newcol=col
    elif move=="left":
      newrow=row
      newcol=col -1
    elif move =="right":
      newrow=row
      newcol=col+1
    else:
      raise "illegal move"


    newPuzzle = Puzzle([0,0,0,0,0,0,0,0,0])
    newPuzzle.cells=[value[:] for value in self.cells]

    newPuzzle.cells[row][col]=self.cells[newrow][newcol]
    newPuzzle.cells[newrow][newcol]=self.cells[row][col]
    newPuzzle.blankTile=(newrow,newcol)
    return newPuzzle
  def __eq__(self, other):
    for row in range( 3 ):
      if self.cells[row] != other.cells[row]:
        return False
    return True

  def printState(self):

    lines=[]
    for row in self.cells:
      eachRow =""
      for col in row:
        eachRow = eachRow +" " + col.__str__()
      print (eachRow)


class SearchProblem:
  def __init__(self,state):

    self.puzzle=state
  def getStartState(self):

      return self.puzzle
  def getSuccessors(self,state):

    succs=[]

    for move in state.legalMoves():
      cState= state.resultState(move)
      succs.append((cState,move))
    return succs
  def isGoalState(self,state):

    return state.isGoal()

class Queue:
  def __init__(self):
    self.list=[]
  def push(self,item):
    self.list.insert(0,item)
  def pop(self):
    return self.list.pop()
  def isEmpty(self):
    return len(self.list)==0



import copy


def BFS(problem):
  state= problem.getStartState()
  queue= Queue()
  action= ""
  fPath= []
  visitedStates=[]
  queue.push(((state,action),fPath))
  counter=0
  while queue.isEmpty()==False:

    current =queue.pop()

    cStatewithAction = current[0]
    cPath = current[1]
    cState = cStatewithAction[0]

    cAction = cStatewithAction[1]
    if cState in visitedStates:
      continue
    else:
      visitedStates.append(cState)

    counter +=1
    if problem.isGoalState(cState):

      return cPath
    else:
      succs=problem.getSuccessors(cState)
    for succ in succs:
      sPath=copy.deepcopy(cPath)
      if succ[0] in visitedStates:

        continue
      else:
        sPath.append(succ[1])
        queue.push((succ,sPath))




class Stack:
  def __init__(self):
    self.list = []
  def push(self, item):
    self.list.append(item)
  def pop(self):
    return self.list.pop()
  def isEmpty(self):
    return len(self.list) == 0

def DFS(problem):
  state = problem.getStartState()
  stack = Stack()
  action = ""
  fPath = []
  visitedStates = []
  stack.push(((state, action), fPath))
  counter = 0
  while not stack.isEmpty():
    current = stack.pop()
    cStatewithAction = current[0]
    cPath = current[1]
    cState = cStatewithAction[0]
    cAction = cStatewithAction[1]
    if cState in visitedStates:
      continue
    else:
      visitedStates.append(cState)
    counter += 1
    if problem.isGoalState(cState):
      return cPath
    else:
      succs = problem.getSuccessors(cState)
      for succ in reversed(succs):
        sPath = cPath + [succ[1]]
        if succ[0] in visitedStates:
          continue
        else:
          stack.push((succ, sPath))




class IDS:
  def __init__(self, problem):
    self.problem = problem
    self.depth_limit = 0

  def search(self):
    while True:
      result = self.depth_limited_search(self.problem.getStartState(), self.depth_limit)
      if result is not None:
        return result
      self.depth_limit += 1

  def depth_limited_search(self, state, depth_limit):
    return self.recursive_dls(state, depth_limit, [])

  def recursive_dls(self, state, depth_limit, path):
    if self.problem.isGoalState(state):
      return path
    elif depth_limit == 0:
      return None
    else:
      for succ in self.problem.getSuccessors(state):
        sState, sAction = succ
        if sState not in path:

          result = self.recursive_dls(sState, depth_limit-1, path + [state])
          if result is not None:
            return [sAction] + result
      return None

startingState = [7,2,4,5,0,6,8,2,1]
finalState = [0,1,2,3,4,5,6,7,8]

def printInitial(startPuzzle):
  print("Starting State : ")
  k=0
  row = ""
  for i in range(9):
    row = row + " " + startPuzzle[i].__str__()
    k+=1
    if(k==3):
      k = 0
      print(row)
      row = ""

def printFinal(finalPuzzle):
  print("Goal State : ")
  k=0
  row = ""
  for i in range(9):
    row = row + " " + finalPuzzle[i].__str__()
    k+=1
    if(k==3):
      k = 0
      print(row)
      row = ""



def menu(inp):
  if(inp == '1'):
    print("Starting BFS....")


  elif(inp == '2'):
    print("Starting DFS....")
    puzzle = Puzzle(startingState)
    p = SearchProblem(puzzle)
    path = DFS(p)
    print (path)
    for p in path:
      puzzle=puzzle.resultState(p)
      puzzle.printState()
      input("Next State")
  elif(inp == '3'):
    print("Starting IDS....")
    puzzle = Puzzle(startingState)
    p = SearchProblem(puzzle)
    ids = IDS(p)
    path = ids.search()
    print(path)
    for p in path:
      puzzle = puzzle.resultState(p)
      puzzle.printState()
      input("Next state")




printInitial(startingState)
print()
printFinal(finalState)


# print("Press 1 to implement BFS : ")
# print("Press 2 to implement DFS : ")
# print("Press 3 to implement IDS : ")
# inp = input(">")



# puzzle = Puzzle([7,2,4,5,0,6,8,2,1])
# p = SearchProblem(puzzle)
# ids = IDS(p)
# path = ids.search()
# print(path)
# for p in path:
#   puzzle = puzzle.resultState(p)
#   puzzle.printState()
#   input("Press Enter")



puzzle = Puzzle(startingState)
p = SearchProblem(puzzle)
path = BFS(p)
print (path)
for p in path:
  puzzle=puzzle.resultState(p)
  puzzle.printState()
  input("Next State")

