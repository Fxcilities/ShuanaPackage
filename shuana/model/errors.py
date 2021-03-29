class PornHubRequestError(Exception):
    def __init__(self, message):
        self.requests_count = float('inf')
        self.message = message
        super().__init__(message)
    
    def __repr__(self) -> str:
        return f"<PornHubRequestError '{self.message}'>"
    
    def __str__(self) -> str:
        return self.message
