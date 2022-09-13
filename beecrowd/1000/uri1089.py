while True:
    N = int(input())

    if N == 0:
        break

    mags = list(map(int,input().split()))

    peaks = 0

    for i in range(len(mags)):
        prev = mags[((i - 1) + N) % N]
        nex = mags[(i + 1) % N]

        if mags[i] < prev and mags[i] < nex or mags[i] > prev and mags[i] > nex:
            peaks += 1

    print(peaks)