T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    
    # 충전 횟수와 현재 위치 초기화
    cnt = 0
    current_position = 0
    
    # 충전기가 설치된 곳에 충전소 표시
    charge_stations = [0] * (N + 1)
    for station in lst:
        charge_stations[station] = 1
    
    while current_position + K < N:
        # 다음 충전기가 있는 곳을 찾음
        next_charge = -1
        for i in range(current_position + K, current_position, -1):
            if charge_stations[i] == 1:
                next_charge = i
                break
        
        # 충전기가 없는 경우 종점에 도달할 수 없음
        if next_charge == -1:
            cnt = 0
            break
        
        current_position = next_charge
        cnt += 1
    
    print(f'#{tc} {cnt}')