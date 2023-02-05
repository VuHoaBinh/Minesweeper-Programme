import global_vars as g




def neighbours(i, j):
    Cells = []
    for (x, y) in [ (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(g.HEIGHT) and y in range(g.WIDTH):
            Cells.append((x, y))
    return Cells

