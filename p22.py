def read_from_file(filename):
  txt = open(filename)
  string_of_names = txt.read()
  return string_of_names

def string_of_names_to_array(string_of_names):
  return string_of_names.replace('"','').split(",")

def get_alpha_value(string):
  sum = 0
  for char in string:
    sum += (ord(char) - 64)
  return sum

def main():
  sum = 0
  filename = "p022_names.txt"
  string_of_names = read_from_file(filename)
  array_of_names = string_of_names_to_array(string_of_names)
  array_of_names.sort()
  for i in range(0, len(array_of_names)):
    sum += (i+1) * get_alpha_value(array_of_names[i])
  return sum


def test_get_alpha_value():
  assert get_alpha_value("COLIN") == 53
  assert get_alpha_value("A") == 1
  assert get_alpha_value("Z") == 26

def test():
  test_get_alpha_value()

if __name__ == '__main__':
  test()
  print main()