import sys

if len(sys.argv) != 4:
    print ("illegal expression")
else:
    try:
        result = eval(' '.join(sys.argv[1]+sys.argv[2]+sys.argv[3]))
        print(result)
    except Exception:
        print("exeption")


