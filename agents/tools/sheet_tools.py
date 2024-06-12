from data_parser.worksheet_manager import WorksheetManagerFactory
from pydantic.v1 import BaseModel, Field


class FetchValueFromSheetRequest(BaseModel):
    sheet_name: str = Field(default="")
    key: str = Field(..., description="the key for which need to fetch the value")
    date: str = Field(..., description="date that is mentioned in the request. Its pattern is YYYY-MM-DD")


class FetchValueFromSheetResponse(BaseModel):
    response: str = Field(..., description="value of the filed in sheet")


class FetchValueFromSheet:
    def __init__(self, worksheet_factory: WorksheetManagerFactory):
        self.w: WorksheetManagerFactory = worksheet_factory

    def execute(self, req: FetchValueFromSheetRequest) -> FetchValueFromSheetResponse:
        parsed_ws = self.w.load_worksheets(req.sheet_name)
        return FetchValueFromSheetResponse(response="test response")
