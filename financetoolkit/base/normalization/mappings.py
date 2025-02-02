from normalized_columns import *

FMP = "fmp"
EODHD = "eodhd"

BALANCE = "balance"
INCOME = "income"
STATS = "statistics"
CASH = "cash"

# provider -> kind -> mapping
MAPPINGS = {
    FMP: {
        BALANCE: {
            "cashAndCashEquivalents" : CASH_AND_CASH_EQUIVALENTS,
            "shortTermInvestments" : SHORT_TERM_INVESTMENTS,
            "cashAndShortTermInvestments" : CASH_AND_SHORT_TERM_INVESTMENTS,
            "netReceivables" : NET_RECEIVABLES,
            "inventory" : INVENTORY,
            "otherCurrentAssets" : OTHER_CURRENT_ASSETS,
            "totalCurrentAssets" : TOTAL_CURRENT_ASSETS,
            "propertyPlantEquipmentNet" : PROPERTY_PLANT_EQUIPMENT_NET,
            "longTermInvestments" : LONG_TERM_INVESTMENTS,
            "taxAssets" : TAX_ASSETS,
            "goodwill" : GOODWILL,
            "intangibleAssets" : INTANGIBLE_ASSETS,
            "otherNonCurrentAssets" : OTHER_NON_CURRENT_ASSETS,
            "totalNonCurrentAssets" : TOTAL_NON_CURRENT_ASSETS,
            "otherAssets" : OTHER_ASSETS,
            "totalAssets" : TOTAL_ASSETS,
            "accountPayables" : ACCOUNT_PAYABLES,
            "shortTermDebt" : SHORT_TERM_DEBT,
            "taxPayables" : TAX_PAYABLES,
            "deferredRevenue" : DEFERRED_REVENUE,
            "otherCurrentLiabilities" : OTHER_CURRENT_LIABILITIES,
            "totalCurrentLiabilities" : TOTAL_CURRENT_LIABILITIES,
            "longTermDebt" : LONG_TERM_DEBT,
            "deferredRevenueNonCurrent" : DEFERRED_REVENUE_NON_CURRENT,
            "deferredTaxLiabilitiesNonCurrent" : DEFERRED_TAX_LIABILITIES_NON_CURRENT,
            "otherNonCurrentLiabilities" : OTHER_NON_CURRENT_LIABILITIES,
            "totalNonCurrentLiabilities" : TOTAL_NON_CURRENT_LIABILITIES,
            "otherLiabilities" : OTHER_LIABILITIES,
            "capitalLeaseObligations" : CAPITAL_LEASE_OBLIGATIONS,
            "totalDebt" : TOTAL_DEBT,
            "netDebt" : NET_DEBT,
            "totalInvestments" : TOTAL_INVESTMENTS,
            "totalLiabilities" : TOTAL_LIABILITIES,
            "preferredStock" : PREFERRED_STOCK,
            "commonStock" : COMMON_STOCK,
            "retainedEarnings" : RETAINED_EARNINGS,
            "accumulatedOtherComprehensiveIncomeLoss" : ACCUMULATED_OTHER_COMPREHENSIVE_INCOME_LOSS,
            "othertotalStockholdersEquity" : OTHERTOTAL_STOCKHOLDERS_EQUITY,
            "totalStockholdersEquity" : TOTAL_STOCKHOLDERS_EQUITY,
            "totalEquity" : TOTAL_EQUITY,
            "totalLiabilitiesAndStockholdersEquity" : TOTAL_LIABILITIES_AND_STOCKHOLDERS_EQUITY,
            "minorityInterest" : MINORITY_INTEREST,
            "totalLiabilitiesAndTotalEquity" : TOTAL_LIABILITIES_AND_TOTAL_EQUITY,
        },
        CASH: {
            "netIncome" : NET_INCOME,
            "depreciationAndAmortization" : DEPRECIATION_AND_AMORTIZATION,
            "deferredIncomeTax" : DEFERRED_INCOME_TAX,
            "stockBasedCompensation" : STOCK_BASED_COMPENSATION,
            "changeInWorkingCapital" : CHANGE_IN_WORKING_CAPITAL,
            "accountsReceivables" : ACCOUNTS_RECEIVABLES,
            "inventory" : INVENTORY,
            "accountsPayables" : ACCOUNTS_PAYABLES,
            "otherWorkingCapital" : OTHER_WORKING_CAPITAL,
            "otherNonCashItems" : OTHER_NON_CASH_ITEMS,
            "netCashProvidedByOperatingActivities" : NET_CASH_PROVIDED_BY_OPERATING_ACTIVITIES,
            "investmentsInPropertyPlantAndEquipment" : PROPERTY_PLANT_EQUIPMENT_NET,
            "acquisitionsNet" : ACQUISITIONS_NET,
            "purchasesOfInvestments" : PURCHASES_OF_INVESTMENTS,
            "salesMaturitiesOfInvestments" : SALES_MATURITIES_OF_INVESTMENTS,
            "otherInvestingActivites" : OTHER_INVESTING_ACTIVITES,
            "netCashUsedForInvestingActivites" : NET_CASH_USED_FOR_INVESTING_ACTIVITES,
            "debtRepayment" : DEBT_REPAYMENT,
            "commonStockIssued" : COMMON_STOCK_ISSUED,
            "commonStockRepurchased" : COMMON_STOCK_REPURCHASED,
            "dividendsPaid" : DIVIDENDS_PAID,
            "" : "Preferred Dividends Paid",
            "otherFinancingActivites" : OTHER_FINANCING_ACTIVITES,
            "netCashUsedProvidedByFinancingActivities" : NET_CASH_USED_PROVIDED_BY_FINANCING_ACTIVITIES,
            "effectOfForexChangesOnCash" : EFFECT_OF_FOREX_CHANGES_ON_CASH,
            "netChangeInCash" : NET_CHANGE_IN_CASH,
            "cashAtEndOfPeriod" : CASH_AT_END_OF_PERIOD,
            "cashAtBeginningOfPeriod" : CASH_AT_BEGINNING_OF_PERIOD,
            "operatingCashFlow" : OPERATING_CASH_FLOW,
            "capitalExpenditure" : CAPITAL_EXPENDITURE,
            "freeCashFlow" : FREE_CASH_FLOW,
        },
        INCOME: {
            "revenue" : REVENUE,
            "costOfRevenue" : COST_OF_REVENUE,
            "grossProfit" : GROSS_PROFIT,
            "grossProfitRatio" : GROSS_PROFIT_RATIO,
            "researchAndDevelopmentExpenses" : RESEARCH_AND_DEVELOPMENT_EXPENSES,
            "generalAndAdministrativeExpenses" : GENERAL_AND_ADMINISTRATIVE_EXPENSES,
            "sellingAndMarketingExpenses" : SELLING_AND_MARKETING_EXPENSES,
            "sellingGeneralAndAdministrativeExpenses" : SELLING_GENERAL_AND_ADMINISTRATIVE_EXPENSES,
            "otherExpenses" : OTHER_EXPENSES,
            "operatingExpenses" : OPERATING_EXPENSES,
            "costAndExpenses" : COST_AND_EXPENSES,
            "interestIncome" : INTEREST_INCOME,
            "interestExpense" : INTEREST_EXPENSE,
            "depreciationAndAmortization" : DEPRECIATION_AND_AMORTIZATION,
            "ebitda" : EBITDA,
            "ebitdaratio" : EBITDARATIO,
            "operatingIncome" : OPERATING_INCOME,
            "operatingIncomeRatio" : OPERATING_INCOME_RATIO,
            "totalOtherIncomeExpensesNet" : TOTAL_OTHER_INCOME_EXPENSES_NET,
            "incomeBeforeTax" : INCOME_BEFORE_TAX,
            "incomeBeforeTaxRatio" : INCOME_BEFORE_TAX_RATIO,
            "incomeTaxExpense" : INCOME_TAX_EXPENSE,
            "netIncome" : NET_INCOME,
            "netIncomeRatio" : NET_INCOME_RATIO,
            "eps" : EPS,
            "epsdiluted" : EPSDILUTED,
            "weightedAverageShsOut" : WEIGHTED_AVERAGE_SHS_OUT,
            "weightedAverageShsOutDil" : WEIGHTED_AVERAGE_SHS_OUT_DIL,
        },
        STATS: {
            "reportedCurrency" : REPORTED_CURRENCY,
            "cik" : CIK,
            "fillingDate" : FILLING_DATE,
            "acceptedDate" : ACCEPTED_DATE,
            "calendarYear" : CALENDAR_YEAR,
            "period" : PERIOD,
            "link" : LINK,
            "finalLink" : FINAL_LINK,
        }
    }
}