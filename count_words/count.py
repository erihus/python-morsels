import re
from collections import Counter


def count_words(string):
  words = string.split(' ');
  counts = {}

  for word in words:
    word = word.lower()
    word = re.sub("[^a-zA-Z\']", "", word)
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1

  return counts


def solution_count_words(string):
  return Counter(re.findall(r"[\w'-]+", string.lower()))