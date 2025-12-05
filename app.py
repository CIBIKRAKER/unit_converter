from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


#Convert Temperature
def convert_temperature(value, fromUnit, toUnit):
    if fromUnit == toUnit:
        return value

    if fromUnit == "celsius":
        if toUnit == "fahrenheit":
            return round(((value * 9/5) + 32), 2)
        elif toUnit == "kelvin":
            return round((value + 273.15),2)
    elif fromUnit == "fahrenheit":
        if toUnit == "celsius":
            return round(((value - 32) * 5/9),2)
        elif toUnit == "kelvin":
            return round(((value - 32) * 5/9 + 273.15),2)
    elif fromUnit == "kelvin":
        if toUnit == "celsius":
            return round((value - 273.15),2)
        elif toUnit == "fahrenheit":
            return round(((value - 273.15) * 9/5 + 32),2)
        
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
    return round((converted_value),2)


#Convert Weight
def convert_weight(value, fromUnit, toUnit):
    factors = {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592,
        "ounce": 28.3495
    }

    value_in_grams = value * factors[fromUnit]
    converted_value = value_in_grams / factors[toUnit]
    return round((converted_value), 2)

@app.route("/")
def index():
    return redirect("/length")

@app.route("/length", methods=["GET", "POST"])
def length():
    try:
        if request.method == "POST":
            value = float(request.form["value"])
            fromUnit = request.form["from_unit"]
            toUnit = request.form["to_unit"]
            converted_value = convert_length(value, fromUnit, toUnit)
            return render_template("result.html", 
                                   converted_value=converted_value, 
                                   value=value, 
                                   fromUnit=fromUnit, 
                                   toUnit=toUnit)
    except ValueError:
        return render_template("length.html", error="Invalid input. Please try again.")
        
    return render_template("length.html")

@app.route("/weight", methods=["GET", "POST"])
def weight():
    try:
        if request.method == "POST":
            value = float(request.form["value"])
            fromUnit = request.form["from_unit"]
            toUnit = request.form["to_unit"]
            converted_value = convert_weight(value, fromUnit, toUnit)
            return render_template("result.html", 
                                   converted_value=converted_value, 
                                   value=value, 
                                   fromUnit=fromUnit, 
                                   toUnit=toUnit)
    except ValueError:
        return render_template("weight.html", error="Invalid input. Please try again.")
        
    return render_template("weight.html")
   
@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    try:
        if request.method == "POST":
            value = float(request.form["value"])
            fromUnit = request.form["from_unit"]
            toUnit = request.form["to_unit"]
            converted_value = convert_temperature(value, fromUnit, toUnit)
            return render_template("result.html", 
                                   converted_value=converted_value, 
                                   value=value, 
                                   fromUnit=fromUnit, 
                                   toUnit=toUnit)
    except ValueError:
        return render_template("temperature.html", error="Invalid input. Please try again.")
        
    return render_template("temperature.html")

app.run(debug=True)

