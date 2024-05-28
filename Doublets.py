from collections import deque

def build_graph(words):
    graph = {}
    for word in words:
        graph[word] = []
        for i in range(len(word)):
            for j in range(97, 123):  # ASCII values for lowercase letters
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word != word and new_word in words:
                    graph[word].append(new_word)
    return graph

def find_shortest_sequence(graph, start, end):
    visited = {start: None}
    queue = deque([start])

    while queue:
        current_word = queue.popleft()
        if current_word == end:
            break
        for neighbor in graph[current_word]:
            if neighbor not in visited:
                visited[neighbor] = current_word
                queue.append(neighbor)

    if end not in visited:
        return None
    
    # Reconstruct the shortest sequence
    sequence = [end]
    while sequence[-1] != start:
        sequence.append(visited[sequence[-1]])
    sequence.reverse()
    return sequence

def main():
    dictionary = []
    while True:
        word = input().strip()
        if not word:
            break
        dictionary.append(word)

    graph = build_graph(dictionary)

    while True:
        try:
            pair = input().split()
            if not pair:
                break
            start, end = pair
            sequence = find_shortest_sequence(graph, start, end)
            if sequence:
                print("\n".join(sequence))
            else:
                print("No solution.")
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()
