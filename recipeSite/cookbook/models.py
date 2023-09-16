from django.db import models

# https://schema.org/NutritionInformation
# class NutritionInformation(models.Model):

# class RestrictedDiet(models.Model):


# https://schema.org/Recipe
class Recipe(models.Model):
    # From Recipe
    cookTime = models.DurationField()
    cookingMethod = models.TextField()
    # nutrition = models.OneToOneField(NutritionInformation, on_delete=models.CASCADE)
    recipeCategory = models.TextField()
    recipeCuisine = models.TextField()
    recipeYieldAmount = models.IntegerField()
    recipeYieldUnits = models.TextField()
    # restrictedDiet = models.ManyToManyField(RestrictedDiet)
    # From HowTo
    estimatedCost = models.DecimalField(max_digits=10, decimal_places=2)
    preformTime = models.DurationField()
    prepTime = models.DurationField()
    totalTime = models.DurationField()
    author = models.TextField()
    datePublished = models.DateField()
    description = models.TextField()
    name = models.CharField(max_length=100)

    def tools(self):
        return self.recipetool_set

    def __str__(self):
        return self.name

class RecipeInstruction(models.Model):
    stepNumber = models.PositiveIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stepNumber) + self.instruction.__str__()


class RecipeIngredient(models.Model):
    amount = models.IntegerField()
    unit = models.TextField(blank=True, null=True)
    item = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name="recipeIngredients", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount) + self.unit.__str__() + self.item.__str__()


class RecipeSupply(models.Model):
    amount = models.IntegerField()
    unit = models.TextField()
    item = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount) + self.unit.__str__() + self.item.__str__()


class RecipeTool(models.Model):
    item = models.TextField()
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.item
