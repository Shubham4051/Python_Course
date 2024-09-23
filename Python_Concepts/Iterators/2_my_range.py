class My_Range:
    def __init__(self, start, end, skip=1):
        self.start = start
        self.end = end
        self.skip = skip

    def __iter__(self):
        return Range_Iterator(self)


class Range_Iterator:
    def __init__(self, iterable_object):
        self.iterable = iterable_object

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end+1:
            # print(self.iterable.start)
            raise StopIteration
        current = self.iterable.start
        # print(self.iterable, self.iterable.start, self.iterable.end)
        self.iterable.start += self.iterable.skip
        return current
    
for i in My_Range(1,10,9):
    print(i)