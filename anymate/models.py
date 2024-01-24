from typing import Literal
from pydantic import BaseModel


class AuthResponse:
    def __init__(self, access_token, expires_in, token_type, scope):
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.scope = scope

class AnymateResponse(BaseModel):
    succeeded: bool
    message: str

class AnymateCreateTaskResponse(BaseModel):
    succeeded: bool
    message: str
    taskId: int

class AnymateCreateTasksResponse(BaseModel):
    succeeded: bool
    message: str
    taskIds: list


class AnymateProcessFailure(BaseModel):
    processKey: str
    message: str


class AnymateFinishRun(BaseModel):
    runId: int
    overwriteSecondsSaved: int = None
    overwriteEntries: int = None


class AnymateOkToRun(BaseModel):
    gateOpen: bool
    tasksAvailable: bool
    notBlockedDate: bool
    okToRun: bool


class AnymateRunResponse(BaseModel):
    processKey: str
    runId: int


class AnymateTaskAction(BaseModel):
    taskId: int
    reason: str
    comment: str = ''
    overwriteSecondsSaved: int = None
    overwriteEntries: int = None


class AnymateRetryTaskAction(BaseModel):
    taskId: int
    reason: str
    comment: str = ''
    activationDate: str = None
    overwriteSecondsSaved: int = None
    overwriteEntries: int = None

class AnymateReturnTaskAction(BaseModel):
    taskId: int
    action: Literal['Solved', 'Manual', 'Error', 'Retry']
    reason: str
    comment: str = ''
    activationDate: str = None
    overwriteSecondsSaved: int = None
    overwriteEntries: int = None

