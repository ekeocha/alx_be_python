def cube(side):
  volume = side **3
  surface_area = 6 * (side**2)
  return volume, surface_area

result = cube(3)
print(f"{result}")