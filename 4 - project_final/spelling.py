import pandas as pd

def cols_word(n_cols: int) :
    if (n_cols % 100 > 10) and (n_cols % 100 < 20) :
        return ('колонок')
    elif (n_cols % 10 == 1) :
        return('колонка')
    elif (n_cols % 10 in [2, 3, 4]) :
        return('колонки')
    else :
        return('колонок')

def rows_word(n_rows: int) :
    if (n_rows % 100 > 10) and (n_rows % 100 < 20) :
        return ('колонок')
    elif (n_rows % 10 == 1) :
        return('строка')
    elif (n_rows % 10 in [2, 3, 4]) :
        return('строки')
    else :
        return('строк')
        
def check_table(df) :
    a0 = df.shape[0]
    a1 = df.shape[1]
    a2 = df.dropna().shape[0]
    a3 = df.drop_duplicates().shape[0]

    print(a0, rows_word(a0), "и", a1, cols_word(a1))
    print(a2, rows_word(a2), "после удаления строк, содержащих NULL")
    print(a3, rows_word(a3), "после удаления дубликатов")