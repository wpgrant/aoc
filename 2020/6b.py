from queue import Empty


def processGroup(groupLines):
  groupList = []
  # Initialize with first line
  for char in groupLines[0]:
    if char != '\n':
      groupList.append(char)
  # Iterate over the rest, and remove any chars that don't remain
  for line in groupLines[1:]:
    groupList = [char for char in groupList if line.find(char) >= 0]
  return len(set(groupList))

if __name__ == '__main__':
  with open('6.txt', 'r') as file:
    lines = file.readlines()
    groupLines = []
    countAllGroups = 0
    for line in lines:
      if len(line.strip()) == 0:
        countAllGroups += processGroup(groupLines)
        groupLines = []
      else:
        groupLines.append(line)
    # Process last group
    countAllGroups += processGroup(groupLines)
    print(f'Count is {countAllGroups}')