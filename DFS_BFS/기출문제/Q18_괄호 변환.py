p = input()

def check_right(u):
  left_cnt = 0
  right_cnt = 0
  total_cnt = 0
  result = False
  for i in range(len(u)):
    if u[i] == "(":
      left_cnt += 1
    elif u[i] ==")":
      right_cnt += 1
    if left_cnt >= right_cnt:
      total_cnt += 1
  if total_cnt == len(u):
      result = True
  return result

def seperate(p):
  left_cnt = 0
  right_cnt = 0
  for i in range(len(p)):
    if p[i] == "(":
      left_cnt += 1
    elif p[i] ==")":
      right_cnt += 1
    if left_cnt == right_cnt:
       u = p[:i+1]
       v = p[i+1:]
       break
  return u, v

ans = ""

def solution(p):
  global ans
  
  if not p:
    return ""
    
  u, v = seperate(p)
  
  if check_right(u):
    ans = u + solution(v)
    
  else:
    ans = "(" + solution(v) + ")"
    new_u = u[1:len(u)-1]
    for i in range(len(new_u)):
      if new_u[i] == "(":
        ans += ")"
      elif new_u[i] == ")":
        ans += "("
        
  return ans

print(solution(p))