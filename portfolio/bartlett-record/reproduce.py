#!/usr/bin/env python3
"""Check the companion's source-derived fiscal arithmetic, not its legal conclusions."""
from pathlib import Path
from decimal import Decimal as D
import csv, json, sys
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
    checks.append({'check':name,'actual':str(actual),'expected':str(expected),'passed':actual==expected})
def rows(name):
    with (ROOT/'data'/name).open(newline='',encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))
rev=rows('revenue.csv')
contrib={'Local/state/federal grants','Contributions','PPP loan and interest forgiveness','United Way','CDBG','Contributed nonfinancial assets'}
for yr,expected in [('FY2024',720301),('FY2025',207649)]:
    check('contribution_components_'+yr,sum(D(x[yr]) for x in rev if x['category'] in contrib),D(expected))
for yr,expected in [('FY2024',933797),('FY2025',469885)]:
    check('all_revenue_lines_'+yr,sum(D(x[yr]) for x in rev),D(expected))
for yr,expected in [('FY2024',842679),('FY2025',733865)]:
    check('functional_expenses_'+yr,sum(D(x[yr]) for x in rows('expense.csv')),D(expected))
check('government_category_decline',D(452969)-D(131834),D(321135))
check('total_revenue_decline',D(933797)-D(469885),D(463912))
check('expense_decline',D(842679)-D(733865),D(108814))
check('net_result_2025',D(469885)-D(733865),D(-263980))
check('cash_decline',D(55108)-D(72278),D(-17170))
check('operating_cash_bridge',sum(D(x['amount']) for x in rows('cash.csv')),D(-13452))
check('nonlease_liability_change',D(133468)-D(33646)-D(98770),D(1052))
check('internal_revenue',sum(D(x['actual8months']) for x in rows('internal.csv')),D('380842.56'))
check('internal_budget_revenue',sum(D(x['budget8months']) for x in rows('internal.csv')),D('556699.28'))
carry=D('2806.88')*7-D('4912.03')*4
check('candidate_carry',carry,D('0.04'))
check('candidate_rent_balance',D('2905.12')*3+carry,D('8715.40'))
check('internal_accounting_deficit',D('380842.56')-D('426463.84'),D('-45621.28'))
print(json.dumps({'checks':checks,'passed':all(x['passed'] for x in checks),'limits':'Arithmetic from research tables only. Candidate rent is not an authenticated ledger. Accounting deficit is not cash burn.'},indent=2))
sys.exit(0 if all(x['passed'] for x in checks) else 1)
