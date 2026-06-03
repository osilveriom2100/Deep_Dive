# conditions
# if, elif, else
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")
# nested conditions
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")   

# expresiones condicionales (ternary operator)
# la sintaxis es: value_if_true if condition else value_if_false
# es una forma concisa de escribir una expresión condicional en una sola línea, lo que puede mejorar la legibilidad del código en casos simples.
is_raining = True
weather = "rainy" if is_raining else "sunny"
print(f"The weather is {weather}.")