#skeleton
from pydantic import BaseModel

class EmployeesStatus(BaseModel):
    PerfScoreID:int
    SalaryID: int
    PositionID:int
    EngagementSurvey: int
    EmpSatisfaction: float
    SpecialProjectsCount: int
    DaysLateLast30: int
    Absences: int