# Twenty-One game

This is an **individual Python project** where I created a console version of the card game **Tjugoett (Blackjack)**.  
The program is fully written in **Python**, following an object-oriented structure with two main classes:  
`Deck` and `Tjugoett`.

## Om Spelet

Spelet är en digital version av klassiska **Tjugoett (Blackjack)** där spelaren möter en dealer.  
Korten dras slumpmässigt från en kortlek på 52 kort som återställs mellan varje spelrunda.  
Spelet körs helt i terminalen.

## Funktioner

- Fullständig kortlek med 52 kort  
- Slumpmässig kortdragning  
- Möjlighet att välja ess-värde (1 eller 11)  
- Dealern drar kort automatiskt tills summan ≥ 17  
- Kontroll av vinst, förlust och oavgjort  
- Möjlighet att spela flera rundor  
- Inputhantering med **pyinputplus**  

## Krav
- **Python 3.11+**
- Installera biblioteket `pyinputplus` med:
```bash
pip install pyinputplus
```

## Kör applicationen

Starta spelet gemon att köra:
```bash
python TjugoEtt.py
```
När programmet startas visas:
Welcome to Twenty-One! Do you want to play? Yes/No
Följ instruktionerna i terminal för att spela.

## Regler för spelet

1. Klädda kort (Knekt, Dam, Kung) har ett värde av *10*.

2. Ess kan ha antingen värdet 1 eller 11: a. Spelaren väljer värdet på esset. b. För dealern (datorn) har esset värdet __*1*__ om summan är större än 10, eller __*11*__ om summan är 10 eller mindre.

3. Dealern och spelaren drar kort från _samma_ kortlek.

4. När ett kort dras, tas det bort så att det inte kan visas igen.

5. Om spelaren får 21 eller över 21 avslutas spelet och dealern spelar inte.

6. Om spelaren och dealern har samma summa (under 21), vinner dealern.

7. Om dealern får 21 vinner dealern. Om dealern går över 21 vinner spelaren.

Detta projekt och README skapades av **AmyPap**.

