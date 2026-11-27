import random

def tick(o_confid, o_price, o_time):
  confid = confidence(o_confid)

  head, p_confid, time = events(confid, o_time)
  if p_confid is None:
    p_confid = confid

  price, q_confid = movement(o_price, p_confid)

  return head, price, q_confid, time

def initialize():
  bal = 50
  cry = random.randint(200,500)
  m_confid = 50
  time = 800
  return bal, cry, time, m_confid

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

def events(confid, time):
  events = [("CEO Reinstated After Affairs", 2),
            ("AI Company After IPO Down 15%", 0.75),
            ("Pump and Dump Scam Affects New Coin", 0.5),
            ("Tech Bubble Suspicions Continue to Brew", 0.5),
            ("AI Companies Remain Unprofitable", 0.25),
            ("First Succesful Space Datacenter in Orbit", 1.5),
            ("In Rare Move, AI CEO Introduces Safety Measures", 1.25),
            ("Diplomacy Allows For New US-China Trade Relations", 1.5),
            ("AI Escapes Guardrails Causing a Cyberattack", 0.75),
            ("Questions Arise After New Details About Cyber Incident", 0.5),
            ("New Technology Allows for Farmers to Predict Crop Growth", 1.25)]

  odd = random.randint(1,time)

  if odd == 1:
    choice = random.choice(events)
    heading, n_confid = choice
    n_confid = confid * n_confid
    n_confid = round(n_confid)
    if n_confid > 99:
      n_confid = 99
    if n_confid < 1:
      n_confid = 1

    return heading, n_confid, 800

  else:
    n_time = time - 1

    return None, None, n_time

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
