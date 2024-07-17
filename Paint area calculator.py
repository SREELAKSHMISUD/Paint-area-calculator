import math
def paint_calc(height, width, cover):
  num_cans=(height*width)/coverage
  round_num_cans=math.ceil(num_cans)
  print(f"You'll need {round_num_cans} cans of paint.")

test_h = int(input("enter height: ")) # Height of wall (m)
test_w = int(input("enter width: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

