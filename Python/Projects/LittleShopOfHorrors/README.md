
# Little Shop of Horrors

<img src='https://user-images.githubusercontent.com/72005563/177007763-4ba8fa44-3243-4d2f-8d9c-1794b01d1122.png' height=200>




# Background Info
  
This Kata is inspired by [Little Shop of Horrors](https://en.wikipedia.org/wiki/Little_Shop_of_Horrors_(film)). The film centers on a florist who discovers a mysterious carnivorous plant that feeds on human blood. The more humans the plant was fed, the more rapidly the plant would grow. 


> *"Feed me, Seymour!"*



# Task

Create a function `little_shop_of_horrors,` that takes two parameters, `"plant_food"` and `"starting_height."` `plant_food` is a `list` of human-objects, and `starting_height` is the starting height of your plant in `feet.` The function should return the `total height` of your plant in `feet` after it has been feed the list of human-objects. The output should be rounded to the nearest whole number. Your plant will grow `100 cm` for every `1 gallon` of blood it consumes from `"alive"` human-object only! Each human-object will have the following attributes, and associated datatypes:

- `is_alive`: bool  
  - `True` for alive, and `False` for dead.
- `gender`: str
  - Either `male` or `female.`
- `height`: int
  - The height of the human-object in `inches.`
- `weight`: int 
  - The weight of the human-object in `pounds.`

Use [Nadler's Formula](https://pubmed.ncbi.nlm.nih.gov/30252333/) to calculate the blood volume of each human in `liters`:

- For `Males` = 0.3669 * `height` in `meters` ** 3 + 0.03219 * `weight` in `kgs` + 0.6041
- For `Females` = 0.3561 * `height` in `meters` ** 3 + 0.03308 * `weight` in `kgs` + 0.1833


If the plants's `starting_height` is less then zero, and your returning result is less then 0, then return plant's `starting_height`.  



# Sample Data

```python
from collections import namedtuple

Food = namedtuple('FoodSource', ['is_alive', 'gender', 'height', 'weight'])

jon = Food(True, 'male', 72, 175)
jane = Food(True, 'female', 54, 120)
joe = Food(True, 'male', 63, 485)
zombie = Food(False, 'male', 52, 95)

plant_food = (jon, jane, joe, zombie)

```



# Test Sample Explanation

Analyize the `namedtuple` in  `Testcase.` As you can see, each human-object has a set of attributes.

1.   Using `Nadler's Formula`, calculate the total blood volume in `liters` of each human-object in the list who are `"alive"` only. 

```
[5.402996788698916, 2.902448321222131, 9.187835185254412]
```


2. Convert `liters` into `gallons`:

```
4.621738519200914
```

3. The plant grows `100 cm` for every `1 gallon of blood`:

```
462.1738519200914
```

4. Now, add `462.1738519200914 cm` to the plant's `starting_height` of `15 feet`, and return the result rounded to the nearest whole number: 
 
```
30
```
Therefore, after feeding, your plant grew an additional `15 feet` from it's original `starting_height,` thus the correct answer is `30.`
