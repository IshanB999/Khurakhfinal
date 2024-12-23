from mealplans.models import MealCategory, Meal, PredefinedMealPlan, PredefinedDailyMeal
from django.utils import timezone

# Create meal categories
low_carb = MealCategory.objects.create(name="Low Carb", description="A meal plan focusing on low-carbohydrate meals to aid in weight loss or blood sugar control.")
vegetarian = MealCategory.objects.create(name="Vegetarian", description="A plant-based meal plan, avoiding all meat and fish.")
vegan = MealCategory.objects.create(name="Vegan", description="A fully plant-based meal plan without any animal products.")
non_veg = MealCategory.objects.create(name="Non-Vegetarian", description="A balanced meal plan including both plant-based meals and meat or fish.")

# Create meals
grilled_chicken_salad = Meal.objects.create(name="Grilled Chicken Salad", category=low_carb, calories=350, protein=30, carbs=10, fats=15, description="Grilled chicken breast served over mixed greens.")
zucchini_noodles_pesto = Meal.objects.create(name="Zucchini Noodles with Pesto", category=low_carb, calories=250, protein=5, carbs=10, fats=20, description="Spiralized zucchini with homemade basil pesto.")
spinach_feta_omelette = Meal.objects.create(name="Spinach and Feta Omelette", category=vegetarian, calories=200, protein=12, carbs=5, fats=15, description="A fluffy omelette filled with fresh spinach and feta.")
vegetable_stir_fry = Meal.objects.create(name="Vegetable Stir Fry", category=vegetarian, calories=300, protein=10, carbs=40, fats=5, description="Mixed vegetables stir-fried in a light soy sauce glaze.")
lentil_soup = Meal.objects.create(name="Lentil Soup", category=vegan, calories=180, protein=10, carbs=25, fats=3, description="A hearty soup made with red lentils, carrots, and spices.")
chickpea_salad = Meal.objects.create(name="Chickpea Salad", category=vegan, calories=250, protein=8, carbs=30, fats=7, description="A refreshing salad with chickpeas, cucumbers, and lemon.")
baked_salmon_quinoa = Meal.objects.create(name="Baked Salmon with Quinoa", category=non_veg, calories=400, protein=35, carbs=25, fats=15, description="Oven-baked salmon served with quinoa and steamed broccoli.")
beef_stir_fry = Meal.objects.create(name="Beef Stir Fry", category=non_veg, calories=450, protein=35, carbs=15, fats=20, description="Sliced beef stir-fried with peppers, onions, and soy sauce.")

# Create predefined meal plans
low_carb_plan = PredefinedMealPlan.objects.create(category=low_carb, description="A plan for low-carb meals, ideal for weight loss.")
vegetarian_plan = PredefinedMealPlan.objects.create(category=vegetarian, description="A week of plant-based meals for vegetarians.")
vegan_plan = PredefinedMealPlan.objects.create(category=vegan, description="A fully vegan week with no animal products.")
non_veg_plan = PredefinedMealPlan.objects.create(category=non_veg, description="A balanced non-vegetarian meal plan for the week.")

# Create predefined daily meals for each plan (example for Low Carb Plan)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Monday', breakfast=grilled_chicken_salad, lunch=zucchini_noodles_pesto, dinner=grilled_chicken_salad)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Tuesday', breakfast=zucchini_noodles_pesto, lunch=grilled_chicken_salad, dinner=zucchini_noodles_pesto)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Wednesday', breakfast=grilled_chicken_salad, lunch=zucchini_noodles_pesto, dinner=grilled_chicken_salad)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Thursday', breakfast=zucchini_noodles_pesto, lunch=grilled_chicken_salad, dinner=zucchini_noodles_pesto)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Friday', breakfast=grilled_chicken_salad, lunch=zucchini_noodles_pesto, dinner=grilled_chicken_salad)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Saturday', breakfast=zucchini_noodles_pesto, lunch=grilled_chicken_salad, dinner=zucchini_noodles_pesto)
PredefinedDailyMeal.objects.create(plan=low_carb_plan, day='Sunday', breakfast=grilled_chicken_salad, lunch=zucchini_noodles_pesto, dinner=grilled_chicken_salad)

# Repeat similar data insertion for Vegetarian, Vegan, and Non-Vegetarian Plans

PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Monday', breakfast=spinach_feta_omelette, lunch=vegetable_stir_fry, dinner=spinach_feta_omelette)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Tuesday', breakfast=vegetable_stir_fry, lunch=spinach_feta_omelette, dinner=vegetable_stir_fry)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Wednesday', breakfast=spinach_feta_omelette, lunch=vegetable_stir_fry, dinner=spinach_feta_omelette)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Thursday', breakfast=vegetable_stir_fry, lunch=spinach_feta_omelette, dinner=vegetable_stir_fry)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Friday', breakfast=spinach_feta_omelette, lunch=vegetable_stir_fry, dinner=spinach_feta_omelette)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Saturday', breakfast=vegetable_stir_fry, lunch=spinach_feta_omelette, dinner=vegetable_stir_fry)
PredefinedDailyMeal.objects.create(plan=vegetarian_plan, day='Sunday', breakfast=spinach_feta_omelette, lunch=vegetable_stir_fry, dinner=spinach_feta_omelette)

# Similarly for Vegan and Non-Vegetarian plans (you can copy the above structure)
