# Random Search for Treasure on Connected Graphs

## Overview
This project is a mathematics capstone inspired by the paper *Tipsy cop and 
tipsy robber: Collisions of biased random walks on graphs* by Pamela E. Harris, 
Erik Insko, and Florian Lehner (2024). In their game, a cop and robber take 
turns moving around a graph, each with a finite chance of moving randomly. We 
asked: what if the cop moved randomly every single turn?

## The Game
We created a game where a hunter (the cop) always moves randomly, as if they 
have no idea where the treasure (the robber) is located. A few key rules:

- The treasure does not move — since the hunter moves randomly there is no 
  reason for it to try to escape, hence the name "buried treasure"
- The hunter moves to any vertex it has not already visited that is a neighbor 
  of a vertex it is currently on, or a neighbor of a vertex it has already 
  visited
- This movement guarantees a random walk of every connected graph in which 
  all vertices are visited exactly once, ensuring a finite expected capture time

## Research Question
Since the hunter always moves randomly, we focused on optimizing the starting 
positions of both the hunter and the treasure. We expected that placing the 
hunter near the center of the graph would minimize expected capture time.

## Results
Our results showed that when the treasure is placed randomly, the starting 
position of the hunter does not matter in terms of average expected capture 
time. This was a surprising and counterintuitive result.

## What the Code Does
For any given graph the code computes:
- The expected capture time for every combination of hunter and treasure 
  starting positions
- The optimal hunter placement (minimizes worst-case expected capture time)
- The worst-case hunter placement
- Average expected capture time for each starting vertex

## Technologies
- Python

## Getting Started
Clone the repository and run the script directly — no dependencies required.

```bash
git clone https://github.com/FranklinW10/GraphTheoryCapstone
cd GraphTheoryCapstone
python capstone.py
```
You can define your graph by setting the vertex list `V` and edge list `E` at the 
bottom of the script, then run:

```bash
python ProbDesityCalcFirstDraft.py
```

### Example
```python
V = [1, 2, 3, 4]
E = [(1,2), (2,3), (3,4), (1,4)]
```

## Future Work
I would like to extend this project by testing additional graph parameters 
and graph families, with the eventual goal of publishing a paper on the results.

## References
[1] Harris, P. E., Insko, E., & Lehner, F. (2024). Tipsy cop and tipsy robber: 
Collisions of biased random walks on graphs.

## Contributors
Created by Franklin Wohnoutka and Thomas Jendrejack
