import graphene
from graphene_django import DjangoObjectType

from recipeSite.cookbook.models import Recipe, RecipeTool, RecipeSupply, RecipeIngredient, RecipeInstruction


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = ("id", "name", "recipeCategory", "recipeCuisine", "recipeYieldAmount", "recipeYieldUnits",
                  "estimatedCost", "preformTime", "prepTime", "totalTime", "author", "datePublished", "description",
                  "cookTime")


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


class InstructionType(DjangoObjectType):
    class Meta:
        model = RecipeInstruction
        fields = ("id", "stepNumber", "instruction", "recipe")


class Query(graphene.ObjectType):
    all_recipies = graphene.List(RecipeType)
    all_tools = graphene.List(ToolType)

    def resolve_all_recipies(root, info):
        return Recipe.objects.all()

    def resolve_all_tools(root, info):
        return RecipeTool.objects.all()


schema = graphene.Schema(query=Query)