# pip install jovian --upgrade --quiet

from jovian.pythondsa import evaluate_test_cases

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
    return -1

def binary_search_card(cards, query):
    lo, hi = 0, len(cards)-1

    while(lo <= hi):
        mid = (lo+hi)//2
        mid_n = cards[mid]

        print('lo:',lo,'high:',hi,'mid:',mid,'mid number:',mid_n)

        if mid_n == query:
            return mid
        if mid_n > query:
            hi = mid-1
        if mid_n < query:
            lo = mid+1

    return -1

tests = []
tests.append({
    'input':{
        'cards':[13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
        },
    'output':3
    })
tests.append({
    'input':{
        'cards':[0, 1, 3, 4, 7, 10, 11, 13],
        'query': 1
        },
    'output': 1
    })
tests.append({
    'input':{
        'cards':[-1, 1, 2, 4],
        'query': 4
        },
    'output': 3
    })
tests.append({
    'input':{
        'cards':[-127, -9, -1, 3],
        'query': -127
        },
    'output': 0
    })
tests.append({
    'input':{
        'cards':[6],
        'query': 6
        },
    'output': 0
    })
tests.append({
    'input':{
        'cards':[-9, 2, 5, 7, 9],
        'query': 4
        },
    'output':-1
    })
tests.append({
    'input':{
        'cards':[],
        'query': 7
        },
    'output':-1
    })
tests.append({
    'input':{
        'cards':[0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
        'query': 3
        },
    'output': 6
    })
tests.append({
    'input':{
        'cards':[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
        },
    'output': 2
    })
tests.append({
    'input':{
        'cards':[0]*1000000+[1]*1000000+[2]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000
        +[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[3]*1000000+[21],
        'query': 21 
        },
    'output': 55000000
    })

#evaluate_test_cases(locate_card, tests)
evaluate_test_cases(binary_search_card, tests)
