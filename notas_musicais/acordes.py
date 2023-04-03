
from notas_musicais.escalas import GRADES, scale


def _smaller(cipher):
    note, _ = cipher.split('m')
    if '+' in cipher:
        tonic, third, fifth = triad(note, 'menor')
        grades = [tonic, third, semitone(fifth, interval=1)]
        
        degrees = ['I', 'III-', 'V+']
        
    else:
        grades = triad(note, 'menor')
        degrees = ['I', 'III-', 'V']
        
    return grades, degrees


def semitone(note, *, interval):
    pos = GRADES.index(note) + interval
    
    return GRADES[pos % 12]


def triad(note, tonality):
    degrees = (0, 2, 4)
    scale_notes, _ = scale(note, tonality).values()
    
    return [scale_notes[degree] for degree in degrees]
    

def wake_up(cipher: str) -> dict[str, list[str]]:
    """
    ->  Gera as notas de um acorde partindo de uma cifra.
    Parameters:
        cipher: Um acorde em forma de cifra
    Returns:
        Um dicionário com as notas e os graus correspondentes da escala maior
    Examples:
        >>> wake_up('C')
        {'grades': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
        >>> wake_up('Cm')
        {'grades': ['C', 'D#', 'G'], 'degrees':  ['I', 'III-', 'V']}
        >>> wake_up('C°')
        {'grades': ['C', 'D#', 'F#'], 'degrees': ['I', 'III-', 'V-']}
        >>> wake_up('C+')
        {'grades': ['C', 'E', 'G#'], 'degrees': ['I', 'III', 'V+']}
        >>> wake_up('Cm+')
        {'grades': ['C', 'D#', 'G#'], 'degrees': ['I', 'III-', 'V+']}
        
    """
    
    if 'm' in cipher:
        grades, degrees = _smaller(cipher)
    elif '°' in cipher:
        note, _ = cipher.split('°')
        tonic, third, fifth = triad(note, 'menor')
        grades = [tonic, third, semitone(fifth, interval=-1)]
        degrees = ['I', 'III-', 'V-']
    elif '+' in cipher:
        note, _ = cipher.split('+')
        tonic, third, fifth = triad(note, 'maior')
        grades = [tonic, third, semitone(fifth, interval=+1)]
        degrees = ['I', 'III', 'V+']
        
    else:
        grades = triad(cipher, 'maior')
        degrees = ['I', 'III', 'V']
        
    return {'grades': grades, 'degrees': degrees}