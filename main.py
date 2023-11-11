print()

people = float(input("Enter the city's population: "))
area = float(input("Enter the city's area in square miles: "))

density = people / area
print(f"\nThe density is {density:,} per square mile.")

density_average_city = 4300
print(f"\nThe average US city has a density of {density_average_city:,} per square mile.")

if density < density_average_city:
  print("It is less crowded than the average US city.")
elif density > density_average_city:
  print("It is more crowded than the average US city.")
else:
  print("It is as crowded as the average US city.")
