"""
AAA or 3A or A3
Arrange - Act - Asserts!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises
from notas_musicais.escalas import SCALES, GRADES, scale


def test_should_work_with_lowercase_notes():
    # Arrange
    tonic = 'c'
    tonality = 'maior'
    
    # Act 
    result = scale(tonic, tonality)
    assert result


def test_should_return_an_error_saying_that_the_note_does_not_exist():
    tonic = 'X'
    tonality = 'maior'
    
    msg_error = f'Essa nota não existe, tente uma dessas {GRADES}'
    
    with raises(ValueError) as error:
        scale(tonic, tonality)
    
    assert msg_error == error.value.args[0]
        
        
def test_should_return_an_error_saying_that_the_scale_does_not_exist():
    tonic = 'c'
    tonality = 'tonality'
    
    msg_error = ('Essa scale não existe ou não foi implementada.'
                    f'Tente uma dessas {list(SCALES.keys())}')
    
    with raises(KeyError) as error:
        scale(tonic, tonality)
    
    assert msg_error == error.value.args[0]


@mark.parametrize(
    'tonic, tonality,expected',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_should_return_the_correct_grades(tonic, tonality, expected):
    result = scale(tonic, tonality)
    assert result['notas'] == expected


def must_return_the_seven_degrees():
    tonic = 'c'
    tonality = 'maior'
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    
    result = scale(tonic, tonality)
    assert result['degrees'] == expected