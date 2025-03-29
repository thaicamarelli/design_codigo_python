from flask import request as FlaskRequest
from errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self,request: FlaskRequest): # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        calc_result = self.__calc_average(input_data)
        response = self.__format_response(calc_result)

        return response
    
    def __validate_body(self, body: dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        if not isinstance(body['numbers'], list):
            raise HttpUnprocessableEntityError("body precisa ser uma lista")
        
        input_data = body["numbers"]
        return input_data
        
    def __calc_average(self, numbers: list[float]) -> float:
        average = sum(numbers) / len(numbers)
        return average
        
    def __format_response(self, calc_result: float) -> dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(calc_result, 2)
            }
        }
    