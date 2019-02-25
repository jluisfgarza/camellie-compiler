# Camellie Compiler

### User Variables:

- Day
- Money
- Inventory
- Candy (quantity)
- Tacos (quantity)
- Medicine (quantity)

### Pet Variables:

- Name
- Age
- Health
- Energy
- Hunger
- Fun
- Hygiene
- Bladder
- Level (evolve at certain levels)

### User functions:

- Shop
- Turn On/Off light
- Offer food (taco)
- Offer candy
- Offer medicine
- Start new game
  - Name new pet
- Save current game
- Load game

### Pet functions

- Eat : decreases hunger
- Play : increases fun, increases money
  - Create mini game, maybe?
- Take medicine : increases health
- Bath : increases hygiene
- Poop : decreases hygiene (timed action)
- Become sick : decreases health (timed action)
- Get hungry : increases hunger (timed action)
- Age Up : increases age (timed action)
- Sleep : increases energy
- Evolve (`if age == 10 && health == MAX && fun == MAX && hunger == MIN`)
- Die : GAME OVER (`if hunger == MAX || health == MIN`)

### Other functions

- updateDay : increases day count

### Shop Variables:

- Items for sale (list?)
  - Apple : decreases hunger
  - Toy : increases fun
  - Medicine : increases health

---
## Graphics req:

## Alebrije

- Egg
- Evolution 1
- Evolucion 2
- Evolucion 3

### Spaces

- Room
- Hospital
- Park

### Items

- Taco
- Medicine
- Money
- Candy
- Poop

---

## Language

### TOKENS
- *all homework 3 tokens*
- `++`
- `--`
- `&&`
- `||`
- `!=`
- `MIN_INT`
- `MAX_INT`

### SYNTAX DIAGRAMS

### SEMANTIC CHARACTERISTICS

### FUNCIONES

---

### Useful Links

- [pico8](https://github.com/topics/pico-8)
- [pyxel](https://github.com/kitao/pyxel)
- [StayAlive.py](http://usingpython.com/dl/StayAlive.py)
