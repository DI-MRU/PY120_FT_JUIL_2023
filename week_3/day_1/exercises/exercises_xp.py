class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1=Cat("PsPsPs",3)
cat2=Cat("felix",20)
cat3=Cat("Spike",7)
 
    
def oldest_cat(cat_list):
    oldest_cat = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat
   

calculate_oldest = oldest_cat([cat1,cat2,cat3]) 
print(f"The oldest cat is {calculate_oldest.name}, and is {calculate_oldest.age} years old.")