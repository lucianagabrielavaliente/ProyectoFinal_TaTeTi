# TaTeTi
Este repositorio  proyecto final de la asignatura Ingeniería de Software.

![tateti_portada 2 0](https://user-images.githubusercontent.com/54379062/162546710-08d089f5-f515-4a0a-b6ac-ffda845e80df.jpg)

## Descripción
El mundo TaTeTi permite que dos agentes realicen jugadas en un tablero por medio de los sensores y actuadores concretos.


La arquitectura a seguir:

![diagram](https://user-images.githubusercontent.com/54379062/167011894-7b557c0e-349c-4557-8583-9a01a1fb3726.png)


## Funcionamiento

- Se le asigna un ID a los actores (X u O) de forma aleatoria y éste será la letra que van a dibujar el actor en el tablero. 
- El actor 1 realiza la primer jugada.
- Se le asigna el ID del jugador a la variable last_player.
- Se muestra el estado actual del tablero.
- El actor 2 realiza la jugada.
- Se controla si se ha realizado una jugada de victoria o se ha llegado a un empate (ya se ha dibujado en todos los casilleros del tablero).
- Se le asigna el id del jugador a la variable last_player.
- Se muestra el estado actual del tablero.
- Dependiendo del valor en la variable last_player se determinará que actor realizará la jugada.
- Las jugadas ganadoras se encuentran almacenadas en una lista, al final del turno del actor se controla si en el tablero existe una jugada ganadora.
- Al finalizar se muestra 'Tie' si se llego a un empate o el ID del actor ganador.


![diagramadeflujo](https://user-images.githubusercontent.com/54379062/162551450-89e79e1e-e2d5-4beb-b9ad-76cfbb412876.jpg)


##  Integrantes

Rebeca Benedetti, Lucía Thea, Luciana Valiente. 

#### @ Universidad Tecnológica Nacional - Facultad Regional Concepción del Uruguay

