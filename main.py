import pandas as pd
from data import data
def analisis_estadistico(data):
    if not data or not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        return 'Error'

    data_frame = pd.DataFrame(data, columns=['fi'])
    data_frame['Fi'] = data_frame['fi'].cumsum()
    data_frame['ri'] = (data_frame['fi'] / data_frame['fi'].sum()).round(2)
    data_frame['Ri'] = data_frame['ri'].cumsum().round(2)
    data_frame['pi'] = (data_frame['ri'] * 100).round(2)
    data_frame['Pi'] = (data_frame['pi'].cumsum()).round(2)

    return data_frame.to_clipboard(index=False)

analisis_estadistico(data)