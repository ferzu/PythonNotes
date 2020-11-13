# 1. Using zip() ********************************************************************************************
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
points = list(zip(labels, x_coord, y_coord, z_coord))
for point in points
    point_i = list(point)
    print (str(point_i[0]) +": " + str(point_i[1]) +", " + str(point_i[2]) + ", " + str(point_i[3]))



# 2. Use zip to create a dictionary cast that uses names as keys and heights as values. *************************
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = {}
for data in zip(cast_names, cast_heights):
    cast[data[0]] = data[1]
print(cast)



# 3. Unzip the cast tuple into two names and heights tuples ******************************************************
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)



# 4. ****************************************************************************************************************
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)



# 5. ******************************************************************************************************************
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i, name in enumerate(zip(cast,heights)):
    print( i, name)








# Solutions: ***********************************************************************************************************

# 1. uses the asterisc in format to unpack the tuple!
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
for point in points:
    print(point)


#2.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = dict(zip(cast_names, cast_heights))
print(cast)


#3.
names, heights = zip(*cast)
print(names)
print(heights)


#4.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)


# 5. using enumerate you have an index to access the iterables
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])
print(cast)
