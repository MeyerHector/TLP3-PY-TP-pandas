import pandas as pd
from data import data
def analisis_estadistico(data):
    #Manejo de errores, primero verifica si hay data, luego utiliza isinstance() para verificar la instancia de data si es una lista o no, para despues verificar en toda la data y hacer una iteracion por cada valor en la lista, si se puede transformar en int, sino retorna "Error"
    if not data or not isinstance(data, list) or not all(isinstance(i, (int)) for i in data):
        return 'Error'
    #Crea el dataframe con la function, pasando como parametros data y estableciendo la columna como 'fi'
    data_frame = pd.DataFrame(data, columns=['fi'])
    #Calculos para obtener el analisis estadistico basico con sus operaciones correspondientes
    data_frame['Fi'] = data_frame['fi'].cumsum()
    data_frame['ri'] = (data_frame['fi'] / data_frame['fi'].sum()).round(2)
    data_frame['Ri'] = data_frame['ri'].cumsum().round(2)
    data_frame['pi'] = (data_frame['ri'] * 100).round(2)
    data_frame['Pi'] = (data_frame['pi'].cumsum()).round(2)
    
    #Retorna el data_frame modificado y lo pega en el portapapeles sin index
    return data_frame.to_clipboard(index=False)

#Ejecucion de la funcion
analisis_estadistico(data)