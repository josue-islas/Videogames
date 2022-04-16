import pandas as pd


def top_frame(genre, gk, column_to_explore, textt = 'Countries', rango = 5):
    '''Disponible Genres:
    Shooter, Misc, Action, Sports, Fighting, Puzzle, Racing, Platform, Simulation, Adventure, }
    Role-Playing,Strategy'''

    gk_genre = gk.loc[genre].sort_values(by='Global_Sales', ascending=False).reset_index()
    others = {column_to_explore:f'Other {textt} +{len(gk_genre.iloc[rango:,1])}', 'Global_Sales':gk_genre.iloc[rango:,1].sum()}
    gk_top = gk_genre.iloc[:rango]
    gk_top = gk_top.append(others, ignore_index=True)
    return gk_top

def indexar_variables(df):
    '''Función que toma un DataFrame y retorna un nuevo DataFrame con cada una
    de las variables numericas indexadas.
    
    El método consiste en calcular el máximo local de cada variable (columna del df)
    para posteriormente dividir cada observación entre el máximo local.
    
    Resulta especialmente útil para hacer homogenea la información'''
    maximos = df.max()
    i = 0
    df_indexado = pd.DataFrame()
    for column in df:
        df_indexado[f'{column}'] = df[column]/maximos[i]
        i += 1
    df_indexado.index = pd.to_datetime(df_indexado.index, errors='coerce')
    return df_indexado