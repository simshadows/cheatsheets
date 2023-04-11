#!/usr/bin/env python3

"""
file:   heap-demo.py
author: simshadows <contact@simshadows.com>

Max-heap demonstration.
"""

def heapify(heap):
    for i in range(len(heap) >> 1, 0, -1):
        sift_down(heap, i - 1)

def hpush(heap, item):
    heap.append(item)
    sift_up(heap, len(heap) - 1)

# PRECONDITION: len(heap) > 0
def hpop(heap):
    to_return = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return to_return

# PRECONDITION: len(heap) > 0
def hpushpop(heap, item):
    if item < heap[0]:
        (item, heap[0]) = (heap[0], item)
        sift_down(heap, 0)
    return item

# PRECONDITION: len(heap) > 0
def hpoppush(heap, item):
    (item, heap[0]) = (heap[0], item)
    sift_down(heap, 0)
    return item

def sift_down(heap, i):
    left = (i << 1) + 1
    if left >= len(heap):
        return
    right = left + 1

    if (right >= len(heap)) \
            or (heap[left] > heap[right]):
        next_child = left
    else:
        next_child = right

    if heap[next_child] <= heap[i]:
        return
    (heap[next_child], heap[i]) = \
            (heap[i], heap[next_child])
    sift_down(heap, next_child)

def sift_up(heap, i):
    parent = (i - 1) >> 1
    if (i == 0) or (heap[parent] > heap[i]):
        return
    (heap[parent], heap[i]) = (heap[i], heap[parent])
    sift_up(heap, parent)

print("=== HEAPIFY ===");

heap = [18, 35, 74, 36, 29, 81, 5, 57, 87, 68, 41, 94]
print(heap)
heapify(heap)
print(heap)

template = heap.copy()

print("=== PUSH ===")

print(heap)
hpush(heap, 92)
print(heap)

print("=== POP ===")

heap = template.copy()
print(heap)
result = hpop(heap)
print(result)
print(heap)

print("=== PUSH-POP ===")

print("Push-popping 37")
heap = template.copy()
print(heap)
result = hpushpop(heap, 37)
print(result)
print(heap)
print()

print("Push-popping 95")
heap = template.copy()
print(heap)
result = hpushpop(heap, 95)
print(result)
print(heap)

print("=== POP-PUSH ===")

print("Push-popping 37")
heap = template.copy()
print(heap)
result = hpoppush(heap, 37)
print(result)
print(heap)
print()

print("Push-popping 95")
heap = template.copy()
print(heap)
result = hpoppush(heap, 95)
print(result)
print(heap)

