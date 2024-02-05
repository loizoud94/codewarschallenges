def solution(number):
    collected_numbers = []
    if number < 0:
        return 0
    else:
        for i in range(number):
            if i % 3 == 0:
                collected_numbers.append(i)
            elif i % 5 == 0:
                collected_numbers.append(i)
        
        return sum(collected_numbers)
