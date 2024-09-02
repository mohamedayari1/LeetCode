class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj =  collections.defaultdict(list)
        l = wordList
        l.append(beginWord)
        
        for word in l:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]   
                adj[pattern].append(word)

        visited = set(beginWord)
        queue =  collections.deque([(beginWord, 1)])

        while queue:
            for j in range(len(queue)):
                word, depth = queue.popleft()

                if word == endWord: 
                    return depth 

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]   
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append((nei, depth + 1))
                            visited.add(nei)
        return 0
