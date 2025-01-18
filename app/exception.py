from fastapi import HTTPException, status

class Exceptions:
    
    @staticmethod
    def exception_404(details: str = ''):
        details = "Not Found" if not details else details
        return HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=details)
    
    @staticmethod
    def exception_400(details: str = ""):
        details = "Payload Issue" if not details else details
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=details)
    
    @staticmethod
    def exception_401(details: str = ""):
        details = "Invalid Credentials" if not details else details
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=details)
    
    @staticmethod
    def exception_409(details: str = ""):
        details = "Conflict: vote already exists or does not exist." if not details else details
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=details)