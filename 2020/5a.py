def getRow(ticket):
  convTicket = ticket.replace('F', '0').replace('B', '1')
  return int(convTicket, 2)

def getSeat(ticket):
  convTicket = ticket.replace('L', '0').replace('R', '1')
  return int(convTicket, 2)

def processTicket(ticket):
  row = getRow(ticket[:7])
  seat = getSeat(ticket[7:])
  return (row * 8) + seat

if __name__ == '__main__':
  with open('5.txt', 'r') as file:
    lines = file.readlines()
    
    highestTicketNum = 0
    for line in lines:
      ticketNum = processTicket(line)
      if ticketNum >= highestTicketNum:
        highestTicketNum = ticketNum

    print(f'highestTicketNum = {highestTicketNum}')