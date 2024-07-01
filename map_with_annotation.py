import folium

# Define the hash value
hash_value = 'etoile'

# Create a map centered on Lyon, France
map = folium.Map(location=[45.75, 4.85], zoom_start=13)

# HTML for the popup with a form to input the annotation, tickboxes, and include the hash value as a hidden input
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Marker Popup</title>
</head>
<body>
    <h4>Écrivez quelque chose :</h4>
    <form action="http://localhost:5000/save_annotation" method="post" target="hidden_iframe">
        <textarea id="text" name="text" rows="4" cols="30"></textarea><br>
        <label><input type="checkbox" name="correct" value="correct"> Correct</label><br>
        <label><input type="checkbox" name="wrong" value="wrong"> Wrong</label><br>
        <label><input type="checkbox" name="abberant" value="abberant"> Abberant</label><br>
        <input type="hidden" id="hash" name="hash" value="{hash_value}">
        <input type="submit" value="Sauvegarder">
    </form>
    <iframe name="hidden_iframe" style="display:none;"></iframe>
</body>
</html>
"""

# Add the marker to the map
folium.Marker(
    location=[45.75, 4.85],
    popup=folium.Popup(html, max_width=300)
).add_to(map)

# Save the map to an HTML file
map.save('map_with_annotation.html')
