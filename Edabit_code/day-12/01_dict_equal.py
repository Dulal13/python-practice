def is_equal(obj_one, obj_two):
    return list(obj_one.values()) == list(obj_two.values())


obj_one = {
  "name": "Jason",
  "phone": "9853759721",
  "email": "jason@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


res = is_equal(obj_one, obj_two)
print(res)