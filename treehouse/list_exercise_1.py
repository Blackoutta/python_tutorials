continents = [
              'Asia',
              'South America',
              'North America',
              'Africa', 'Europe',
              'Antarctica',
              'Australia'
              ]

# Your code here
# search for items with the initial "A" and run code on them exclusively
for continent in continents:
    if continent[0] == "A":
        print("* " + continent)
