def reconstruct_file(fragments):
    # Concatenate each pair of fragments together
    concatenated_fragments = [''.join(pair) for pair in zip(fragments[::2], fragments[1::2])]
    
    # Count occurrences of each bit position
    bit_counts = [0] * len(concatenated_fragments[0])
    for fragment in concatenated_fragments:
        for i, bit in enumerate(fragment):
            if bit == '1':
                bit_counts[i] += 1
    
    # Construct the original file based on the bit counts
    reconstructed_file = ''.join(['1' if count % 2 != 0 else '0' for count in bit_counts])
    return reconstructed_file

def main():
    num_cases = int(input())
    input()  # Consume the blank line
    
    for _ in range(num_cases):
        fragments = []
        while True:
            try:
                fragment = input().strip()
                if not fragment:
                    break
                fragments.append(fragment)
            except EOFError:
                break
        
        result = reconstruct_file(fragments)
        print(result)
        
        if num_cases > 1:
            print()

if __name__ == "__main__":
    main()
