class HttpUnprocessableEntityError(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422


try:
    print('Estou no bloco')
    raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as e:
    print(e.status_code)
    print(e.message)