'''
692. Top K Frequent Words
Medium

856

81

Favorite

Share
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

class Solution:
    ''' 方法一 '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_words = collections.Counter(words)
        t = count_words.keys()
        res = sorted(t, key=lambda w : (-count_words[w], w))
        return list(res)[:k]

''' 方法二 '''
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.freq = 0
        self.end = False


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def insert(root, word):
            for c in word:
                root = root.child[c]
            root.freq += 1
            root.end = True
            return root.freq

        d = {}
        root = TrieNode()
        for word in words:
            d[word] = insert(root, word)

        keys = d.keys()
        res = sorted(keys, key=lambda w: (-d[w], w))
        return res[:k]

'''
题解：
方法一：使用python自带的collections.Counter方法统计词频，然后使用sored函数进行二次排序。
方法二：字典树 + sorted二次排序，字典树统计词频有利于压缩空间，空间复杂度为logN
'''