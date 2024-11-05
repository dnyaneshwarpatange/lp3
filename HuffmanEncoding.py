import heapq
from collections import defaultdict

# Define a class for Huffman Nodes with comparison based on frequency
class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # This method allows heapq to compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    # Create a heap of nodes from the frequency dictionary
    heap = [HuffmanNode(freq, char) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree by merging nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        # If it's a leaf node, add the code to the codebook
        codebook[node.char] = prefix
    else:
        # Traverse left (0) and right (1)
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    frequency = defaultdict(int, {char: data.count(char) for char in set(data)})
    root = build_huffman_tree(frequency)
    huffman_codes = build_codes(root)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code, decoded_data = "", []
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""
    return ''.join(decoded_data)

# Get user input
data = input("Enter a string to encode: ")
encoded_data, huffman_codes = huffman_encoding(data)

print("Original Data:", data)
print("Encoded Data:", encoded_data)
print("Huffman Codes:", huffman_codes)
print("Decoded Data:", huffman_decoding(encoded_data, huffman_codes))
