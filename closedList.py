class ClosedList(list):
    def __init(self, sequence, bypassOrder='direct'):
        list.__init__(sequence)
        self.order = bypassOrder

    def __getslice__(self, i, j):
        if i == j:
            return ClosedList([self[i]])
        elif i < j:
            return ClosedList(list.__getitem__(self, slice(i, j + 1)))
        elif i > j:
            return self[i:len(self) - 1] + self[0:j]

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__getslice__(item.start, item.stop)

        else:
            return list.__getitem__(self, item)


class IncorrectIndexError(Exception): pass


if __name__ == '__main__':
    lst = ClosedList([1, 2, 3, 4])
    print(lst[2:1])
