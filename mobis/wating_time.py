import copy

def solution(k, n, reqs):
    answer = 0
    
    '''
    n : 멘토의 수
    k : 상담 유형의 수
    reqs : 상담 요청 정보들
    각 유형별 멘토인원이 적어도 한명 이상이어야 한다.
    return : 기다린 시간의 합이 최소가 되는 대기시간
    [전략]
    1. 멘토를 유형별로 최소 1명씩은 배정하는 경우의 수 계산
    2. 각 경우에 대해서 대기시간 계산
    3. 전체 대기시간에서 최솟값 출력
    '''
    
    # 1. n-k 멘토를 k개 유형에 중복조합
    min_w_time = -1
    assert n-k>=0
    remains = list(range(k))
    h_cases = harmonic(remains,n-k)
    for h_case in h_cases:
        case = [1]*k
        for m_type in h_case:
            case[m_type]+=1
        # print(case)
        # 2. 대기시간 계산
        w_time = waiting_time(case,reqs)
        # print(case,w_time)
        # 3. 최솟값 계산
        if min_w_time==-1 or min_w_time>w_time:
            min_w_time = w_time
    
    answer = min_w_time
    
    return answer

def harmonic(arr,r):
    result = []
    
    def combinate(c,index):
        if len(c)==r:
            result.append(c)
            return
        
        for idx,data in enumerate(arr):
            if idx>=index:
                combinate(c+[data],idx)
    combinate([],-1)
    return result

def waiting_time(case,reqs):
    w_time = 0
    schedules = {}
    for i,c in enumerate(case):
        schedules[i+1]=[0]*c # {1:[0,0],2:[0],3:[0,0]}
    # print("schedules in 0",schedules)
    for req in reqs:
        req_start = req[0]
        req_takes = req[1]
        req_type = req[2]
        schedule = schedules[req_type]
        schedule.sort()
        if schedule[0]>req_start:
            w_time += schedule[0]-req_start
            schedule[0]+=req_takes
        else:
            schedule[0]=req_start+req_takes
        # print(schedules)        

    return w_time
        
        
        