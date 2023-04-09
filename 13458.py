N = int(input()) # 시험장의 개수
A = map(int,input().split()) # i번 시험장에 있는 응시자의 수
B, C = map(int,input().split()) # 총감독관 감시 B명, 부감독관 감시 C명
# 각 시험장에 총감독관 : 1명 (오직) / 부감독관 : 여러명 가능
# 필요한 감독관 수의 최솟값
cnt = 0
for Ai in A:
    if B>=Ai:
        cnt+=1
        continue
    else:
        a = Ai-B
        cnt += 1
        cnt += int(a/C)+1
        if a % C == 0:
            cnt-=1
        
print(cnt)