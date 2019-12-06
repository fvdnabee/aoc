def calc_path(orbits, obj):
    path = []

    stop = False
    while not stop:
        v = orbits[obj]
        path.append(v)
        obj = v
        if obj == "COM":
            stop = True

    return path

def calc_orbital_transfers(pathA, pathB):
    # First find common root between both paths:
    root_idx = 0
    while pathA[root_idx] not in pathB:
        root_idx += 1
    root = pathA[root_idx]

    # orb transfers in pathA to root plus orb transfers in pathB to root
    n_transfersA = pathA.index(root)
    n_transfersB = pathB.index(root)

    return n_transfersA + n_transfersB


def run():
    with open('input', 'r') as f:
        inp = f.readlines()

    orbits = {}
    for orbit in inp:
        obj1, obj2 = orbit.split(")")
        orbits[obj2.strip()] = obj1

    print(orbits)
    n_orbits = 0
    for k in orbits:
        if k == 'COM':
            raise Exception("Unexpected key in orbits")

        stop = False
        while not stop:
            n_orbits += 1
            v = orbits[k]
            k = v
            if k == "COM":
                stop = True

    print(n_orbits)

    path_YOU = calc_path(orbits, 'YOU')
    path_SAN = calc_path(orbits, 'SAN')
    n_transfers = calc_orbital_transfers(path_YOU, path_SAN)
    print(n_transfers)


if __name__ == "__main__":
    run()
