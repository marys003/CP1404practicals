"""
Hex Colours
Estimate: 30 minutes
Actual:   25 minutes
"""
COLOR_CODES = {"BLACK": "000000","WHITE": "#ffffff", "ALIZARIN CRIMSON": "#e32636", "ALICEBLUE": "#f0f8ff",
               "SPANISH ORANGE": "#e86100", "VANILLA": "#f3e5ab", "PANSY PURPLE": "#78184a", "MINT": "#3eb489",
               "AQUA": "#00ffff", "BLUE": "#0000ff"}

color_name = input("Enter a color name (or blank to stop): ").upper()
while color_name != "":
    color_code = COLOR_CODES[color_name]
    print(f"Colour :  {color_name}   Code : {color_code}")
    color_name = input("Enter a color name : ").upper()
