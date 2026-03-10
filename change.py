import re
import xml.etree.ElementTree as ET

input_svg = "2.svg"
output_svg = "2ok.svg"

tree = ET.parse(input_svg)
root = tree.getroot()

pattern = re.compile(r'(.+)__([A-Za-z_]+)_$')

for g in root.iter():
    name = g.attrib.get("name")
    if not name:
        continue

    match = pattern.match(name)
    if match:
        territory = name
        country = match.group(2)

        g.set("territory", territory)
        g.set("name", country)

tree.write(output_svg, encoding="utf-8", xml_declaration=True)

print("SVG actualizado guardado en:", output_svg)