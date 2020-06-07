if __name__ == "__main__":
    try:
        t = int(input())
    except:
        pass
    for _ in range(t):
        try:
            n = int(input())
            arr = list(map(int, input().split()))
        except:
            pass
        flag = 0; c5 = 0; c10 = 0; c15 = 0
        for j in range(n):
            if arr[j] == 5:
                c5 = c5+1
            elif arr[j] == 10:
                if c5>0:
                    c10 = c10+1
                    c5 = c5-1
                else:
                    flag=1
            elif arr[j] == 15:
                if c10>0:
                    c10 = c10-1
                    c15 = c15+1
                elif c5>1:
                    c5 = c5-2
                    c15 = c15+1
                else:
                    flag = 1
            if flag == 1:
                print("NO")
                break
        if flag == 0:
            print("YES")