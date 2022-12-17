import re

dirs = {}

def addFile(dir, size):
  if dir in dirs:
    dirs[dir] = dirs[dir] + amt 
  else:
    dirs[dir] = amt

  # Need to add to parent directory as well
  if(dir != '/'):
    parentDir = re.match('(.*)\/.*\/', dir).group(1) + '/'
    addFile(parentDir, size)


if __name__ == '__main__':
  # For this problem this could be optimized to stop counting
  # for directories larger than 100000, but the input was small
  # enough that this wasn't necessary.
  currentDir = "/"
  with open('7.txt', 'r') as file:
    lines = file.readlines()
  
    for line in lines:
      # Process each line
      # $ cd   : Set the current directory
      # Number : Add to the current directory
      # dir    : Ignore
      # ls     : Ignore
      theLine = line.strip()
      if (theLine.startswith('$ cd /')):
        currentDir = "/"
      elif (theLine.startswith('$ cd ..')):
        currentDir = re.match('(.*)\/.*\/', currentDir).group(1) + '/'
      elif (theLine.startswith('$ cd')):
        currentDir += re.match('\$ cd (.*)', theLine).group(1) + '/'
      elif ( re.match('^\d+', theLine) ):
        amt = int(re.match('^(\d+).*', theLine).group(1))
        addFile(currentDir, amt)

  usedSize = dirs['/']
  unusedSize = 70000000 - usedSize
  remainingSize = 30000000 - unusedSize
  lstDirsSorted = sorted(dirs.items(), key=lambda item: item[1])
  for dir, size in lstDirsSorted:
    if size >= remainingSize:
      print(f'{dir} - {size}')
      quit()
