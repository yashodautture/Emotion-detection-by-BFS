# Emotion-detection-by-BFS
The "Emotion Detectection" Python class is designed to analyse binary matrices representing facial expressions and classify them into one of four emotions: "Happy," "Sad," "Neutral," or "None" The code reads the binary matrix data from an input file named txt file and then processes it to make emotion predictions. 
The class leverages a breadth-first search (BFS) algorithm to identify connected
regions of "1s" within the binary matrix, representing facial features. These
connected regions are stored in a dictionary called "visited nodes," where each
entry consists of the (x, y) coordinates of a visited node. The BFS traversal
explores the matrix, ensuring that each node is visited only once.
The classification of emotions is based on specific criteria applied to the
arrangement of nodes in the "visited nodes" dictionary. The code first checks if
all nodes share the same row; if so, it classifies the emotion as "Neutral."
Otherwise, it examines the arrangement of nodes to distinguish between
"Happy" and "Sad" emotions. If the nodes are arranged vertically, it's "Sad,"
while a horizontal arrangement signifies "Happy." If none of these conditions
are met, the emotion is labelled as "None." 
