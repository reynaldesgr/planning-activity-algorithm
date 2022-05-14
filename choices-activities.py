
def extract_activities_from_files(file):
    planning = {}
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(":")
            planning[data[0]] = [ int(data[1]), int(data[2]) ]
    planning['a0'] = [0, 0]
    return planning 

def choose_recursive_planning_activies(dic, deb, end, i, n):
    m = i + 1
    p = []

    """if the next activity begin before the current activity end"""
    while m < n and dic[f"a{m}"][0] < dic[f"a{i}"][1]:
        m += 1

    """ we found an compatible activity sm > fi """
    if m < n:
        yield [f"a{m}", dic[f"a{m}"][0], dic[f"a{i}"][1]]
        yield from choose_recursive_planning_activies(dic, dic[f"a{m}"][0], dic[f"a{i}"][1], m, n) 

def choose_glouton_planning_activities(dic):
    first_activity = dic["a1"]
    p              = ["a1", first_activity]
    i              = 1
    m              = 2
    n              = len(list(dic.keys()))
    for m in range(2, n):
        if dic[f"a{m}"][0] > dic[f"a{i}"][1]:
            i = m
            h = dic[f"a{m}"] 
            p.append(f"a{m}")
            p.append(h)
    return p


p = extract_activities_from_files("activities.txt")
x = choose_recursive_planning_activies(p, 0, 0, 0, len(list(p.keys())))
y = choose_glouton_planning_activities(p)

for h in x:
    print(h)

print(y)
