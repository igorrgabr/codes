N = int(input())
hours = N // 3600
minutes = (N // 60) - hours * 60
seconds = (N - hours * 3600) - minutes * 60
print("{:d}:{:d}:{:d}".format(hours,minutes,seconds))