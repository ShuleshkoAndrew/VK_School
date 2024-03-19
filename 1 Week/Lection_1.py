import ctypes


class DynamicArray(object):
    def __init__(self):
        self.size = 0
        self.capacity = 0
        self.array = self.make_array(self.capacity)

    def cap(self):
        return self.capacity

    def append(self, element):
        if self.size == self.capacity:
            self.resize_append()
            print(f'slow:{self.cap()}')
        else:
            print("fast")
        self.array[self.size] = element
        self.size += 1

    def resize_append(self):
        new_cap = self.capacity * 2
        new_array = self.make_array(new_cap)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_cap

    def delete(self):
        if self.size == self.capacity / 4:
            self.resize_delete()
            print('fast')
        else:
            print('fast')
        self.size -= 1


    def resize_delete(self):
        new_cap = self.capacity / 2

