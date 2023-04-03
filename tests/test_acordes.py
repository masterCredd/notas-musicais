from pytest import mark

from notas_musicais.acordes import wake_up


"""
Entrada:
    acorde C
    
    Esperado:
    I - III - V
    C   E     G
    {'grades': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
"""


@mark.parametrize(
    'note, tonality, expected',
    [
        ('C',  ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ]
)
def test_must_return_to_the_corresponding_notes(note, expected):
    grades, _ = wake_up(note).values()
    
    assert expected == grades
    
    
@mark.parametrize(
    'cipher, expected',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ]
)
def test_should_return_the_corresponding_degrees(cipher, expected):
    _, degrees = wake_up(cipher).values()
    
    assert expected == degrees