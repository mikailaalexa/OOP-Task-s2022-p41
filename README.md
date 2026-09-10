# OOP-Task-s2022-p41
CIE A-level Computer Science task on OOP concepts from s2022-p41. 

## 🎮 Project Focus: Object-Oriented Game Mechanics (CIE 9618 June 2022)

This project contains the implementation of a gaming mechanic involving destructible game objects. It demonstrates object instantiation, state mutation via private tracking fields, and the simulation of an interactive combat round using standalone global functions.

### 🧠 Core Computational Concepts Implemented:
* **Object Encapsulation:** Declared a `Balloon` class featuring private state tracking fields (`Health`, `Colour`, `DefenceItem`) to prevent direct external variable tampering.
* **State Mutators & Accessors:** Created precise class methods to handle internal data changes, such as `ChangeHealth()` for taking damage/healing, and `CheckHealth()` to dynamically flag lifecycle status.
* **Passing Objects as Parameters:** Structured a global function `Defend()` that accepts a reference to a custom `Balloon` object, demonstrating how standalone software routines interact directly with active class objects.
* **Data Flow & Object Modification:** Handled user terminal inputs within functions to subtract health, output status fields dynamically, and return modified object states back to the main game runtime.
* **Driver Testing Logic:** Created a main module script to automate balloon spawning using specific parameters ("Shield", "Red") and execute game defense rounds with test integer variables.
