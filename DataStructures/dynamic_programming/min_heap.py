# make an min-heap algorithm


class MinHeap(object):

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    @staticmethod
    def swap(x, y):
        tmp = y
        y = x
        x = tmp
        return x , y

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, i):

        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.swap(self.heap_list[i], self.heap_list[i // 2])
            i//=2


    def min_child(self, i):
        if 2 *i + 1 > self.current_size:
            return 2 * i 
        else:


    def perc_down(self, i):
        while 2 * i <= self.current_size:


m = MinHeap()

m.insert(10)
m.insert(1)
m.insert(20)
m.insert(300)
m.insert(19)
m.insert(5)

print m.heap_list
