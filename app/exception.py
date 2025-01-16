from fastapi import HTTPException, status

class Exceptions:
    
    @staticmethod
    def exception_404(details: str = ''):
        details = "Not Found" if not details else details
        return HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=details)
