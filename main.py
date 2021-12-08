#

# Dictionary of distances between cities
dist = {'Cape Town':{'Johannesburg':1261},
'Pretoria':{'Cape Town': 1308.26},
'Durban':{'Johannesburg':500.68,'Pretoria':535.35}}

# Input for distances between cities
cities = ['Durban', 'Cape Town']


pair = {cities, dist}

route_parameters = pair


def getkeylist(dict):
  list_of_keys = dict.keys()
  
  list_to_return = []
  for i in cities:
    list_to_return.append(i)
    print(i)
    return list_to_return

def get_smallest_dist(dict):
  
  values = dict.values()
  low_dist = values[0]
  return low_dist
  
  
def getValList (list):

  values = list.values()
  options = [i for i in values]
 
  return options


cities =  getValList(dist)
print(cities)

##zoom seems to be updating XD


  # yupp I am on it
  #cool cool, I'll start working on the other function now

def shortest_distance(route_parameters):
  test_dict = {'Johannesburg':500.68,'Pretoria':535.35}
  get_smallest_dist(test_dict)

# no typing, pens down 
