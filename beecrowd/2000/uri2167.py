N = int(input())
rpm_l = list(map(int,input().split()))
pos = 0
for i in range(1,len(rpm_l)):
    if rpm_l[i] < rpm_l[i-1]:
        pos = i+1
        break
print(pos)