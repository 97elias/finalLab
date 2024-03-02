from elias import MapEdges


def main():
  map_edges = MapEdges()
  
  # Program som skriver ut stadsnamnen och dess koordinater på min ö
  for city in map_edges.cities:
    #print(city)
    pass #ta bort denna senare


  index = map_edges.getIndexFromCity('Advertisement')
  print(index)

main()