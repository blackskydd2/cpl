from collections import Counter

def longest_common_subsequence(a, b):
    # Count occurrences of letters in both strings
    count_a = Counter(a)
    count_b = Counter(b)
    
    # Initialize an empty list to store the characters of the longest common subsequence
    common_subsequence = []
    
    # Iterate through lowercase letters
    for char in "abcdefghijklmnopqrstuvwxyz":
        # Determine the minimum count of the current letter in both strings
        min_count = min(count_a[char], count_b[char])
        
        # Append the current letter to the common subsequence min_count times
        common_subsequence.extend([char] * min_count)
    
    # Convert the list of characters to a string
    return ''.join(common_subsequence)

def main():
    while True:
        try:
            # Read two lines of input
            a = input()
            b = input()
            
            # Calculate the longest common subsequence and print it
            result = longest_common_subsequence(a, b)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()
