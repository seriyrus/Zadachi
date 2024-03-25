def print_car_details(make="unknown", model = "unknown", year= -1):
    info  = f"Марка автомобиля: {make}\nМодель автомобиля: {model}\nГод выпуска автомобиля: {year}"
    print(info) 

print_car_details("Mazda", "6", 2020)