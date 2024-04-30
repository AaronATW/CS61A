"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    selectable_paragraphs = [paragraph for paragraph in paragraphs if select(paragraph)]
    if k >= len(selectable_paragraphs):
        return ''
    else:
        return selectable_paragraphs[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def about_func(paragraph):
        words = split(lower(remove_punctuation(paragraph)))
        for word in words:
            if word in topic:
                return True
        return False
    return about_func
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

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
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if not typed or not reference:
        return 0.0
    right, wrong, i = 0, 0, 0
    while i < len(typed_words):
        if i < len(reference_words):
            if typed_words[i] == reference_words[i]:
                right += 1
            else:
                wrong += 1
        else:
            wrong += 1
        i += 1
    return right * 100 / (right + wrong)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed) / 5 / (elapsed / 60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    min_diff, best_word = float("inf"), ""
    for goal_word in valid_words:
        diff = diff_function(user_word, goal_word, limit)
        if diff < min_diff:
            min_diff, best_word = diff, goal_word
    if min_diff > limit:
        return user_word
    return best_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    diff_len = len(start) - len(goal)
    min_len = min(len(start), len(goal))
    if abs(diff_len) > limit:
        return limit + 1
    def compare(start, goal, pos, accu):
        if pos >= min_len:
            return accu
        if start[pos] != goal[pos]:
            accu += 1
            if accu + abs(diff_len) > limit:
                return limit + 1
        return compare(start, goal, pos + 1, accu)
    return compare(start, goal, 0, 0) + abs(diff_len)
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if start == goal: # Fill in the condition
        # BEGIN
        return 0
        # END
    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        return len(start) + len(goal)
        # END  
    elif limit <= 0:
        return float("inf")
    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + meowstake_matches(start, goal[1:], limit - 1)
        remove_diff = 1 + meowstake_matches(start[1:], goal, limit - 1)
        substitute_diff = 1 + meowstake_matches(start[1:], goal[1:], limit - 1)
        # BEGIN
        return min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    right_words = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            right_words += 1
        else:
            break
    ratio = right_words / len(prompt)
    send({'id': id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    def cal_diff_timestamp(lst):
        if len(lst) <= 1:
            return []
        else:
            return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]
    times = [cal_diff_timestamp(lst) for lst in times_per_player]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    result = []
    for i in players:
        result.append([])
    for i in words:
        fastest_player_id = min(players, key = lambda x: time(game, x, i))     
        result[fastest_player_id].append(word_at(game, i))
    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    if start == goal:
        return 0
    elif limit <= 0:
        return float("inf")
    elif len(start) * len(goal) == 0:
        return len(start) + len(goal)
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + key_distance_diff(start, goal[1:], limit - 1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit - 1)
        sub_diff = key_distance_diff(start[1:], goal[1:], limit - 1) + key_distance[start[0], goal[0]]
        return min(add_diff, remove_diff, sub_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized
key_distance_diff = memo(key_distance_diff)
key_distance_diff = count(key_distance_diff)

def memo_autocorrect(f):
    cache = {}
    def memoized(user_word, valid_words, diff_function, limit):
        if (user_word, diff_function) not in cache:
            cache[user_word, diff_function] = f(user_word, valid_words, diff_function, limit)
        return cache[user_word, diff_function]
    return memoized

def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""
    # BEGIN PROBLEM EC2
    if user_word in valid_words:
        return user_word
    min_diff, best_word = float("inf"), ""
    for goal_word in valid_words:
        diff = diff_function(user_word, goal_word, limit)
        if diff < min_diff:
            min_diff, best_word = diff, goal_word
    if min_diff > limit:
        return user_word
    return best_word
    # END PROBLEM EC2
faster_autocorrect = memo_autocorrect(faster_autocorrect)

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
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
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
        print('Accuracy:        ', accuracy(typed, reference))

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