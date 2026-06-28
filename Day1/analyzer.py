# ratings = [
#     2,5,1,3,3,2,3,3,2,4,3,4,4,4,4,3,4,4,3,4,1,
#     3,3,1,2,3,1,3,3,3,4,3,4,3,1,2,3,4,3,2,4,2,4,3,5,
# ]

# total = 0

# for rating in ratings:
#     total = total + rating

# average = total / len(ratings)

# print("Average confidence level in HTML & CSS is ", average)

# # Your assignement: Extract Data from JS.txt file 

# js_ratings = [
#     1,4,1,3,3,1,3,1,2,4,3,2,3,4,2,3,2,3,1,
#     1,1,1,1,1,2,1,1,2,2,1,3,1,3,3,1,2,1,2,3,1,2,1,3,1,1,
# ]

# total_js = 0
# for ratingjs in js_ratings:
#     total_js = total_js + ratingjs

# average_js = total_js/ len(js_ratings)
# print("Average confidence level in JS is ", average_js)


# def average(ratings):
#     total = 0
#     for rating in ratings:
#         total = total + rating
#     average = total / len(ratings)
#     return average
# html_ratings = [
#     2,5,1,3,3,2,3,3,2,4,3,4,4,4,4,3,4,4,3,4,1,
#     3,3,1,2,3,1,3,3,3,4,3,4,3,1,2,3,4,3,2,4,2,4,3,5,
# ]


# print(average(html_ratings))
# #Html average :3.0
# #js average :1.99


# arr = [ 1,4,1,3,3,1,3,1,2,4,3,2,3,4,2,3,2,3,1,
#      1,1,1,1,1,2,1,1,2,2,1,3,1,3,3,1,2,1,2,3,1,2,1,3,1,1, ]
# freq = {}

# for item in arr:
#     if item in freq:
#         freq[item]+= 1
#     else:
#         freq[item] = 1

# print(freq)


arr = [
    "BIT",
    "BIT",
    "BIT",
    "Engineering",
    "Engineering",
    "CSIT",
    "CSIT",
    "CSIT",
    "BIT",
    "BIT",
    "BIT",
    "BIT",
    "BCA",
    "BCA",
    "BCA",
    "BCA",
    "CSIT",
    "CSIT",
    "CSIT",
    "Engineering",
    "Engineering",
    "CSIT",
    "Engineering",
    "Engineering",
    "Engineering",
    "Engineering",
    "BCA",
    "BIT",
    "Engineering",
    "Engineering",
    "Engineering",
    "BIT",
    "Engineering",
    "Engineering",
    "BCA",
    "Engineering",
    "Engineering",
    "BIT",
    "graduate",
    "Engineering",
    "BIM",
    "BIM",
    "Engineering",
    "High School",
    "Engineering",
]

freq = {}

for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)