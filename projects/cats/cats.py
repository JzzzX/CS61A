"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''      
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # 使用列表推导式找到符合条件（select）的所有段落
    filtered_paragraphs = [paragraph for paragraph in paragraphs if select(paragraph)]
    # 检查长度是否足够长，以找到第 k 个符合条件的段落
    if len(filtered_paragraphs) > k:
        return filtered_paragraphs[k]
    else:
        return ""
    # END PROBLEM 1


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    # 保留断言来检查 subject 列表中的单词是否为小写
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        # 抓换段落为小写
        paragraph = paragraph.lower()

        # 移除段落中的标点符号
        paragraph = remove_punctuation(paragraph)

        # 分割段落为单词表
        words = paragraph.split()

        # 遍历主题单词 检查是否存在匹配单词
        for word in subject:
            if word in words:
                return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    # 分割输入字符串为单词列表
    typed_words = split(typed)
    source_words = split(source)

    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # 处理边界情况
    # 如果 typed 和 source 都为空，返回 100.0
    if not typed_words and not source_words:
        return 100.0
    # 如果 typed 和 source 其中一个为空而另一个不为空，那么没有匹配项，准确率也是 0.0
    if not typed_words:
        return 0.0
    if not source_words:
        return 0.0
    
    # 定义递归函数来计算匹配的数量
    def count_matches(typed_words, source_words):
        # 基础情况，如果任何一个列表为空，返回 0
        if not typed_words or not source_words:
            return 0
        
        # 检查第一个单词是否匹配
        if typed_words[0] == source_words[0]:
            return 1 + count_matches(typed_words[1:], source_words[1:])
        else:
            return count_matches(typed_words[1:], source_words[1:])

    # 使用递归函数计算匹配的单词数量
    correct_count = count_matches(typed_words, source_words)

    # 计算准确率
    accuracy_percentage = (correct_count / len(typed_words)) * 100.0
    return accuracy_percentage
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # 计算字符总数
    total_character = len(typed)
    # 计算输入单词数量
    num_typed = total_character / 5
    # 计算时间
    elapsed = elapsed / 60
    #计算WPM
    wpm = num_typed / elapsed

    return wpm
    # END PROBLEM 4


############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 如果typed_word 在 word_list 中，直接返回
    if typed_word in word_list:
        return typed_word
    
    # 初始化最小差异为一个较大值，方便后续比较
    min_diff = float('inf') # 表示最小差异初始值设为无穷大
    best_word = typed_word # 用以储存差异最小的单词

    # 遍历 word_list 找到与 type_word 差异最小的单词
    for word in word_list:
        diff = diff_function(typed_word, word,limit)

        # 如果找到更小的差异，更新 min_diff 和 best_word
        if diff < min_diff:
            min_diff = diff
            best_word = word

    # 如果最小差异小于等于 limit，返回 best_word，否则返回 typed_word
    if min_diff <= limit:
        return best_word
    else:
        return typed_word

    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    # 基础情况 1: 如果 limit 小于 0，直接返回一个比 limit 大的值（超过了限制）
    if limit < 0:
        return limit + 1
    
    # 基础情况 2: 如果 typed 或 source 为空，返回剩余部分的长度（代表所有字符都需要修改）
    if len(typed) == 0 or len(source) == 0:
        return abs(len(typed) - len(source))
        
    # 递归过程
    # 比较第一个字符
    if typed[0] == source[0]:
        # 如果第一个字符相同，递归比较剩余部分
        return feline_fixes(typed[1:], source[1:], limit)
    else:
        # 如果第一个字符不同，替换次数加 1，递归比较剩余部分，同时将 limit 减 1
        return 1 + feline_fixes(typed[1:], source[1:], limit - 1)
    
    # END PROBLEM 6


############
# Phase 2B #
############


def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # basecase 与 problem6 一致
    if limit < 0: 
        return limit + 1
    if len(typed) == 0 or len(source) == 0: 
        return abs(len(typed) - len(source))

    # 递归的主逻辑：比较当前字符
    if typed[0] == source[0]:
        # 如果当前第一个字符相同 则递归比较剩余部分
        return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        # 如果字符不同，需要考虑三种可能的操作：添加、删除、替换
        # 注意每次操作都会消耗一次编辑机会，因此 limit - 1

        # 添加操作 将 source 第一个字符添加到 typed 中，然后递归
        add = 1 + minimum_mewtations(typed, source[1:], limit - 1)
        # 删除操作 将 typed 的第一个字符删除，然后继续递归比较剩余的部分
        remove = 1 + minimum_mewtations(typed[1:], source, limit - 1)
        # 替换操作 将 typed 的第一个字符替换为 source 的第一个字符，以便两者匹配，然后递归
        substitute = 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
        return min(add, remove, substitute)
        

def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'

FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # 初始化正确的单词
    correct_count = 0

    # 循环遍历
    for i in range(len(typed)):
        if typed[i] == source[i]:
            correct_count += 1
        else:
            break

    # 计算进度
    progress = correct_count / len(source)

    # 上传进度
    upload({'id': user_id, 'progress': progress})

    return progress
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # 初始化时间结果列表
    times = []

    # 遍历每个玩家的时间戳
    for timestamps in timestamps_per_player:
        # 初始化储存每个玩家时间差的列表
        player_times = []

        # 遍历时间戳，计算相邻时间点的时间差
        for i in range(1, len(timestamps)):
            time_spent = timestamps[i] - timestamps[i - 1]
            player_times.append(time_spent)

        # 添加到时间表
        times.append(player_times)

    # 使用构造函数创建 match 数据结构，
    match_data = match(words, times)
    return match_data
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # 初始化每个玩家的最快单词列表
    fastest_words_for_players = [[] for _ in player_indices]
    
    # 遍历每个单词的索引
    for word_index in word_indices:
        # 初始化最快玩家和最短时间
        fastest_player = 0
        fastest_time = time(match, 0, word_index)

        # 遍历每个玩家 找到最快的玩家
        for player_num in player_indices:
            player_time = time(match, player_num, word_index)
            if player_time < fastest_time:
                fastest_player = player_num
                fastest_time = player_time

        # 将该单词添加到最快玩家的列表中
        fastest_words_for_players[fastest_player].append(get_word(match, word_index))

    return fastest_words_for_players
    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)