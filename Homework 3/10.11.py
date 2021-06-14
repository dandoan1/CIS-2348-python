#Dan Doan 1986920
class FoodItem: # TODO: Define constructor with parameters to initialize instance # attributes (name, fat, carbs, protein)
  def __init__(self, name="None", fat=0.00, carbs=0.00, protein=0.00):
    self.name = name
    self.fat = fat
    self.carbs = carbs
    self.protein = protein
  def get_calories(self, num_servings):
      # Calorie formula
      calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
      return calories

  def print_info(self):
      print('Nutritional information per serving of {}:'.format(self.name))
      print('   Fat: {:.2f} g'.format(self.fat))
      print('   Carbohydrates: {:.2f} g'.format(self.carbs))
      print('   Protein: {:.2f} g'.format(self.protein))
if __name__=="__main__":
  food = FoodItem()
  name = input()
  fat = float(input())
  carbs = float(input())
  protein = float(input())
  servings = float(input())
  food.print_info()
  calorie = (food.get_calories(servings)) #can get calorie numbers
  print("Number of calories for {:.2f} serving(s): {:.2f}".format(servings, calorie))
  print()
  food.name = name
  food.fat = fat
  food.carbs = carbs
  food.protein = protein
  food.print_info()
  calorie = (food.get_calories(servings)) #can get calorie numbers
  print("Number of calories for {:.2f} serving(s): {:.2f}".format(servings, calorie))