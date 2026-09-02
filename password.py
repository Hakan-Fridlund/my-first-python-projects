"""
Du ska skriva ett program där användaren får försöka skriva in ett lösenord. Programmet ska:
Ha ett korrekt lösenord lagrat i koden t.ex. password = "hemligt"
Låta användaren försöka skriva in lösenordet flera gånger
Vanligt är 3 försök, men ibland ska du själv välja.
Hantera fel
Det betyder:
Om användaren skriver något som inte är en sträng (t.ex. trycker Enter direkt) → hantera det.
Om användaren skriver fel lösenord → ge ett tydligt felmeddelande.
Om användaren skriver rätt → avsluta direkt.
Ge ett meddelande när försöken är slut
t.ex. “Du har slut på försök.”
(I vissa versioner) använda try/except
För att fånga fel som:
tom input
avbruten input
"""


def main():
    log_in("Skriv in ditt lösenord: ")


def log_in(prompt):
    attempts = 0
    while True:
        try:
            attempt = input(prompt)
            if attempt == password:
                print("Du är inloggad")
                break
        except ValueError:
            print("felaktig input")
        else:
            attempts += 1
            if attempts >= 3:
                print("Ditt konto är låst pga för många inloggnings-försök!")
                break
            print(f"Fel lösenord, du har {3-attempts} försök kvar")


password = "Gecko"
main()
