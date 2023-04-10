#!/usr/bin/env node

function heapify(heap) {
    for (let i = (heap.length >> 1) - 1; i >= 0; --i) {
        _siftDown(heap, i);
    }
}

function hpush(heap, item) {
    let curr = heap.length;
    heap.push(item);
    _siftUp(heap, curr);
}

// Assumes heap.length > 0
function hpop(heap) {
    if (heap.length === 1) return heap.pop();
    const toReturn = heap[0];
    heap[0] = heap.pop();
    _siftDown(heap, 0);
    return toReturn;
}

// Assumes heap.length > 0
function hpushpop(heap, item) {
    if (item[0] < heap[0][0]) {
        [item, heap[0]] = [heap[0], item];
        _siftDown(heap, 0);
    }
    return item;
}

function _siftDown(heap, i) {
    const left = (i << 1) + 1;
    if (heap[left] === undefined) return;
    const right = left + 1;
    const next =
        (heap[right] === undefined || heap[left][0] > heap[right][0])
        ? left
        : right;
    if (heap[next][0] <= heap[i][0]) return;
    [heap[next], heap[i]] = [heap[i], heap[next]];
    _siftDown(heap, next);
}
function _siftUp(heap, i) {
    if (i === 0) return; 
    const parent = (i - 1) >> 1;
    if (heap[parent][0] > heap[i][0]) return;
    [heap[parent], heap[i]] = [heap[i], heap[parent]];
    _siftUp(heap, parent);
}

//function graphicalHeap(h) {
//    console.log("==================================");
//    console.log(`                ${h[0]}`);
//    console.log(`       ${h[1]}               ${h[2]}`);
//    console.log(`   ${h[3]}      ${h[4]}       ${h[5]}      ${h[6]}`);
//    console.log(` ${h[7]}  ${h[8]}  ${h[9]}  ${h[10]}   ${h[11]}`);
//    console.log("==================================");
//}

console.log("=== HEAPIFY ===");

heap = [[18], [35], [74], [36], [29], [81], [5], [57], [87], [68], [41], [94]];
console.log(heap);
heapify(heap);
console.log(heap);

