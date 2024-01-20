pin = 1234  # PIN predefinito per l'account
balance = 1000.0  # Saldo iniziale dell'account

# Richiede il PIN all'utente
user_pin = int(input("Inserisci il tuo PIN: "))

# Verifica il PIN dell'utente
if user_pin != pin:
    print("PIN non valido. L'accesso è stato negato.")
    exit()

# Ciclo principale del programma
while True:
    print("Benvenuto nell'ATM!")
    print("1. Visualizza saldo")
    print("2. Prelievo")
    print("3. Deposito")
    print("4. Esci")

    # Legge la scelta dell'utente
    choice = int(input("Scegli un'opzione: "))

    # Gestisce la scelta dell'utente
    if choice == 1:
        print("Il tuo saldo è:", balance, "euro")
    elif choice == 2:
        withdrawal_amount = float(input("Inserisci l'importo da prelevare: "))
        if withdrawal_amount > balance:
            print("Saldo insufficiente!")
        else:
            balance -= withdrawal_amount
            print("Hai prelevato", withdrawal_amount, "euro. Il tuo nuovo saldo è:", balance, "euro")
    elif choice == 3:
        deposit_amount = float(input("Inserisci l'importo da depositare: "))
        balance += deposit_amount
        print("Hai depositato", deposit_amount, "euro. Il tuo nuovo saldo è:", balance, "euro")
    elif choice == 4:
        print("Grazie per aver usato l'ATM!")
        exit()
    else:
        print("Scelta non valida. Riprova.")
