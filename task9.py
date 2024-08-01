#problem1 : ion get it 


#problem2
# def somescoreboard(round):
#   scoreboard = {}
#   for player, score in round:
#     scoreboard[player] = scoreboard.get(player, 0) + score
#   return scoreboard

# rounds = [(1, 5), (2, 3), (1, 2), (3, 4), (2, 1), (1, 3)]
# final = somescoreboard(rounds)
# print(final)

#problem3
def remove_occurrences(list, num):
  return [kys for kys in list if kys != num]

def add_contact(contacts, name, phone):
  contacts[name] = phone

def remove_contact(contacts, name):
  return name in contacts and contacts.pop(name, None) is not None

def search_contact(contacts, search_term):
  return [f"{name}: {phone}" for name, phone in contacts.items() if name.lower().find(search_term.lower()) != -1]

def view_all_contacts(contacts):
  return [f"{name}: {phone}" for name, phone in contacts.items()]

def update_contact(contacts, name, phone):
  if name in contacts:
    contacts[name] = phone
    return True
  return False
