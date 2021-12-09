import time

problems = []
for problem in range(1, 100):
    problem_name = str(problem).zfill(3)
    try:
        with open("problems/p" + problem_name + ".py") as f:
            print("> " + problem_name)
            
            time_start = time.time()
            exec(f.read())
            time_end = time.time()
            
            time_duration = round((time_end-time_start) * 1000)
            problems.append([problem_name, time_duration])
    except:
        pass

print("-----")
print("PROBLEMS:")
problems.sort(key=lambda x: x[1], reverse=True)
for problem in problems:
    print(str(problem[0]) + ": " + str(problem[1]) + "ms")