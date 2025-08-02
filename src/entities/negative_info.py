from typing import Optional
from pydantic import BaseModel, Field

class NegativeInfo(BaseModel):
    id: Optional[int] = None
    partner_id: Optional[int] = None
    status: Optional[str] = Field(default=None, alias="Статус")
    removed_from_sme_registry: Optional[str] = Field(default=None, alias="ИсклИзРеестраМСП")
    recently_registered: Optional[str] = Field(default=None, alias="РегНедавно")
    disqualified_director: Optional[str] = Field(default=None, alias="ДисквРук")
    disqualified_director_other: Optional[str] = Field(default=None, alias="ДисквРукДр")
    disqualified_director_other_no_inn: Optional[str] = Field(default=None, alias="ДисквРукДрБезИНН")
    sme_mass_address_registry: Optional[str] = Field(default=None, alias="РеестрМассАдрес")
    mass_address: Optional[str] = Field(default=None, alias="МассАдрес")
    decision_change_address: Optional[str] = Field(default=None, alias="РешИзмАдрес")
    invalid_address: Optional[str] = Field(default=None, alias="НедостоверАдрес")
    region_change_last_year: Optional[str] = Field(default=None, alias="СменаРег")
    mass_director_registry: Optional[str] = Field(default=None, alias="РеестрМассРук")
    mass_directors: Optional[str] = Field(default=None, alias="МассРук")
    mass_directors_no_inn: Optional[str] = Field(default=None, alias="МассРукБезИНН")
    director_liquidated_companies: Optional[str] = Field(default=None, alias="РукЛиквКомп")
    director_liquidated_companies_no_inn: Optional[str] = Field(default=None, alias="РукЛиквКомпБезИНН")
    invalid_director: Optional[str] = Field(default=None, alias="НедостоверРук")
    mass_founder_registry: Optional[str] = Field(default=None, alias="РеестрМассУчр")
    mass_director_founder_registry: Optional[str] = Field(default=None, alias="РеестрМассРукУчр")
    disqualified_founder_other: Optional[str] = Field(default=None, alias="ДисквУчрДр")
    disqualified_founder_other_no_inn: Optional[str] = Field(default=None, alias="ДисквУчрДрБезИНН")
    founder_liquidated_companies: Optional[str] = Field(default=None, alias="УчрЛиквКомп")
    founder_liquidated_companies_no_inn: Optional[str] = Field(default=None, alias="УчрЛиквКомпБезИНН")
    simultaneous_change_director_founder: Optional[str] = Field(default=None, alias="ОдноврСменаРукУчр")
    director_changes_per_year_more_than_two: Optional[str] = Field(default=None, alias="СменаРукГод")
    director_is_sole_founder: Optional[str] = Field(default=None, alias="РукУчр1Комп")
    invalid_founder: Optional[str] = Field(default=None, alias="НедостоверУчр")
    encumbrances: Optional[str] = Field(default=None, alias="Обременения")
    no_tax_reporting_over_year: Optional[str] = Field(default=None, alias="НеПредостОтч")
    tax_debt: Optional[str] = Field(default=None, alias="ЗадолжНалог")
    decision_reduce_charter_capital: Optional[str] = Field(default=None, alias="РешУмКап")
    employee_count: Optional[str] = Field(default=None, alias="КолРаб")
    account_blocked: Optional[str] = Field(default=None, alias="БлокСчета")
    bankrupt: Optional[str] = Field(default=None, alias="Банкрот")
    bankruptcy_intent: Optional[str] = Field(default=None, alias="БанкротНамерение")
    tax_audit_risk: Optional[str] = Field(default=None, alias="РискНалогПроверки")
    tax_arrears: Optional[str] = Field(default=None, alias="НедоимкаНалог")
    summary_text: Optional[str] = Field(default=None, alias="Текст")

    class Config:
        allow_population_by_field_name = True
