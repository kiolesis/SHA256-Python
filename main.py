# Kiolesis
# https://www.youtube.com/watch?v=-lefbawmaFk
import os # Import OS
import hashlib # Import HASHLIB

print("Narzędzie Secure Hash Algorithm 256") # Nazwij swój program dowolną nazwą, niech to nie będzie podobne do czegoś powszechnego
print("") # Wolna linijka tekstu
print("Hashowanie wartości w SHA256") # Informacja dla użytkownika o funkcji programu
zmiennahash = input(":") # Przyjmowanie danych od użytkownika

print(hashlib.sha256(zmiennahash.encode('utf-8')).hexdigest()) # Wyprintuj zmiennahash, ale użyj hashlib w celu zahashowania sha256.
os.system("pause>>nul") # Opcjonalny kod tak na prawdę, jeśli jednak korzystasz z programu z poziomu linii poleceń, to zostaw ten kod.
os.system("exit") # Opcjonalnykod tak na prawdę tjw.
