import math

class PriorityQueueWithMaxHeap:
    def __init__(self):
        self.__list = [-10000]
        self.__count = len(self.__list) - 1

    def swap(self, i, j):
        tmp = self.__list[i]
        self.__list[i] = self.__list[j]
        self.__list[j] = tmp

    def __heapifyBasedOnPriority(self, str):
        if str == "Append":  # append후 heapify
            count = self.__count
            while count > 1:
                idx = math.trunc(count / 2.0)  # math.trunc 소수점 버림
                if self.__list[count] > self.__list[idx]:
                    self.swap(count, idx)
                    count = idx
                else:
                    break
        elif str == "Pop":
            count = 1
            while self.__count >= count * 2:
                idx, j = count * 2, (count * 2) + 1  # index error
                try:
                    if self.__list[idx] > self.__list[j]:
                        if self.__list[idx] > self.__list[count]:
                            self.swap(idx, count)
                        else:
                            break
                    else:
                        if self.__list[j] > self.__list[count]:
                            self.swap(j, count)
                        else:
                            break
                except IndexError as e:
                    if self.__list[idx] > self.__list[count]:
                        self.swap(idx, count)
                    else:
                        break
                count *= 2

    def append(self, num):
        self.__list.append(num)
        self.__count += 1
        self.__heapifyBasedOnPriority("Append")
        return self.__repr__()


    def pop(self):
        tmpPop = self.check(1)
        self.swap(1, -1)
        self.__list.pop(-1)
        self.__count -= 1
        self.__heapifyBasedOnPriority("Pop")
        return tmpPop

    def check(self, idx):
        try:
            return self.__list[idx]
        except IndexError as e:
            pass

    def __repr__(self):
        return str(self.__list[1:])


class PriorityQueueWithMinHeap:
    def __init__(self):
        self.__list = [-10000]
        self.__count = len(self.__list) - 1

    def swap(self, i, j):
        tmp = self.__list[i]
        self.__list[i] = self.__list[j]
        self.__list[j] = tmp

    def __heapifyBasedOnPriority(self, str):
        if str == "Append":  # append후 heapify
            count = self.__count
            while count > 1:
                idx = math.trunc(count / 2.0)  # math.trunc 소수점 버림
                if self.__list[count] < self.__list[idx]:
                    self.swap(count, idx)
                    count = idx
                else:
                    break
        elif str == "Pop":
            count = 1
            while self.__count >= count * 2:
                idx, j = count * 2, (count * 2) + 1  # index error
                try:
                    if self.__list[idx] < self.__list[j]:
                        if self.__list[idx] < self.__list[count]:
                            self.swap(idx, count)
                        else:
                            break
                    else:
                        if self.__list[j] < self.__list[count]:
                            self.swap(j, count)
                        else:
                            break
                except IndexError as e:
                    if self.__list[idx] < self.__list[count]:
                        self.swap(idx, count)
                    else:
                        break
                count *= 2

    def append(self, num):
        self.__list.append(num)
        self.__count += 1
        self.__heapifyBasedOnPriority("Append")
        return self.__repr__()

    def pop(self):
        tmpPop = self.check(1)
        self.swap(1,-1)
        self.__list.pop(-1)
        self.__count -= 1
        self.__heapifyBasedOnPriority("Pop")
        return tmpPop

    def check(self, idx):
        try:
            return self.__list[idx]
        except IndexError as e:
            pass

    def __repr__(self):
        return str(self.__list[1:])


list1 = PriorityQueueWithMaxHeap()  # list1은 작은 값, list2는 큰 값
list2 = PriorityQueueWithMinHeap()



