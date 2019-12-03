wires = []
with open('input', 'r') as f:
    for l in f.readlines():
        segments = l.split(',')
        wires.append(segments)

wires_elements = []
for wire in wires:
    current_pos = [0, 0]
    wire_elements = []
    for segment in wire:
        steps = int(segment[1:])
        for i in range(steps):
            if segment[0] == 'L':
                current_pos[0] = current_pos[0] - 1
            elif segment[0] == 'R':
                current_pos[0] = current_pos[0] + 1
            elif segment[0] == 'D':
                current_pos[1] = current_pos[1] - 1
            elif segment[0] == 'U':
                current_pos[1] = current_pos[1] + 1
            else:
                raise Exception('Unknown path element')

            wire_elements.append(tuple(current_pos))

    wires_elements.append(wire_elements)

intersection = set(wires_elements[0]).intersection(wires_elements[1])

min_manhatten_distance = 1e100
for e in intersection:
    manhatten_distance = abs(e[0]) + abs(e[1])
    print(e, manhatten_distance)
    if manhatten_distance < min_manhatten_distance:
        min_manhatten_distance = manhatten_distance

print(min_manhatten_distance)
