def testgen(index):
    weekdays=['sun','mon','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]
    day=testgen(0)
    print (next(day),next(day))
