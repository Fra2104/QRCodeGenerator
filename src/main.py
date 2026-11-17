
import qrcode
from pathlib import Path


def salva_qr(contenuto):
    """Genera e salva un QR Code."""
    nome_file = input(
        "Inserisci il nome del file per salvare il QR Code: "
    ).strip()

    if not nome_file:
        print("Errore: il nome del file non può essere vuoto.")
        return

    percorso = Path(nome_file).with_suffix(".png")

    try:
        img = qrcode.make(contenuto)
        img.save(percorso)
        print(f"\nQR Code generato e salvato come: {percorso}")

    except (OSError, ValueError) as errore:
        print(f"Errore durante il salvataggio: {errore}")


def genera_testo():
    testo = input("Inserisci il link o il testo: ").strip()

    if testo:
        salva_qr(testo)
    else:
        print("Il testo non può essere vuoto.")


def genera_vcard():
    nome = input("Inserisci il nome: ").strip()
    cognome = input("Inserisci il cognome: ").strip()
    telefono = input("Inserisci il numero di telefono: ").strip()
    email = input("Inserisci l'email: ").strip()

    if not nome or not cognome:
        print("Nome e cognome sono obbligatori.")
        return

    vcard = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{cognome};{nome};;;\n"
        f"FN:{nome} {cognome}\n"
        f"TEL;TYPE=CELL:{telefono}\n"
        f"EMAIL:{email}\n"
        "END:VCARD"
    )

    salva_qr(vcard)


def genera_wifi():
    ssid = input("Inserisci il nome della rete Wi-Fi (SSID): ").strip()
    password = input("Inserisci la password Wi-Fi: ")

    if not ssid:
        print("Il nome della rete non può essere vuoto.")
        return

    # Escape dei caratteri speciali del formato Wi-Fi QR
    def escape_wifi(valore):
        for carattere in ("\\", ";", ",", ":", '"'):
            valore = valore.replace(carattere, "\\" + carattere)
        return valore

    wifi = (
        f"WIFI:T:WPA;"
        f"S:{escape_wifi(ssid)};"
        f"P:{escape_wifi(password)};;"
    )

    salva_qr(wifi)


def main():
    while True:
        print("\n================================")
        print("   BENVENUTO NEL QR GENERATOR")
        print("================================")
        print("1. Link o testo")
        print("2. Biglietto da visita (vCard)")
        print("3. Wi-Fi")
        print("4. Esci")

        scelta = input("\nScegli un'opzione (1-4): ").strip()

        if scelta == "1":
            genera_testo()

        elif scelta == "2":
            genera_vcard()

        elif scelta == "3":
            genera_wifi()

        elif scelta == "4":
            print("\nUscita dal programma. Arrivederci!")
            break

        else:
            print("\nScelta non valida. Riprova.")


if __name__ == "__main__":
    main()
