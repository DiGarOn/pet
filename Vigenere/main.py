def create_molecules():
    molecules = []

    with open("input.txt", 'r') as f:
        c = 1
        for line in f:
            if "WIDTH=\"35%\"" in line:
                s = line.split(">")
                if c == 1:
                    molecules.append(s[1][:s[1].find("<")])
                c *= -1

    molecules = molecules[1:]
    return molecules
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print(create_molecules())
