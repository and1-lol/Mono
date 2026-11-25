import random

def initialize():
  bal = 50
  cry = random.randint(200,500)
  m_confid = 50
  return bal, cry

def movement(past_price, m_confid): #is to also be called idlely
  fluct = round(random.uniform(0,10),2)
  margin = random.randint(1,99) < m_confid
  if margin:
    past_price += fluct * 2
  if not margin:
    past_price -= fluct * 2
  if past_price <= 0:
    past_price = 10
  return past_price

def wager(bal, amount, current, p_confid):
  bench = current
  now = current
  for _ in range(30):
    now = movement(now, p_confid)
    if _ % 3 == 0:
      p_confid = confidence(p_confid)

  if now > bench:
    bal += amount
  if now < bench:
    bal -= amount
  if now == bal:
    pass

  if bal < 0:
    bal, now = initialize()
    return None

  return bal, now, p_confid

def confidence(p_confid): #when displayed make sure it is a percent; also idle
  fluct = random.randint(0,5)
  margin = random.randint(1,2)
  if margin == 1:
    p_confid += fluct
  if margin == 2:
    p_confid -= fluct
  if p_confid < 1:
    p_confid = 5
  if p_confid > 99:
    p_confid = 95
  return p_confid
