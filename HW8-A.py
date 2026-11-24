
N = int(input())

if N > 0:
    playlist = input().split()
else:
    playlist = input().split()

Q = int(input())

for i in range(Q):
    command = input().split()

    if command[0] == "ADD":
        playlist.append(command[1])

    elif command[0] == "REMOVE":
        if command[1] in playlist:
            playlist.remove(command[1])

    elif command[0] == "REVERSE":
        playlist.reverse()

print(len(playlist))

if len(playlist) == 0:
    print("EMPTY")
else:
    print(" ".join(playlist))
