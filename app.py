from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/length")


#Convert Length
def convert_length(value, fromUnit, toUnit):
    factors = {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "inch": 0.0254
    }

    value_in_meters = value * factors[fromUnit]
    converted_value = value_in_meters / factors[toUnit]
    return converted_value

@app.route("/length", methods=["GET", "POST"])
def length():
    result = None

    if request.method == "POST":
        value = request.form["value"]
        fromUnit = request.form["from_unit"]
        toUnit = request.form["to_unit"]

        if value:
            convert_length(value, fromUnit, toUnit) 
    
    return render_template("length.html", result=result)      


#Convert Weight
def convert_weight(value, fromUnit, toUnit):
    factors = {
        "Gram": 1,
        "Kilogram": 1000,
        "Pound": 453.592,
        "Ounce": 28.3495
    }

    value_in_grams = value * factors[fromUnit]
    converted_value = value_in_grams / factors[toUnit]
    return converted_value

@app.route("/weight")
def weight():
    return render_template("weight.html")



#Convert Temperature
def convert_temperature(value, fromUnit, toUnit):
    if fromUnit == toUnit:
        return value

    if fromUnit == "Celsius":
        if toUnit == "Fahrenheit":
            return (value * 9/5) + 32
        elif toUnit == "Kelvin":
            return value + 273.15
    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            return (value - 32) * 5/9
        elif toUnit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif fromUnit == "Kelvin":
        if toUnit == "Celsius":
            return value - 273.15
        elif toUnit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

app.run(debug=True)