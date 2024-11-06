import heapq
from collections import defaultdict, Counter

# A class to represent the Huffman Tree Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # character
        self.freq = freq  # frequency of character
        self.left = None  # left child
        self.right = None  # right child

    # Defining comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    # Create a priority queue (min-heap) to store Huffman nodes
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Iterate until we have only one node in the priority queue
    while len(priority_queue) > 1:
        # Remove two nodes of the lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with these two nodes as children
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node to the priority queue
        heapq.heappush(priority_queue, merged)

    # The remaining node is the root of the Huffman Tree
    return priority_queue[0]


# Function to generate Huffman Codes by traversing the Huffman Tree
def generate_huffman_codes(root, current_code, codes):
    if root is None:
        return

    # If we reach a leaf node, it represents a character
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse the left subtree
    generate_huffman_codes(root.left, current_code + "0", codes)
    # Traverse the right subtree
    generate_huffman_codes(root.right, current_code + "1", codes)


# Function to encode the given text using Huffman Codes
def huffman_encoding(text):
    # Count frequency of each character
    frequency = Counter(text)

    # Build the Huffman Tree
    huffman_tree_root = build_huffman_tree(frequency)

    # Generate Huffman Codes
    codes = {}
    generate_huffman_codes(huffman_tree_root, "", codes)

    # Encode the text
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes


# Function to decode the encoded text using Huffman Codes
def huffman_decoding(encoded_text, codes):
    # Reverse the codes dictionary to get char by code
    reverse_codes = {code: char for char, code in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    
    return decoded_text


# Example usage
if __name__ == "__main__":
    text = "hello huffman"
    print(f"Original text: {text}")

    # Encoding
    encoded_text, codes = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}")
    print(f"Huffman Codes: {codes}")

    # Decoding
    decoded_text = huffman_decoding(encoded_text, codes)
    print(f"Decoded text: {decoded_text}")


"""Huffman encoding :
Huffman encoding is a lossless data compression algorithm that uses variable-length codes to represent data.
it assigns shorter codes to more frequent characters and longer codes to less frequent characters.
This approach reduces the overall size of the data by efficiently encoding high-frequency elements with shorter bit sequences.

Greedy Approach :
The greedy approach is an algorithmic strategy that makes a series of choices, each of which seems the best at the moment (locally optimal), with the hope that this will lead to a globally optimal solution.
Greedy algorithms are often used for optimization problems where the goal is to maximize or minimize a certain value."""
