def solution(s):
    answer = len(s)
    for step in range(1, answer//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j+step]
                count = 1
        
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        answer = min(answer, len(compressed))
    return(answer)

print(solution('aabbaccc'))