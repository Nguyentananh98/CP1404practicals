"""
Programming 2 -Practical 5
NGUYEN TAN ANH
"""

HEX_COLORS = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'AliceBlue': '#f0f8ff', 'Alizarin crimson': '#e32636',
              'Amaranth': '#e52b50', 'Amber': '#ffbf00', 'Amethyst': '#9966cc', 'AntiqueWhite': '#faebd7', 'AntiqueWhite1': '#ffefdb',
              'AntiqueWhite2': '#eedfcc'}

print(HEX_COLORS)

input_color = input('Please insert color name: ').title()

while input_color != "":
    try:
        print(f'The hex code of the color {input_color} is {HEX_COLORS[input_color]}')
    except KeyError:
        print('Invalid color name: ')
    input_color = input('Please insert color name: ').title()
