
# Erstelle einfache App-Icons mit PIL
from PIL import Image, ImageDraw, ImageFont
import os

# Icon 192x192
def erstelle_icon(groesse, dateiname):
    # Erstelle ein Bild mit Farbverlauf
    img = Image.new('RGB', (groesse, groesse), color='#667eea')
    draw = ImageDraw.Draw(img)
    
    # Zeichne einen Kreis
    draw.ellipse([groesse//4, groesse//4, 3*groesse//4, 3*groesse//4], 
                 fill='#f5576c', outline='white', width=groesse//20)
    
    # Füge Text hinzu (vereinfacht, da Font möglicherweise nicht verfügbar)
    try:
        font_size = groesse // 4
        # Versuche eine Schriftart zu laden
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        # Fallback zu Standard-Font
        font = ImageFont.load_default()
    
    # Zeichne mathematisches Symbol
    text = "1+1"
    # Berechne Position für zentrierten Text (vereinfacht)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((groesse - text_width) // 2, (groesse - text_height) // 2)
    
    draw.text(position, text, fill='white', font=font)
    
    # Speichere das Bild
    img.save(dateiname, 'PNG')
    return dateiname

# Erstelle beide Icons
icon_192 = erstelle_icon(192, 'icon-192.png')
icon_512 = erstelle_icon(512, 'icon-512.png')

print(f"✓ Icons erstellt: {icon_192}, {icon_512}")
print("\n" + "="*60)
print("ALLE DATEIEN ERFOLGREICH ERSTELLT!")
print("="*60)
