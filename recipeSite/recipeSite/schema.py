import datetime

import graphene
from graphene_django import DjangoObjectType

from cookbook.models import Recipe, RecipeTool, RecipeSupply, RecipeIngredient, RecipeInstruction


class RecipeType(DjangoObjectType):
    recipeIngredients = graphene.Field(lambda: IngredientType)
    def resolve_cookTime(self, info):
        return self.cookTime.total_seconds()

    def resolve_preformTime(self, info):
        return self.preformTime.total_seconds()

    def resolve_prepTime(self, info):
        return self.prepTime.total_seconds()

    def resolve_totalTime(self, info):
        return self.totalTime.total_seconds()

    def resolve_recipeIngredient(self, info):
        return self.recipeIngredients.all()

    class Meta:
        model = Recipe
        fields = ("id", "name", "recipeCategory", "recipeCuisine", "recipeYieldAmount", "recipeYieldUnits",
                  "estimatedCost", "preformTime", "prepTime", "totalTime", "author", "datePublished", "description",
                  "cookTime", "cookingMethod", "recipeIngredients")


class ToolType(DjangoObjectType):
    class Meta:
        model = RecipeTool
        fields = ("id", "item")


class SupplyType(DjangoObjectType):
    class Meta:
        model = RecipeSupply
        fields = ("id", "amount", "unit", "item", "recipe")


class IngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient
        fields = ("id", "amount", "unit", "item", "recipe")


class IngredientInputType(graphene.InputObjectType):
    amount = graphene.Int(required=True)
    unit = graphene.String()
    item = graphene.String(required=True)


class InstructionType(DjangoObjectType):
    class Meta:
        model = RecipeInstruction
        fields = ("id", "stepNumber", "instruction", "recipe")


class Query(graphene.ObjectType):
    all_recipies = graphene.List(RecipeType)
    all_tools = graphene.List(ToolType)

    def resolve_all_recipies(root, info):
        return list(Recipe.objects.all())

    def resolve_all_tools(root, info):
        return list(RecipeTool.objects.all())


class CreateRecipe(graphene.Mutation):
    class Arguments:
        cookTime = graphene.Int()
        cookingMethod = graphene.String()
        recipeCategory = graphene.String()
        recipeCuisine = graphene.String()
        recipeYieldAmount = graphene.Int()
        recipeYieldUnits = graphene.String()
        estimatedCost = graphene.Decimal()
        preformTime = graphene.Int()
        prepTime = graphene.Int()
        totalTime = graphene.Int()
        author = graphene.String()
        datePublished = graphene.Date()
        description = graphene.String()
        name = graphene.String()
        recipeIngredients = graphene.List(IngredientInputType)
    ok = graphene.Boolean()
    recipe = graphene.Field(lambda: RecipeType)

    @classmethod
    def mutate(cls, root, info, cookTime, cookingMethod, recipeCategory, recipeCuisine, recipeYieldAmount,
               recipeYieldUnits, estimatedCost, preformTime, prepTime, totalTime, author, datePublished, description,
               name, recipeIngredients):
        recipe = Recipe(cookTime=datetime.timedelta(seconds=cookTime), cookingMethod=cookingMethod,
                        recipeCategory=recipeCategory, recipeCuisine=recipeCuisine, recipeYieldAmount=recipeYieldAmount,
                        recipeYieldUnits=recipeYieldUnits, estimatedCost=estimatedCost,
                        preformTime=datetime.timedelta(seconds=preformTime),
                        prepTime=datetime.timedelta(seconds=prepTime),
                        totalTime=datetime.timedelta(seconds=totalTime), author=author, datePublished=datePublished,
                        description=description, name=name)
        recipe.save()
        for ingredient in recipeIngredients:
            recipe.recipeIngredients.create(amount=ingredient.amount, unit=ingredient.unit,
                                            item=ingredient.item)
        return CreateRecipe(ok=True, recipe=recipe)


class MyMutations(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
