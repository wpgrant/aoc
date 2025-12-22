import copy

def countSplits(lines, cols):
  splits = 0
  for line in lines[1:]:
    newCols = copy.deepcopy(cols)
    for col in cols:
      if line[col] == '^':
        splits += 1
        newCols.remove(col)
        if col-1 not in newCols:
          newCols.append(col-1)
        if col+1 not in newCols:
          newCols.append(col+1)
    cols = newCols
  return splits

if __name__ == '__main__':
  #with open('7tst.txt', 'r') as file:
  with open('7.txt', 'r') as file:
    lines = file.readlines()
    
  cols = []
  start = [i for i, char in enumerate(lines[0]) if char == 'S']
  if len(start) != 1:
    print("Invalid start position")
    exit(1)
  cols.append(start[0])
  splits = countSplits(lines, cols)
  print(splits)
    