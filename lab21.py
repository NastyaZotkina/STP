weight,height=map(float,input().split())
def bmi(weight: float, height: float) -> float:
    return weight/(height/100)**2
def print_bmi(bmi: float):
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<25.0):
        print("Normal")
    elif(bmi>=25.0 and bmi<30.0):
        print("Overweight")
    elif(bmi>=30.0):
        print("Obesity")
    else:
        print("введены некорректные данные")
print_bmi(bmi(weight,height))