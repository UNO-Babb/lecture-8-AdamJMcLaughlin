def main():
  myFile = open("ufo_sightings.csv", 'r')

  for line in myFile:
            info = line.strip().split()
            if len(info) > 12:
              city = info[0]
              state = info[1]
              shape = info[3]
              description = info[5]
              print(f"In {city} {state} a {shape} {description}.")
              



if __name__ == '__main__':
  main()
