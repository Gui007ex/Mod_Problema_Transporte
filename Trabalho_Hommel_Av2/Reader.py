def next_line(f):
    if len(f):
        return list(map(int, f.pop(0).split()))

def filter_Data(path: str):
    arq = open(path, "r")
    file = arq.read().split("\n")
    arq.close()

    origins, destinies = map(int, file.pop(0).split())
    data = {"prod":{}, "dem":{}, "costs":{}}
    data["prod"] = {f"O{i+1}":num for i, num in enumerate(next_line(file))}
    data["dem"] = {f"D{i+1}":num for i, num in enumerate(next_line(file))}
    for origin in data["prod"]:
        costs = next_line(file)
        for destiny in data["dem"]:
            data["costs"][f"{origin}_{destiny}"] = costs.pop(0)

    return origins, destinies, data