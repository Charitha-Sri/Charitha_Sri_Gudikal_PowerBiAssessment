#DAY1
"""
inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]


1.)calculate the TotalRevenue
2.)List Low stock item if stock is less than 5
3.)calculte the categorywise Revenue
"""

inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
#1.
rev=0
for row in inventory:
    rev+=row[2]*row[3]
print(rev)

"""
OUTPUT:
669.0
"""
#2.
for row in inventory:
    if row[4] < 5:
        print(f'The name {row[0]} and category {row[1]}')
"""
OUTPUT:
The name Cheddar and category Dairy
The name Baguette and category Bakery
The name Croissant and category Bakery
"""
#3.
rev1=0
cat_revenue={}
for row in inventory:
    cat=row[1]
    rev1=row[2]*row[3]
    if cat in cat_revenue:
        cat_revenue[cat]+=rev1
    else:
        cat_revenue[cat]=rev1

for category,total_revenue in cat_revenue.items():
    print(f'The Category is {category} and the Total revenue is ${total_revenue:.2f}')
"""
OUTPUT:
The Category is Fruit and the Total revenue is $228.00
The Category is Vegetable and the Total revenue is $109.00
The Category is Dairy and the Total revenue is $150.00
The Category is Bakery and the Total revenue is $182.00
"""