import requests
from heapq import *


def start_api(url, problem):
    header = {'X-Auth-Token': '8c5a24b740aadacc75c1581753b817fe',
              'Content-Type': 'application/json'}

    data = {"problem": f'{problem}'
            }

    response = requests.post(url+'/start', headers=header, json=data).json()
    return response["auth_key"]


def waiting_line_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/waiting_line', headers=header).json()
    return response["waiting_line"]


def game_result_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/game_result', headers=header).json()
    return response["game_result"]


def user_info_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/user_info', headers=header).json()
    return response["user_info"]


def match_api(url, key, match_list):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    data = {"pairs": match_list}

    response = requests.put(url + '/match', headers=header, json=data).json()
    print(response)
    return response


def change_grade_api(url, key, command):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    data = {"commands": command}

    response = requests.put(url + '/change_grade', headers=header, json=data).json()
    return response


def score_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/score', headers=header).json()
    print(response)
    return response["score"]


def match_users(user_grade, waiting_lines, wait_limit, max_time, max_time_limit):
    heap = []
    pairs = []
    if len(waiting_lines) > wait_limit or max_time > max_time_limit:
        for waiting_line in waiting_lines:
            user_id = waiting_line['id']
            user_from = waiting_line['from']
            heappush(heap, (-user_grade[user_id], user_from, user_id))
        while len(heap) > 1:
            user1 = heappop(heap)
            user2 = heappop(heap)
            pairs.append([user1[2], user2[2]])

    return pairs
