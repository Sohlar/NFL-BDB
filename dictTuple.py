import csv
def readDictTuple(filepath):

    with open(filepath, 'r') as f:

        reader = csv.DictReader(f)

        data = {}

        for row in reader:
            data[(row['playid'], row['playerid'], row['frameid'])] = {
                'x': row['x']
                'y': row['y']
                'direction': row['direction']
                'degree': row['o']
            }

def iterDict():

    for key in data:
    playid, playerid, frameid = key
    x = data[key]['x']
    y = data[key]['y']
    direction = data[key]['direction']
    degree_of_rotation = data[key]['degree of rotation']

    # Do something with the data for each frame
    print(f'Play ID: {playid}')
    print(f'Player ID: {playerid}')
    print(f'Frame ID: {frameid}')
    print(f'X: {x}')
    print(f'Y: {y}')
    print(f'Direction: {direction}')
    print(f'Degree of rotation: {degree_of_rotation}')

