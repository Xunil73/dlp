import matplotlib.pyplot as plt

# 1. Daten als Listen definieren
x = [1, 2, 3, 4, 5, 6] # Gemeinsame x-Achse (optional)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [1, 4, 9, 16, 25, 36]
y3 = [6, 5, 4, 3, 2, 1]
y4 = [2, 2, 8, 4, 10, 6]

# 2. Plot erstellen
# label= dient dazu, die Legende später zu beschriften
plt.plot(x, y1, label='Linie 1', color='red', linestyle='-')
plt.plot(x, y2, label='Linie 2', color='blue', linestyle='--')
plt.plot(x, y3, label='Linie 3', color='green', linestyle=':')
plt.plot(x, y4, label='Linie 4', color='purple', linestyle='-.')

# 3. Diagramm beschriften und verschönern
plt.title('Vier Kurven in einem Plot')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.legend() # Zeigt die Legende an
plt.grid(True) # Blendet ein Gitter ein

# 4. Diagramm anzeigen
plt.show()
