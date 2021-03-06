def jug():
    global jug1size
    jug1size = int(input("Enter Capacity of jug 1:"))
    global jug2size
    jug2size = int(input("Enter Capacity of jug 2:"))

    goalstate1 = input("Final state jug 1:")
    goalstate2 = input("Final state jug 2:")

    startstate = (0, 0)
    goalstate = (int(goalstate1), int(goalstate2))

    list = []
    list.append([startstate])

    print("Jug sizes: " + str(jug1size) + ", " + str(jug2size))
    print("Starting state: " + str(startstate))
    print("Goal state: " + str(goalstate))

    while (1):
        if len(list) == 0:
            print("This cannot be happen")
            exit(0)
        curnode = list.pop(0)

        if curnode[-1] == goalstate:
            print("There is a solution:")
            print(curnode)
            exit(0)

        list += S(curnode)


def S(node):
    returnlist = []
    state = node[-1]
    jug1, jug2 = state

    def checkState(new_state, old_state):
        if new_state != old_state:
            if not new_state in node:
                new_node = node.copy()
                new_node.append(new_state)
                returnlist.append(new_node)

    slist = [(jug1, 0), (0, jug2), (jug1size, jug2), (jug1, jug2size),
             (jug1 - min(jug1, jug2size - jug2), jug2 + min(jug1, jug2size - jug2)),
             (jug1 + min(jug2, jug1size - jug1), jug2 - min(jug2, jug1size - jug1))]
    for s in slist:
        checkState(s, state)

    return returnlist


if __name__ == "__main__":
    print("Water jug problem solver Using DFS: ")
    jug()
