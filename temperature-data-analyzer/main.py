import csv
from statistics import mean
import matplotlib.pyplot as plt

File = "temperature.csv"
SogliaMi = 0
SogliaMa = 35

orari =[]
temperature = []

with open(File, mode="r",encoding="utf-8") as file:
    lettore = csv.DictReader(file)
    for riga in lettore:
      riga_pulita = {k.strip(): v.strip() for k, v in riga.items() if k is not None}

      orari.append(riga_pulita["timestamp"])
      temperature.append(float(riga_pulita["temperature_c"]))

if not temperature:
    raise ValueError("il file non contiene temperature")
media = mean(temperature)
minima = min(temperature)
massima = max(temperature)

print(f"Numero di misurazioni: {len(temperature)}")
print(f"Temperatura media: {media:.1f} °C")
print(f"Temperatura minima: {minima:.1f} °C")
print(f"Temperatura massima: {massima:.1f} °C")

print("\\nValori fuori intervallo:")
for orario, valore in zip(orari, temperature):
    if valore < SogliaMi or valore > SogliaMa:
        print(f"{orario}: {valore:.1f} °C")

plt.figure(figsize=(9, 4))
plt.plot(orari, temperature, marker="o")
plt.axhline(SogliaMi, linestyle="--", label="Soglia minima")
plt.axhline(SogliaMa, linestyle="--", label="Soglia massima")
plt.title("Andamento della temperatura")
plt.xlabel("Orario")
plt.ylabel("Temperatura(°C)")
plt.legend()
plt.tight_layout()
plt.savefig("temperature_plot.png", dpi=150)
plt.show()
