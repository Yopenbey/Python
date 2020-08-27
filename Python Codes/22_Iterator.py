carros=["HRV","Polo","Jetta","Cruze"]
itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("\nFim da Lista")
        break