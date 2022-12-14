#!/usr/bin/env python3

import sys
import heapq

INPUT = "day12-input.txt"

INFINITY = sys.maxsize

# PrioQueue is a priority queue, based on a heap
class PrioQueue:
    # used as a placeholder for entries in the heap to mark then as removed after the entry priority has been adjusted.
    # based on https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
    REMOVED = "REMOVED"

    def __init__(self):
        # the heap maintanied sorted with heapq. Entries are [<priority>, payload] 2-item lists.
        self._heap = []
        # map of <payload> to the entries in the heap.  Allows indexing of the heap entry to "remove" an entry.
        # assumes that <payload> is hashable
        self._entries_map = {}
        

    def __len__(self):
        return len(self._entries_map) #not len(self._heap) which contains some REMOVED entries

    def pop(self):
        while self._heap:
            prio, p = heapq.heappop(self._heap)
            if p is not PrioQueue.REMOVED:
                break
        else:
            raise Exception("Pop from empty queue")
        del self._entries_map[p]
        return p


    def push(self, p, prio):
        if p in self._entries_map:
            raise Exception(f"Point {p} already in queue")
        entry = [prio, p]
        self._entries_map[p] = entry
        heapq.heappush(self._heap, entry)
        

    def adjust_prio(self, p, newprio):
        try:
            entry = self._entries_map[p]
        except KeyError:
            raise Exception(f"adjusting prio of unknown point {p}")
        entry[1] = PrioQueue.REMOVED
        entry = [newprio, p]
        heapq.heappush(self._heap, entry)
    


class VisitableMap:
    def __init__(self, m):
        self._m = m
        self.height = len(m)
        self.width = len(m[0])

        size = self.width * self.height
        self._non_visited = PrioQueue()
        self._dists_from_start = {}
        

    def get(self, p):
        return self._m[p[1]][p[0]]

    def get_special(self, p):
        v = self.get(p)
        if v == 'S':
            return 'a'
        if v == 'E':
            return 'z'
        return v

    def non_visited_count(self):
        return len(self._non_visited)

    def neighbours(self, p):
        val = ord(self.get_special(p))
        n = [(p[0]-1, p[1]), (p[0], p[1]-1), (p[0]+1, p[1]), (p[0], p[1]+1)]
        return [p for p in n if 0 <= p[0] < self.width and 0 <= p[1] < self.height and ord(self.get_special(p)) <= val+1]

    def pop_non_visited_minimum(self):
        return self._non_visited.pop()

    def set_dist_from_start(self, p, d):
        cur = self.get_dist_from_start(p)
        if cur == INFINITY:
            self._non_visited.push(p, d)
        else:
            self._non_visited.adjust_prio(p, d)  # has non inifity dist means it is already in the prioqueue
        self._dists_from_start[p] = d

    def get_dist_from_start(self, p):
        return self._dists_from_start.get(p, INFINITY)

class LinearMap:
    def __init__(self, init_val, width, height):
        self._width = width
        self._height = height
        self._m = [init_val] * (height*width)

    def get(self, p):
        return self._m[p[1] * self._width + p[0]]

    def set(self, p, val):
        self._m[p[1] * self._width + p[0]] = val


def dijkstra(map, start, end):
    predecessors = LinearMap(None, map.width, map.height)
    map.set_dist_from_start(start, 0)

    while map.non_visited_count() != 0:
        s = map.pop_non_visited_minimum()
        for n in map.neighbours(s):
            dist_through_s = map.get_dist_from_start(s) + 1
            if map.get_dist_from_start(n) > dist_through_s:
                map.set_dist_from_start(n, dist_through_s)
                predecessors.set(n, s)

    track = []
    s = end
    while s != start:
        track.append(s)
        s = predecessors.get(s)
    track.reverse()
    return track



if __name__ == '__main__':
    with open(INPUT, "r") as fIn:
        lines = [s.strip() for s in fIn.readlines()]
        
        map = VisitableMap(lines)

        print(f"right-down height: {map.get((map.width -1, map.height -1))}")

        for y in range(map.height):
            for x in range(map.width):
                v = map.get((x, y))
                if v == 'S':
                    start = (x, y)
                elif v == 'E':
                    end = (x, y)

        track = dijkstra(map, start, end)

        print(f"Result: {len(track)}, confirmed: 490")
