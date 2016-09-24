import socket
import re

#setup socket to server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 8000))

#Figure out how much of each bill or coin to return, and subtract from total.
def changeExtractor(amount, value):
    change = int(round(amount,2) / value)
    if change:
        amount = amount - (change * value)
    return amount, change

#Processes all of the change.
def processAmount(amount):
    amount, tenthousanddollars = changeExtractor(amount, 10000.0)
    amount, fivethousanddollars = changeExtractor(amount, 5000.0)
    amount, onethousanddollars = changeExtractor(amount, 1000.0)
    amount, fivehundreddollars = changeExtractor(amount, 500.0)
    amount, onehundreddollars = changeExtractor(amount, 100.0)
    amount, fiftydollars = changeExtractor(amount, 50.0)
    amount, twentydollars = changeExtractor(amount, 20.0)
    amount, tendollars = changeExtractor(amount, 10.0)
    amount, fivedollars = changeExtractor(amount, 5.0)
    amount, onedollar = changeExtractor(amount, 1.0)
    amount, halfdollars = changeExtractor(amount, .50)
    amount, quarters = changeExtractor(amount, .25)
    amount, dimes = changeExtractor(amount, .10)
    amount, nickels = changeExtractor(amount, .05) 
    amount, pennies = changeExtractor(amount, .01)

    return amount, tenthousanddollars, fivethousanddollars, onethousanddollars, fivehundreddollars, onehundreddollars, fiftydollars, twentydollars, tendollars, fivedollars, onedollar, halfdollars, quarters, dimes, nickels, pennies

#Responds to the server's request for each money type.
def sendChange(currency):
    s.send(str(currency) + "\n")
    print(str(currency) + " Sent")

#Loops over the sends and recvs.
#Responds to the server with the change needed.
#initiates the function call to process each amount.
while 1:
    data = s.recv(1024)

    if data == "":
        break
    
    if (re.search("flag", data)):
        break

    #Matches on the very first run, before we've solved anything. Initiated the first processAmount() call.
    if ((re.search("10,000 bills: $", data)) and not (re.search("^correct", data))):
        splitdata = data.split('\n')
        amount = float(splitdata[0].strip("$"))
        #print amount
        data = splitdata[1]
        #print "Received: ", repr(splitdata[1])
        amount, tenthousanddollars, fivethousanddollars, onethousanddollars, fivehundreddollars, onehundreddollars, fiftydollars, twentydollars, tendollars, fivedollars, onedollar, halfdollars, quarters, dimes, nickels, pennies = processAmount(amount)

    #Matches when we have a correct pass. Initites the next processAmount() call.
    if (re.search("^correct", data)):
        print repr(data)
        splitdata = data.split('\n')
        data = splitdata[2]
        amount = float(splitdata[1].strip('$'))
        amount, tenthousanddollars, fivethousanddollars, onethousanddollars, fivehundreddollars, onehundreddollars, fiftydollars, twentydollars, tendollars, fivedollars, onedollar, halfdollars, quarters, dimes, nickels, pennies = processAmount(amount)
    
    print "Received:", repr(data)

    if ("$10,000 bills: " == data):
        sendChange(tenthousanddollars)
        continue
    if ("$5,000 bills: " == data):
        sendChange(fivethousanddollars)
        continue
    if ("$1,000 bills: " == data):
        sendChange(onethousanddollars)
        continue
    if ("$500 bills: " == data):
        sendChange(fivehundreddollars)
        continue
    if ("$100 bills: " == data):
        sendChange(onehundreddollars)
        continue
    if ("$50 bills: " == data):
        sendChange(fiftydollars)
        continue
    if ("$20 bills: " == data):
        sendChange(twentydollars)
        continue
    if ("$10 bills: " == data):
        sendChange(tendollars)
        continue
    if ("$5 bills: " == data):
        sendChange(fivedollars)
        continue
    if ("$1 bills: " == data):
        sendChange(onedollar)
        continue
    if ("half-dollars (50c): " == data):
        sendChange(halfdollars)
        continue
    if ("quarters (25c): " == data):
        sendChange(quarters)
        continue
    if ("dimes (10c): " == data):
        sendChange(dimes)
        continue
    if ("nickels (5c): " == data):
        sendChange(nickels)
        continue
    if ("pennies (1c): " == data):
        sendChange(pennies)
        continue

print repr(data)
print "Connection closed."
s.shutdown(socket.SHUT_WR)
s.close()
