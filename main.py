import random

def initialize():
  bal = 50
  cry = random.randint(200,500)
  m_confid = 50
  return bal, cry

def movement(past_price, m_confid): #is to also be called idlely
  fluct = round(random.uniform(0,15),2)
  margin = 75 < random.randint(1,99) + (m_confid * 0.5)
  if margin:
    past_price += fluct * 3
  if not margin:
    past_price -= fluct * 3
  if past_price <= 0:
    past_price = 10
    m_confid = 45
  return past_price, m_confid

def credit(bal, amount, now, bench):
  if now > bench:
    bal += amount
  if now < bench:
    bal -= amount

  if bal < 0:
    bal, cry = initialize()
    return bal, cry, True

  return bal, None, False

def buy_sell(frc_price, bal, frc_bal, bors, amount): #bors is to be a true or false statement
  if bors:
    if bal >= frc_price * amount:
      bal -= frc_price * amount
      frc_bal += 1 * amount
  if not bors:
    if frc_bal >= amount:
      bal += frc_price * amount
      frc_bal -= 1 * amount
  return bal, frc_bal

def confidence(p_confid): #when displayed make sure it is a percent; also idle
  fluct = random.randint(0,5)
  margin = random.randint(1,2)
  if margin == 1:
    p_confid += fluct
  if margin == 2:
    p_confid -= fluct
  if p_confid < 1:
    p_confid = 10
  if p_confid > 99:
    p_confid = 90
  return p_confid
