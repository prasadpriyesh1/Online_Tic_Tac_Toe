import pickle
import socket
from Objects import *
import threading


server = '192.168.43.51'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
p_id = 0
g_id = 0
games = {}


def Thread_client(player1, g_id1, conn):

    global games

    try:
        conn.send(str.encode(str(player1)))

    except socket.error as e1:
        print(e1)
    conn.recv(4096)
    conn.send(pickle.dumps(games[g_id1]))

    while True:
        pos = int(conn.recv(4096).decode())

        games[g_id].moveCount += 1
        if player1 == 1:
            games[g_id1].p1.append(pos)

            if games[g_id1].check_win_p1():
                games[g_id1].win_player = 1

            games[g_id1].players[0].turn = False
            games[g_id1].players[1].turn = True
        else:

            games[g_id1].p2.append(int(pos))
            if games[g_id1].check_win_p1():
                games[g_id1].win_player = 2

            games[g_id1].players[0].turn = True
            games[g_id1].players[1].turn = False
        games[g_id1].moves += 1
        if games[g_id1].moveCount == 9:
            if games[g_id1].win_player == '':
                games[g_id1].win_player = 3

        conn.send(pickle.dumps(games[g_id1]))


def main():

    global p_id, g_id, games
    conn, addr = s.accept()

    p_id += 1
    g_id = (p_id-1)//2
    if p_id % 2 == 1:
        player = 1
        games[g_id] = Game(g_id)
    else:
        games[g_id].ready = True
        player = 2
        games[g_id].players[0].turn = True
        games[g_id].players[1].turn = False
        games[g_id].players[0].move = 'cross'
        games[g_id].players[1].move = 'circle'

    t = threading.Thread(target = Thread_client, args= (player, g_id, conn))
    t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
    t.start()


main()
