import random # El mati lo hizo lol

jugadorJuega = True
DealerJuega = True

mesa = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
         "J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K","A"]
cartasDelJugador = []
cartasDelDealer = []
mano=[]

def repartirCartas (turno):
    cartas=random.choice(mesa)
    turno.append(cartas)
    mesa.remove(cartas)
    
    
def total(turno):
    total = 0
    facecard = ("J,Q,K")
    for cartas in turno:
        if cartas in range(1,11):
            total += cartas
        elif cartas in facecard:
            total += 10
        else:
            if total > 11:
                total += 11
            else:
                total+= 11
    return total


def revelarCartasDelDealer():
    if len(cartasDelDealer) == 2:
        return cartasDelDealer [0]
    elif len(cartasDelDealer) > 2:
        return cartasDelDealer[0], cartasDelDealer [1]
    
    
for _ in range(2):
    repartirCartas(cartasDelDealer)
    repartirCartas(cartasDelJugador)
    

while jugadorJuega or DealerJuega:
    print(f"Las cartas del Dealer son: {revelarCartasDelDealer()} Y X ")
    print(f"el Jugador tiene {cartasDelJugador} con un total de {total(cartasDelJugador)}") 
    if jugadorJuega:
        plantarseOpedir = input("1.plantarse\n2.pedir\n")
    if total(cartasDelDealer) > 16:
        DealerJuega = False
    else:
        repartirCartas(cartasDelDealer)
    if plantarseOpedir == "1":
        jugadorJuega = False
    else:
        repartirCartas(cartasDelJugador)
    if total(cartasDelJugador) >= 21:
        break
    elif total(cartasDelDealer) >=21:
        break            
            
if total (cartasDelJugador) == 21:
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print("BLACKJACK!!!")
elif total (cartasDelDealer) == 21:
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print(f"\nel Dealer obtuvo BLACKJACK!")
elif total (cartasDelJugador) > 21:
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print(f"BREAK! el Dealer gana")
elif total (cartasDelDealer) > 21:
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print("El Dealer hizo un BREAK, el jugador gana")
elif 21 - total(cartasDelDealer) < 21 - total(cartasDelJugador):
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print("el Dealer gana!")
elif 21 - total(cartasDelJugador) > - total(cartasDelDealer):
    print(f"\ntienes {cartasDelJugador} por un total de {total(cartasDelJugador)} y el Dealer tiene {cartasDelDealer} con un total de {total(cartasDelDealer)}")
    print("tu ganas")
        
          




    
 

