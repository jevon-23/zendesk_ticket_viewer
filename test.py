import viewer

def test_list():
    req = viewer.getApi()
    if (req.status_code != 200):
        print('There was a problem with requesting the api.\n')
        return

    ticks = req.json()['tickets']
    print('-- p1 --\n')
    viewer.printTicks(0, ticks)
    print('-- p2 --\n')
    viewer.printTicks(1, ticks)
    print('-- p3 -- \n')
    viewer.printTicks(2, ticks)
    print('-- p4 -- \n')
    viewer.printTicks(3, ticks)
    print('-- p5 --\n')
    viewer.printTicks(4, ticks)



def test_ind():
    req = viewer.getApi()
    if (req.status_code != 200):
        print('There was a problem with requesting the api.\n')
        return

    ticks = req.json()['tickets']

    print('printing ticket 25 \n')
    viewer.printInd('25', ticks)
    print('===========\n')

    print('printing 105, should not work\n ')
    viewer.printInd('105', ticks)
    print('===========\n')

    print('printing 0, should return back very first\n')
    viewer.printInd('0', ticks)
    print('==========\n')

    print('printing 100, should not work.\n')
    viewer.printInd('100', ticks)

    print('subject officia sunt aliquip duis nisi, ticket 92')
    viewer.printInd('officia sunt aliquip duis nisi', ticks)
    print('===========\n')

    print('partial subj eiusmod tempor dolore, ticket 88')
    viewer.printInd('eiusmod tempor dolore', ticks)
    

print('Testing the printTicks()...\n')
test_list()
print('\n\nTesting printInd()...\n')
test_ind()
