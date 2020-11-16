import time, sys, re, requests

"""Attempts to fetch personal api """
def getApi():
    url = 'https://jevon.zendesk.com/api/v2/tickets.json'
    usr = 'jevonjackson@berkeley.edu/token'
    token = 'xCddswYzUlwvYIbAcyjgYtNRBpNnTQ2Cv2XELgQR'
    req = requests.get(url, auth=(usr, token))
    return req

""" Helper function for printInd. Prints the details of the ticket. CURRTICK is the ticket that we are printing out."""
def printDet(currTick):
    print('requester_id :', currTick['requester_id'])
    print('assignee-id :', currTick['assignee_id'])
    print('subject :', currTick['subject'])
    print('description :', currTick['description'])
    print('tags : ', currTick['tags'], '\n')

"""Prints all of the tickets that have either contain the string SUBJECT or at the index SUBJECT.
    SUBJECT will either be a string or an integer. """
def printInd(subject, ticks):
    bool = False

    #checking to see if they passed in a number instead of a subject
    isDigit = re.compile('\d+')
    if (isDigit.match(subject) != None):
        if (int(subject) >= len(ticks) or int(subject) < 0):
            print('Index is out of range, please give an index that is 0 -', len(ticks) - 1, '\n')
        else:
            print('\n--- ticket', subject, '---')
            printDet(ticks[int(subject)])

        return

    #If it is not a digit, then we will iterate through the tickets to look for the ones w SUBJECT
    for i in range(len(ticks)):
        currTick = ticks[i]
        if (subject in currTick['subject']):
            print('\n--- ticket', i, '---')
            printDet(ticks[i])
            bool = True

    if (not bool):
        print('There are no tickets that conatain that subject.\n')

""" Prints the tickets in the order that they came in. TICKETS is the list of tickets that we have.
PAGE is what page we are printing. Returns the next page number. If we are at the last page, returns 0"""
def printTicks(page, ticks):

    #the index of the ticket that will begin the new page
    index = page * 25

    if (index >= len(ticks)):
        return printTicks(0, ticks)
    print('page', page+1, ',', 'tickets', index, '-', index + 25)

    #Getting the json tickets list
    for val in range(25):
        #If we are at the last ticket
        if (index + val >= len(ticks)):
            return 0

        #The current ticket
        currTick = ticks[index + val]

        #Printing out the values of the current ticket
        print('\n--- ticket', index + val, '---')
        print('requester_id :', currTick['requester_id'])
        print('assignee-id :', currTick['assignee_id'])
        print('subject :', currTick['subject'], '\n')

    return page + 1

"""Main function. Gets api, and then awaits input from user."""
def main():
    #Accessing api
    req = getApi()
    if (req.status_code != 200):
        print('There was a problem with requesting the api.\n')
        return

    ticks = req.json()['tickets']

    #Starting page
    page = 0

    print('Enter \'help\' to view options, enter \'exit\' to exit program\n')

    while True:
        next = input()

        #print first page
        if (next == 'list'):
            page = printTicks(0, ticks)
            print('To go to the next page, enter \"next\". To go back, enter \"back\"')

        #If user wants the next page
        elif (next == 'next'):
            page = printTicks(page, ticks)
            print('To go to the next page, enter \"next\". To go back, enter \"back\"')

        #If user wants to go back a page, if you try to go back after visiting the first page or not visiting a page, outputs first page
        elif (next == 'back'):
            if (page > 1):
                page = printTicks(page-2, ticks)
            else:
                page = printTicks(0, ticks)
            print('To go to the next page, enter \"next\". To go back, enter \"back\"')

        #searching for a subject / ticket number
        elif ('search' in next):
            val = next.split('search ')
            printInd(val[1], ticks)

        #exit the program
        elif (next == 'exit'):
            return
        elif (next == 'help'):
            print('\nTo get a list of all the tickets, enter \"list\".\nTo get an individual ticket, enter \"search {subject}\" or \"search {ticket number}. \nTo exit program, enter \"exit\"\n')
        else:
            print('Invalid input. \n')
#When argv > 1, we are running a test
if (__name__ == "__main__"):
    main()
