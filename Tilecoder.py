import math

numTilings = 8
tiles = 41  
numTiles = numTilings*tiles*tiles*tiles
    
def tilecode(in1,in2,in3,tileIndices):  
    
    step_x = (300.0/(tiles-1))
    step_y = (380.0/(tiles-1))
    step_z = (380.0/(tiles-1))
    
    shift_x = (step_x/numTilings)
    shift_y = (step_y/numTilings)
    shift_z = (step_z/numTilings)
    
    x_cord = math.floor(in1/step_x)
    y_cord = math.floor(in2/step_y)
    z_cord = math.floor(in3/step_z)
    
    tileIndices[0] = (tiles*tiles*z_cord + tiles*y_cord + x_cord)
    
    for i in range(numTilings-1):
        in1 = in1 + (shift_x)
        in2 = in2 + (shift_y)
        in3 = in3 + (shift_z)
        x_cord = math.floor(in1/step_x)
        y_cord = math.floor(in2/step_y)
        z_cord = math.floor(in3/step_z)
        
        tileIndices[i+1] = (tiles*tiles*z_cord + tiles*y_cord + x_cord + (tiles*tiles*tiles)*(i+1))
        
    
def printTileCoderIndices(in1,in2,in3):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,in3,tileIndices)
    print 'Tile indices for input (',in1,',',in2,',',in3,') are : ', tileIndices

#printTileCoderIndices(300,250,260)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)