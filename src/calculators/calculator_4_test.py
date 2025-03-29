from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self,body:dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [2,2,4]})
    
    calculator_4 = Calculator4()
    response = calculator_4.calculate(mock_request)
    
    # Testar sempre o formato da responsta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 2.67
    assert response["data"]["Calculator"] == 4

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something":4})
    calculator_4 = Calculator4()

    # se tiver qualquer erro no meu processo
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    # validando se o que retornou e igual a essa mensagem
    assert str(excinfo.value) == 'body mal formatado'

