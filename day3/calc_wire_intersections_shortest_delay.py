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

min_delay = 1e100
for e in intersection:
    delay1 = wires_elements[0].index(e) + 1
    delay2 = wires_elements[1].index(e) + 1
    total_delay = delay1 + delay2
    print(e, total_delay)

    if total_delay < min_delay:
        min_delay = total_delay

print("minimum delay: {} steps".format(min_delay))
