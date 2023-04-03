from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_scale_cli_should_return_0_to_stdout():
    result = runner.invoke(app, ['scale'])
    assert result.exit_code == 0
    

@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_scale_should_contain_the_grades_in_the_answer(note):
    result = runner.invoke(app, ['scale'])
    assert note in result.stdout
    

@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_cli_scale_should_contain_the_grades_in_the_answer_fa(note):
    result = runner.invoke(app,  ['scale', 'F'])
    assert note in result.stdout
    
    
@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_cli_scale_must_contain_all_degrees(degree):
    result = runner.invoke(app, ['scale', 'F'])
    assert degree in result.stdout
    
    
@mark.parametrize('note', ['C', 'E', 'G'])
def test_cli_wake_up_should_contain_the_grades_in_the_answer(note):
    result = runner.invoke(app, ['wake_up'])
    assert note in result.stdout
    
    
@mark.parametrize('degree', ['I', 'III', 'V'])
def test_cli_wake_up_must_contain_all_degrees(degree):
    result = runner.invoke(app, ['scale', 'F'])
    assert degree in result.stdout