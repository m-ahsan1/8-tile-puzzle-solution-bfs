


########################################################

class PuzzleState:
  def __init__(self,numbers):
  #print "initialize the data"
    #print(numbers)
    self.cells=[]
    self.blankLocation=0,0
    #[0,1,2,3,4,5,6,7,8]
    k=0
    for i in range(3):
      row=[]
      for j in range(3):
        row.append(numbers[k])
        if numbers[k]==0:
          self.blankLocation=i,j
        k +=1
        #print(row)
      self.cells.append(row)


  def printState(self):
  #print "print the current state"
    lines=[]
    horizontalline=("_" * (13))
    print(horizontalline)
    for row in self.cells:
      rowline ="|"
      for col in row:
        if col ==0:
          col= "."
        rowline=rowline +" " + col.__str__() + "|"
      print (rowline)
      print (horizontalline)

  def isGoal(self):
  #print "check is the state is goal or not"
    current=0
    for i in range(3):
      for j in range(3):
        if current !=self.cells[i][j]:
          return False
        current +=1

    return True
  def legalMoves(self):
  #print "return all the legal moves"
    row,col=self.blankLocation
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
  #print "return the next state based on the move"
    row,col = self.blankLocation
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


    newPuzzle = PuzzleState([0,0,0,0,0,0,0,0,0])
    newPuzzle.cells=[value[:] for value in self.cells]
    #print newPuzzle.cells
    newPuzzle.cells[row][col]=self.cells[newrow][newcol]
    newPuzzle.cells[newrow][newcol]=self.cells[row][col]
    newPuzzle.blankLocation=(newrow,newcol)
    return newPuzzle
  def __eq__(self, other):
    for row in range( 3 ):
      if self.cells[row] != other.cells[row]:
        return False
    return True

class SearchProblem:
  def __init__(self,state):
  #print "initialize the search problem"
    self.puzzle=state
  def getStartState(self):
  #print "return the start state"
      return self.puzzle
  def getSuccessors(self,state):
  #print "return all the child states"
    succs=[]

    for move in state.legalMoves():
      cState= state.resultState(move)
      succs.append((cState,move))
    return succs
  def isGoalState(self,state):
  #print "return information that state is goal state or not"
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
  #print counter
    current =queue.pop()
    #print current
    cStatewithAction = current[0]
    cPath = current[1]
    cState = cStatewithAction[0]

    cAction = cStatewithAction[1]
    if cState in visitedStates:
      continue
    else:
      visitedStates.append(cState)

    counter +=1
  #print type(cState)
    if problem.isGoalState(cState):
  #print "Goal found"
  #print cPath
      return cPath
    else:
      succs=problem.getSuccessors(cState)
    for succ in succs:
      sPath=copy.deepcopy(cPath)
      if succ[0] in visitedStates:
  #print "already present"
        continue
      else:
        sPath.append(succ[1])
        queue.push((succ,sPath))





puzzle = PuzzleState([5,1,2,3,0,4,6,7,8])
p = SearchProblem(puzzle)
path = BFS(p)
print (path)
for p in path:
  puzzle=puzzle.resultState(p)
  puzzle.printState()
  input("Press Enter")
