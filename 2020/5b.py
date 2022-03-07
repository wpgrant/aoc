def getRow(ticket):
  convTicket = ticket.replace('F', '0').replace('B', '1')
  return int(convTicket, 2)

def getSeat(ticket):
  convTicket = ticket.replace('L', '0').replace('R', '1')
  return int(convTicket, 2)

def processTicket(ticket):
  row = getRow(ticket[:7])
  seat = getSeat(ticket[7:])
  ticketNum = (row * 8) + seat
  return ticketNum

def findGaps(sortedList):
  prevNumber = sortedList[0]
  for currNumber in sortedList:
    if currNumber - prevNumber > 1:
      yourTicket = currNumber - 1
      print(f'{prevNumber} & {currNumber} exists, yours must be {yourTicket}.')
    prevNumber = currNumber

if __name__ == '__main__':
  with open('5.txt', 'r') as file:
    lines = file.readlines()
    
    fullList = []
    for line in lines:
      fullList.append(processTicket(line))

    sortedList = sorted(fullList)
    findGaps(sortedList)
