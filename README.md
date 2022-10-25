# EvolutionaryAerofoils
This project uses an evolutionary algorithm to optimise the geomety of a 2-D aerofoil

# Fitness
To evaluate the 'fitness' of a given aerofoil, an xfoil simulation is carried out to generate a polar for the xfoil
The max lift to drag ratio is then estimated from this polar and used to determine fitness.
Xfoil is a panel solver, a type of 2-D inviscid CFD software: https://web.mit.edu/drela/Public/web/xfoil/

# Genetic Operations
Currently only mutation is implemented (I'm intending to add crossover in future)
This works by randomly selecting a coordinates and adjusting it (in the x-axis) by a small amount
It's 2 nearest neighbors on either side are also adjusted slightly for smoothness

# Running
TODO - REQUIRMENTS.TXT
It is necessary to specify an initial population of aerofoils. Examples can be found here: https://m-selig.ae.illinois.edu/ads/coord_database.html
