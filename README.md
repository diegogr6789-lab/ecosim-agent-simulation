# EcoSim: A Live Market and Population Simulator in Python

<img src="demo.gif" width="500" alt="EcoSim Gameplay Demo">

I built this simulation using Python and Pygame to experiment with how an open economy behaves when driven by autonomous agents with distinct psychological traits. The system models a live marketplace where prices react dynamically in real time based on supply, demand, and population mobility.

## How the Simulation Works

The core of this project is a multi-agent system where citizens make independent financial choices based on their individual profiles:

* Savers: They protect their capital and only purchase goods when the local market prices fall below a certain threshold.
* Impulsive Citizens: They spend their money immediately as soon as they have liquidity, regardless of market inflation.
* Entrepreneurs: They act as market traders. They scan the map, analyze price differences between cities, calculate distance costs, and travel to maximize arbitrage profits.
* Farmers: They focus on production, generating stock and consuming a fraction of it to survive.

### Dynamic Economy Logic
Prices in each city are not static. They are computed dynamically based on a basic economic formula: price = 10 * (population / stock). If a city becomes overcrowded and goods become scarce, prices rise. If production outpaces demand, prices drop automatically.

### Routing and Pathfinding
To make the traveling entrepreneurs functional, the engine calculates trigonometric distances between urban nodes using math.hypot. This distance value is combined with a Lambda sorting function, allowing agents to weigh transportation costs against potential market profits before choosing their destination.

## Tech Stack and Architecture

* Language: Python 3
* Graphics Engine: Pygame (handles visual rendering, city node connections, and population density metrics)
* Core Logic: Native Math and Random modules for the behavioral decision trees
* Design Patterns: Developed under Object-Oriented Programming (OOP) principles, isolating the execution logic into clean modules (main.py, people.py, and ciudades.py)

---
Feel free to clone the repository, modify the economic formulas, or inject new agent profiles to see how the market reacts.

