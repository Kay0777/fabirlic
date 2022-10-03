class ExceptionHandler(Exception):
    def __init__(self, status_code, error_msg) -> None:
        self.status_code = status_code
        self.error_msg = error_msg
