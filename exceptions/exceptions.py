from fastapi import status

class ResourceExistsError(Exception):

  def __init__(self, message: str, error_code:int=status.HTTP_409_CONFLICT):
    self.error_code = error_code
    self.message = message
    super().__init__(error_code, message)