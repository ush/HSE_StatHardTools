import numpy as np

table = []

way = int(input("way (one-way - 1, two-way - 2): "))
rows = int(input("number of rows: "))
N = 0
mean = 0

if (way == 1):
    columns = int(input("number of elements in a row is constant?(# of columns - yes, 0 - no): "))
    
    for j in range(rows):
        row = []
        if (columns == 0): 
            for i in range(int(input("number of elements: "))):
                row.append(float(input()))
            table.append(row)
            N += len(row)
            print("End of row ", j + 1)
        else:
            for i in range(columns):
                row.append(float(input()))
            table.append(row)
            N += len(row)
            print("End of row ", j + 1)
    
    for j in range(rows):
        mean += np.mean(table[j])
    
    mean /= rows
    B = 0
    W = 0
    
    for j in range(rows):
        W += np.var(table[j])*len(table[j])
        B += len(table[j])*(np.mean(table[j]) - mean)**2 
    
    print("Source   DF      SS        MS       F       p-value")
    print("Factor   ", rows - 1, "  ", '%.3f'%B, " ", '%.3f'%(B/(rows - 1)), " ", '%.3f'%((B/(rows - 1))/(W/(N - rows))))
    print("Error    ", N - rows, " ", '%.3f'%W, " ", '%.3f'%(W/(N - rows)))
    print("Total    ", N - 1, " ", '%.3f'%(B + W))
    
if (way == 2):
    columns = int(input("number of columns: "))
    
    for j in range(rows):
        row = []
        for i in range(columns):
            row.append(float(input()))
        table.append(row)
        print("End of row ", j + 1)
        
    N = rows*columns
    Total_SS = 0
    Residual_SS = 0
    B_col = 0
    B_row = 0
    mean_col = 0
    
    for j in range(rows):
        for i in range(columns):
            mean += table[j][i]
    mean /= N
    
    for j in range(columns):
        for i in range(rows):
            mean_col += table[i][j]
        mean_col /= rows
        B_col += (mean_col - mean)**2
    
    for j in range(rows):
        for i in range(columns):
            Total_SS += (table[j][i] - mean)**2
        B_row += (np.mean(table[j]) - mean)**2
    
    B_col *= columns
    B_row *= rows
    Residual_SS = Total_SS - B_row - B_col
    
    F_row = ((columns - 1)*B_row)/Residual_SS
    F_col = ((rows - 1)*B_col)/Residual_SS
    
    print("Source           DF          SS             MS          F           p-value")
    print("Row factor       ", (rows - 1), "    ", '%.3f'%B_row , "     ", '%.3f'%(B_row/(rows - 1)), "  ", '%.3f'%F_row)
    print("Column factor    ", (rows - 1), "    ", '%.3f'%B_col , "   ", '%.3f'%(B_col/(columns - 1)),"", '%.3f'%F_col)
    print("Residual         ", (rows - 1)*(columns - 1), "   ", '%.3f'%Residual_SS, "  ", '%.3f'%(Residual_SS/((rows - 1)*(columns - 1))))
    print("Total            ", (rows*columns - 1), "    ", '%.3f'%Total_SS)
    
    

    
    
