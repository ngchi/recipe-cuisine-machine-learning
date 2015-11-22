import json
from pprint import pprint
from collections import defaultdict
from ingredients import normalize_ingredient_name


class Preprocess:
    cuisines = defaultdict(list)
    cuisines_set = set()
    ingredient_list = defaultdict(list)
    ingredient_set = set()
    data = []

    def __init__(self):
        self.load_data()

    def parseData(self, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
            return data

    def load_data(self):
        default_data_dir = "data/train.json"
        self.data = self.parseData(default_data_dir)
        for datum in self.data:
            cuisine = datum['cuisine'].lower()
            self.cuisines[cuisine].append(datum)
            self.cuisines_set.add(cuisine)
            ingredients = datum['ingredients']
            for ingredient in ingredients:
                ingredient = ingredient.lower()
                self.ingredient_list[ingredient].append(datum)
                self.ingredient_set.add(ingredient)

    def print_info(self):
        print "Number of recipes:", len(self.data)

        cuisine_count = []
        for cuisine in self.cuisines_set:
            cuisine_count.append((cuisine, len(self.cuisines[cuisine])))
        cuisine_count.sort(key=lambda tup: tup[1])
        for (cuisine, count) in cuisine_count:
            print cuisine.title(), count

        ingredient_count = []
        for ingredient in self.ingredient_set:
            ingredient_count.append((ingredient, len(self.ingredient_list[ingredient])))
        print len(ingredient_count), "different kinds of ingredients"

        ingredient_count.sort(key=lambda tup: tup[1])
        for i in range(0, 25):
            print ingredient_count[i][0], ingredient_count[i][1]

        ingredient_count.reverse()
        for i in range(0, 25):
            print ingredient_count[i][0], ingredient_count[i][1]

