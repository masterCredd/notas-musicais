
GRADES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def scale(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    ->  Gera uma scale a partir de uma tonic e uma tonality
    Parameters:
        tonic: note que será tonic da scale
        tonality: tonality da scale
    Returns:
        Um dicionario com as GRADES e os degrees
    Raises:
        ValueError: Caso a tonic não seja uma note valida.
        KeyError: Caso a scale não exista ou não tenha sido implementada.
    Examples:
        >>> scale('C', 'maior')
            {'grades': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'] }
        >>> scale('a', 'menor')
            {'grades': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'] }
    """
    tonic = tonic.upper()
    
    try:
        breaks = SCALES[tonality]
        tonic_pos = GRADES.index(tonic)
    except ValueError:
        raise ValueError(f'Essa note não existe, tente uma dessas {GRADES}')
    except KeyError:
        raise KeyError('Essa scale não existe ou não foi implementada.'
            f'Tente uma dessas {list(SCALES.keys())}')
    temp = []
    
    for interval in breaks:
        note = (tonic_pos + interval) % 12
        temp.append(GRADES[note])

    return {'grades': temp,
            'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
