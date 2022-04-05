from collections import Counter, namedtuple
import heapq 

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(str):
    huffman_arr = []
    for ch, freq in Counter(str).items():
        huffman_arr.append((freq, len(huffman_arr), Leaf(ch)))
    heapq.heapify(huffman_arr)
    count = len(huffman_arr)
    while len(huffman_arr) > 1:
        freq1, _count1, left = heapq.heappop(huffman_arr)
        freq2, _count2, right = heapq.heappop(huffman_arr)
        heapq.heappush(huffman_arr, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if huffman_arr:
        [(_freq, _count, root)] = huffman_arr
        root.walk(code, "")
    return code


if __name__ == '__main__':
    s = input()
    h_code = huffman_encode(s)
    encoded = "".join(h_code[ch] for ch in s)
    for ch in sorted(h_code):
        print(f"{ch}: {h_code[ch]}")
