import datetime

import graphene
from graphene_django import DjangoObjectType

from cookbook.models import Recipe, RecipeTool, RecipeSupply, RecipeIngredient, RecipeInstruction


class IngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient
        fields = ("id", "amount", "unit", "item", "recipe")


class InstructionType(DjangoObjectType):
    class Meta:
        model = RecipeInstruction
        fields = ("id", "stepNumber", "instruction", "recipe")


class SupplyType(DjangoObjectType):
    class Meta:
        model = RecipeSupply
        fields = ("id", "amount", "unit", "item", "recipe")


class RecipeType(DjangoObjectType):
    recipeIngredients = graphene.List(IngredientType)
    recipeInstructions = graphene.List(InstructionType)
    recipeSupplies = graphene.List(SupplyType)

    def resolve_cookTime(self, info):
        return self.cookTime.total_seconds()

    def resolve_preformTime(self, info):
        return self.preformTime.total_seconds()

    def resolve_prepTime(self, info):
        return self.prepTime.total_seconds()

    def resolve_totalTime(self, info):
        return self.totalTime.total_seconds()

    def resolve_recipeIngredients(self, info):
        return list(self.recipeIngredients.all())

    def resolve_recipeInstructions(self, info):
        return list(self.recipeInstructions.all())

    def resolve_recipeSupplies(self, info):
        return list(self.recipeSupplies.all())

    def resolve_toolsUsed(self, info):
        return list(self.toolsUsed.all())

    class Meta:
        model = Recipe
        fields = ("id", "name", "recipeCategory", "recipeCuisine", "recipeYieldAmount", "recipeYieldUnits",
                  "estimatedCost", "preformTime", "prepTime", "totalTime", "author", "datePublished", "description",
                  "cookTime", "cookingMethod", "recipeIngredients", "recipeInstructions", "recipeSupplies", "toolsUsed")


class ToolType(DjangoObjectType):
    def resolve_usedInRecipe(self, info):
        return list(self.usedInRecipe.all())
    class Meta:
        model = RecipeTool
        fields = ("id", "item", "usedInRecipe")


class ToolInputType(graphene.InputObjectType):
    item = graphene.String()


class IngredientInputType(graphene.InputObjectType):
    amount = graphene.Int(required=True)
    unit = graphene.String()
    item = graphene.String(required=True)


class InstructionInputType(graphene.InputObjectType):
    stepNumber = graphene.Int(required=True)
    instruction = graphene.String(required=True)


class SupplyInputType(graphene.InputObjectType):
    amount = graphene.Int(required=True)
    unit = graphene.String()
    item = graphene.String(required=True)


class Query(graphene.ObjectType):
    all_recipies = graphene.List(RecipeType)
    all_tools = graphene.List(ToolType)

    def resolve_all_recipies(root, info):
        return list(Recipe.objects.all())

    def resolve_all_tools(root, info):
        return list(RecipeTool.objects.all())


class EditRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
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
        recipeInstructions = graphene.List(InstructionInputType)
        recipeSupplies = graphene.List(SupplyInputType)
        toolsUsed = graphene.List(ToolInputType)
    ok = graphene.Boolean()
    recipe = graphene.Field(lambda: RecipeType)

    @classmethod
    def mutate(cls, root, info, id, cookTime, cookingMethod, recipeCategory, recipeCuisine, recipeYieldAmount,
               recipeYieldUnits, estimatedCost, preformTime, prepTime, totalTime, author, datePublished, description,
               name, recipeIngredients, recipeInstructions, recipeSupplies, toolsUsed):
        recipe = Recipe.objects.get(id=id)
        recipe.cookTime = datetime.timedelta(seconds=cookTime)
        recipe.cookingMethod = cookingMethod
        recipe.recipeCategory = recipeCategory
        recipe.recipeCuisine = recipeCuisine
        recipe.recipeYieldAmount = recipeYieldAmount
        recipe.recipeYieldUnits = recipeYieldUnits
        recipe.estimatedCost = estimatedCost
        recipe.preformTime = datetime.timedelta(seconds=preformTime)
        recipe.prepTime = datetime.timedelta(seconds=prepTime)
        recipe.totalTime = datetime.timedelta(seconds=totalTime)
        recipe.author = author
        recipe.datePublished = datePublished
        recipe.description = description
        recipe.name = name
        recipe.recipeIngredients.all().delete()
        for ingredient in recipeIngredients:
            recipe.recipeIngredients.create(amount=ingredient.amount, unit=ingredient.unit,
                                            item=ingredient.item)
        recipe.recipeInstructions.all().delete()
        for instruction in recipeInstructions:
            recipe.recipeInstructions.create(stepNumber=instruction.stepNumber, instruction=instruction.instruction)
        recipe.recipeSupplies.all().delete()
        for supply in recipeSupplies:
            recipe.recipeSupplies.create(amount=supply.amount, unit=supply.unit, item=supply.item)
        recipe.toolsUsed.clear()
        for tool in toolsUsed:
            foundTool = RecipeTool.objects.filter(item=tool.item)
            if foundTool.count() == 0:
                recipe.toolsUsed.create(item=tool.item)
            elif foundTool.count() == 1:
                recipe.toolsUsed.add(foundTool.get(item=tool.item))
        recipe.save()
        return EditRecipe(ok=True, recipe=recipe)


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
        recipeInstructions = graphene.List(InstructionInputType)
        recipeSupplies = graphene.List(SupplyInputType)
        toolsUsed = graphene.List(ToolInputType)
    ok = graphene.Boolean()
    recipe = graphene.Field(lambda: RecipeType)

    @classmethod
    def mutate(cls, root, info, cookTime, cookingMethod, recipeCategory, recipeCuisine, recipeYieldAmount,
               recipeYieldUnits, estimatedCost, preformTime, prepTime, totalTime, author, datePublished, description,
               name, recipeIngredients, recipeInstructions, recipeSupplies, toolsUsed):
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
        for instruction in recipeInstructions:
            recipe.recipeInstructions.create(stepNumber=instruction.stepNumber, instruction=instruction.instruction)
        for supply in recipeSupplies:
            recipe.recipeSupplies.create(amount=supply.amount, unit=supply.unit, item=supply.item)
        for tool in toolsUsed:
            foundTool = RecipeTool.objects.filter(item=tool.item)
            if foundTool.count() == 0:
                recipe.toolsUsed.create(item=tool.item)
            elif foundTool.count() == 1:
                recipe.toolsUsed.add(foundTool.get(item=tool.item))
        return CreateRecipe(ok=True, recipe=recipe)


class DeleteRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        Recipe.objects.get(id=id).delete()
        return DeleteRecipe(ok=True)



class MyMutations(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()
    edit_recipe = EditRecipe.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
