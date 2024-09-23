def personal_for_loop(iterable):
    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))
        except StopIteration:
            break

personal_for_loop((1,2,3,4,5,6,7))
personal_for_loop(range(3,13))
personal_for_loop({1:'Shubham', 2:'Adarsh'})
personal_for_loop({1,2,3,4})
personal_for_loop([1,2,3,4,5])
# personal_for_loop(26)