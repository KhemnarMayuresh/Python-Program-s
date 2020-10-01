# Program to output unique names from two list

def main():
  names1 = ["Ava", "Emma", "Olivia"]
  names2 = ["Olivia", "Sophia", "Emma"]
  print(set(names1+names2))
main()

# output: {'Ava', 'Olivia', 'Sophia', 'Emma'}
