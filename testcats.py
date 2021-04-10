from cats import cat

cat1 = cat("Барон", "мальчик", 2)
cat2 = cat("Сэм", "мальчик", 2)

print(cat1.get_name(), cat1.get_sex(), cat1.get_age())
print(cat2.get_name(), cat2.get_sex(), cat2.get_age())