from pydantic import BaseModel
from typing import Optional
from datetime import date

class Client(BaseModel):
    """Модель для работы с таблицей 'clients' в базе данных."""
    
    id: Optional[int] = None
    company_name: str
    address: Optional[str] = None
    inn: int
    okved: Optional[str] = None
    director: Optional[str] = None
    director_function: Optional[str] = None
    date_reg: Optional[date] = None
    fns_check_date: Optional[date] = None
    has_negative: Optional[bool] = None