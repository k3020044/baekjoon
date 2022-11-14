T = int(input())
for _ in range(T):
    input_a = list(map(int, input().split()))
    input_b = list(map(int, input().split()))

    # 카드 번호를 index로 하는 배열에 카드 개수 저장
    card_a = [0] * 5
    card_b = [0] * 5

    for i in range(1, input_a[0]+1):
        card_a[input_a[i]] += 1
    for i in range(1, input_b[0]+1):
        card_b[input_b[i]] += 1
    #print(card_a)
    #print(card_b)

    if card_a[4] != card_b[4]:
        if card_a[4] > card_b[4]:
            print('A')
        else:
            print('B')
    else:
        if card_a[3] != card_b[3]:
            if card_a[3] > card_b[3]:
                print('A')
            else:
                print('B')
        else:
            if card_a[2] != card_b[2]:
                if card_a[2] > card_b[2]:
                    print('A')
                else:
                    print('B')
            else:
                if card_a[1] != card_b[1]:
                    if card_a[1] > card_b[1]:
                        print('A')
                    else:
                        print('B')
                else:
                    print('D')