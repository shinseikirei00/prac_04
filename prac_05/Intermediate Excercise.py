COLOUR_WHEEL = {"AliceBlue": "#f0f8ff",
                "AntiqueWhite": "#faebd7",
                "Beige": "#f5f5dc",
                "Black": "#000000",
                "BlanchedAlmond": "#ffe4c4",
                "BlueViolet": "#8a2be2",
                "Brown": "#a52a2a",
                "Burlywood": "#deb887",
                "CadetBlue": "#5f9ea0",
                "Chocolate": "#d2691e"}

colour_choice = str(input("Enter Required Colour"))
if colour_choice not in COLOUR_WHEEL:
    print("please select from one of the available colours")
    colour_choice = str(input("Enter Required Colour"))

print(COLOUR_WHEEL[colour_choice])
