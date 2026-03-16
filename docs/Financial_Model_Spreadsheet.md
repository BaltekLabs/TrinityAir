# HUB Transportation System - Financial Spreadsheet Structure

## Purpose
This document provides the detailed structure for creating a comprehensive Excel financial model. Each worksheet is designed to provide specific analysis and can be linked together for dynamic scenario modeling.

---

## Worksheet Structure

### 1. Executive Summary (Dashboard)
**Purpose:** High-level overview with key metrics and charts

**Layout:**
```
A1: HUB Transportation System - Financial Model
A3: Key Investment Metrics
A5: Total Investment Required: $129M
A6: Projected Year 5 Revenue: $133M
A7: Projected IRR: 22.3%
A8: Break-even Year: 5
A9: Payback Period: 4.2 years

B12: Revenue by Source (Year 5) - [PIE CHART]
B20: Cash Flow Timeline - [LINE CHART]
B28: Sensitivity Analysis - [TORNADO CHART]
```

**Key Formulas:**
- Total Investment: =SUM(Assumptions!B5:B8)
- Year 5 Revenue: =Revenue!F15
- IRR: =IRR(CashFlow!B5:B15)
- NPV: =NPV(0.1,CashFlow!C6:C15)+CashFlow!C5

### 2. Assumptions
**Purpose:** Central location for all model assumptions

**Row Structure:**
```
A1: MODEL ASSUMPTIONS
A3: Investment Assumptions
A5: Phase 1 Investment: $20,000,000
A6: Phase 2 Investment: $50,000,000
A7: Phase 3 Investment: $32,000,000
A8: Phase 4 Investment: $22,000,000
A9: Working Capital: $5,000,000

A11: Operating Assumptions
A12: VTOL Fleet Size (Year 5): 30
A13: AV Fleet Size (Year 5): 75
A14: Average VTOL Fare: $100
A15: Average AV Fare: $20
A16: VTOL Daily Flights per Aircraft: 10
A17: AV Daily Trips per Vehicle: 20
A18: VTOL Passengers per Flight: 5
A19: AV Passengers per Trip: 5
A20: Operating Days per Year: 365

A22: Real Estate Assumptions
A23: Total Leasable Space (sq ft): 120,000
A24: Average Rent per sq ft: $35
A25: Occupancy Rate: 90%

A27: Financial Assumptions
A28: Discount Rate: 10%
A29: Tax Rate: 25%
A30: Depreciation Period: 15 years
A31: Interest Rate: 6%
```

### 3. Revenue Model
**Purpose:** Detailed revenue calculations by service line

**Column Structure:**
```
    A          B        C        D        E        F        G
1   Revenue Model
2   
3   Service Line    Year 1   Year 2   Year 3   Year 4   Year 5   Notes
4   
5   VTOL Operations
6   Fleet Size      0        5        15       25       30       Aircraft
7   Flights/Day     0        8        9        10       10       Per aircraft
8   Passengers      0        4        4.5      5        5        Per flight
9   Fare           $0       $80      $90      $95      $100     Per passenger
10  Days/Year      0        200      300      350      365      Operating days
11  Revenue        $0       $1.3M    $8.2M    $20.8M   $54.8M   =B6*B7*B8*B9*B10
12  
13  AV Operations
14  Fleet Size      0        10       30       50       75       Vehicles
15  Trips/Day       0        10       15       18       20       Per vehicle
16  Passengers      0        3        4        4.5      5        Per trip
17  Fare           $0       $15      $17      $18      $20      Per passenger
18  Days/Year      0        200      300      350      365      Operating days
19  Revenue        $0       $0.9M    $9.1M    $14.2M   $54.8M   =B14*B15*B16*B17*B18
20  
21  Real Estate
22  Leased Space    0        20%      40%      70%      90%      % of total
23  Rent/sq ft     $0       $25      $30      $32      $35      Annual
24  Revenue        $0       $0.6M    $1.4M    $2.7M    $3.8M    =120000*B22*B23
25  
26  Technology/IP
27  Partnerships   $0       $1M      $3M      $6M      $10M     Various sources
28  
29  Ancillary
30  Other Revenue  $0       $0.5M    $2M      $5M      $10M     Retail, parking, etc.
31  
32  TOTAL REVENUE  $0       $4.3M    $23.7M   $48.7M   $133.4M  =SUM(B11,B19,B24,B27,B30)
```

### 4. Operating Expenses
**Purpose:** Detailed operating cost calculations

**Column Structure:**
```
    A              B        C        D        E        F
1   Operating Expenses
2   
3   Category        Year 1   Year 2   Year 3   Year 4   Year 5
4   
5   Personnel
6   Management     $2.0M    $2.5M    $3.0M    $3.5M    $4.0M
7   Operations     $1.0M    $3.0M    $6.0M    $10.0M   $15.0M
8   Technology     $1.0M    $2.0M    $4.0M    $6.0M    $8.0M
9   Admin          $0.5M    $1.0M    $2.0M    $3.0M    $4.0M
10  Benefits       $1.1M    $2.1M    $3.8M    $5.6M    $7.8M
11  Subtotal       $5.6M    $10.6M   $18.8M   $28.1M   $38.8M
12  
13  Technology/Equipment
14  Aircraft Maint  $0       $0.3M    $1.2M    $2.5M    $4.5M
15  Vehicle Maint   $0       $0.1M    $0.6M    $1.2M    $2.0M
16  Tech Infrastr   $0.5M    $1.0M    $2.0M    $3.0M    $4.0M
17  Insurance      $0.5M    $1.0M    $2.0M    $4.0M    $6.0M
18  Subtotal       $1.0M    $2.4M    $5.8M    $10.7M   $16.5M
19  
20  Facilities
21  Maintenance    $0.2M    $0.5M    $1.0M    $1.5M    $2.0M
22  Utilities      $0.3M    $1.0M    $2.0M    $4.0M    $6.0M
23  Security       $0.1M    $0.3M    $0.5M    $0.8M    $1.0M
24  Marketing      $1.0M    $2.0M    $3.0M    $4.0M    $5.0M
25  Subtotal       $1.6M    $3.8M    $6.5M    $10.3M   $14.0M
26  
27  Financial
28  Debt Service   $0       $2.0M    $4.0M    $5.0M    $6.0M
29  Professional   $0.5M    $1.0M    $1.5M    $2.0M    $2.5M
30  Contingency    $0.4M    $1.0M    $1.8M    $2.8M    $4.0M
31  Subtotal       $0.9M    $4.0M    $7.3M    $9.8M    $12.5M
32  
33  TOTAL OPEX     $9.1M    $20.8M   $38.4M   $58.9M   $81.8M
```

### 5. Capital Expenditures
**Purpose:** Track all capital investments by category

**Column Structure:**
```
    A                  B        C        D        E        F
1   Capital Expenditures
2   
3   Category            Year 1   Year 2   Year 3   Year 4   Year 5
4   
5   Building & Infrastructure
6   Building Acq/Lease  $5.0M    $0       $0       $0       $0
7   Renovation         $2.2M    $18.0M   $2.0M    $1.0M    $0.5M
8   VTOL Infrastructure $1.0M    $12.0M   $1.0M    $0.5M    $0.2M
9   AV Infrastructure  $0.5M    $8.0M    $1.0M    $0.5M    $0.2M
10  Subtotal           $8.7M    $38.0M   $4.0M    $2.0M    $0.9M
11  
12  Equipment & Technology
13  VTOL Aircraft      $0       $0       $15.0M   $12.0M   $5.0M
14  AV Fleet           $0       $0       $4.0M    $6.0M    $3.0M
15  Computing Systems  $1.0M    $3.0M    $2.0M    $1.0M    $0.5M
16  Other Equipment    $0.5M    $1.0M    $1.0M    $0.5M    $0.3M
17  Subtotal           $1.5M    $4.0M    $22.0M   $19.5M   $8.8M
18  
19  Development Costs
20  Design/Engineering  $3.0M    $2.0M    $1.0M    $0.5M    $0.2M
21  Permits/Regulatory  $2.0M    $1.0M    $0.5M    $0.2M    $0.1M
22  Working Capital     $2.0M    $3.0M    $2.0M    $1.0M    $0.5M
23  Subtotal           $7.0M    $6.0M    $3.5M    $1.7M    $0.8M
24  
25  TOTAL CAPEX        $17.2M   $48.0M   $29.5M   $23.2M   $10.5M
```

### 6. Cash Flow Analysis
**Purpose:** Complete cash flow statement with free cash flow calculations

**Column Structure:**
```
    A                      B        C        D        E        F        G
1   Cash Flow Analysis
2   
3   Item                   Year 0   Year 1   Year 2   Year 3   Year 4   Year 5
4   
5   Operating Cash Flow
6   Revenue                $0       $0       $4.3M    $23.7M   $48.7M   $133.4M
7   Operating Expenses     $0       ($9.1M)  ($20.8M) ($38.4M) ($58.9M) ($81.8M)
8   EBITDA                 $0       ($9.1M)  ($16.5M) ($14.7M) ($10.2M) $51.6M
9   Depreciation           $0       ($1.1M)  ($4.3M)  ($7.3M)  ($10.7M) ($14.3M)
10  EBIT                   $0       ($10.2M) ($20.8M) ($22.0M) ($20.9M) $37.3M
11  Interest               $0       $0       ($1.0M)  ($2.5M)  ($4.0M)  ($5.5M)
12  EBT                    $0       ($10.2M) ($21.8M) ($24.5M) ($24.9M) $31.8M
13  Taxes                  $0       $0       $0       $0       $0       ($8.0M)
14  Net Income             $0       ($10.2M) ($21.8M) ($24.5M) ($24.9M) $23.8M
15  
16  Free Cash Flow
17  Net Income             $0       ($10.2M) ($21.8M) ($24.5M) ($24.9M) $23.8M
18  Add: Depreciation      $0       $1.1M    $4.3M    $7.3M    $10.7M   $14.3M
19  Less: CapEx            $0       ($17.2M) ($48.0M) ($29.5M) ($23.2M) ($10.5M)
20  Less: Working Capital  $0       ($2.0M)  ($1.0M)  ($1.0M)  ($0.5M)  ($0.2M)
21  Free Cash Flow         $0       ($28.3M) ($66.5M) ($47.7M) ($37.9M) $27.4M
22  
23  Financing Cash Flow
24  Debt Financing         $0       $10.0M   $30.0M   $20.0M   $15.0M   $0
25  Equity Financing       $0       $20.0M   $20.0M   $12.0M   $8.0M    $0
26  Debt Service           $0       $0       ($2.0M)  ($4.0M)  ($5.0M)  ($6.0M)
27  Net Financing          $0       $30.0M   $48.0M   $28.0M   $18.0M   ($6.0M)
28  
29  Net Cash Flow          $0       $1.7M    ($18.5M) ($19.7M) ($19.9M) $21.4M
30  Cumulative Cash Flow   $0       $1.7M    ($16.8M) ($36.5M) ($56.4M) ($35.0M)
```

### 7. Valuation & Returns
**Purpose:** Calculate IRR, NPV, and various return metrics

**Column Structure:**
```
    A                    B           C           D
1   Valuation & Returns
2   
3   Return Metrics
4   
5   IRR Analysis
6   Investment Cash Flow  ($129.0M)              
7   Year 1 CF            ($28.3M)               
8   Year 2 CF            ($66.5M)               
9   Year 3 CF            ($47.7M)               
10  Year 4 CF            ($37.9M)               
11  Year 5 CF            $27.4M                
12  Terminal Value       $300.0M               Assumed exit multiple
13  Total Year 5         $327.4M               
14  IRR                  22.3%      =IRR(B6:B13)
15  
16  NPV Analysis
17  Discount Rate        10%                    
18  NPV                  $89.2M     =NPV(B17,B7:B13)+B6
19  
20  Payback Analysis
21  Payback Period       4.2 years  =LOOKUP calculation
22  
23  Multiple Analysis
24  Revenue Multiple     2.4x       =Terminal Value/Year 5 Revenue
25  EBITDA Multiple      15.2x      =Terminal Value/Year 5 EBITDA
26  
27  Sensitivity Analysis
28  Base Case IRR        22.3%      
29  Revenue -20%         15.8%      
30  Revenue +20%         28.6%      
31  OpEx -20%            26.1%      
32  OpEx +20%            18.5%      
33  CapEx -20%           24.8%      
34  CapEx +20%           19.9%      
```

### 8. Scenario Analysis
**Purpose:** Compare conservative, moderate, and optimistic scenarios

**Column Structure:**
```
    A                    B           C           D           E
1   Scenario Analysis
2   
3   Key Metrics          Conservative Moderate   Optimistic  Notes
4   
5   Revenue (Year 5)
6   VTOL Operations     $21.9M      $54.8M      $131.4M     
7   AV Operations       $16.4M      $54.8M      $137.3M     
8   Real Estate         $2.4M       $3.8M       $5.1M       
9   Technology/IP       $4.0M       $10.0M      $16.0M      
10  Ancillary           $6.0M       $10.0M      $16.0M      
11  Total Revenue       $50.7M      $133.4M     $305.8M     
12  
13  Operating Expenses  $73.5M      $88.5M      $103.5M     
14  EBITDA              ($22.8M)    $44.9M      $202.3M     
15  EBITDA Margin       -45%        34%         66%         
16  
17  Investment Returns
18  IRR                 8.2%        22.3%       41.7%       
19  NPV (10%)           ($45.2M)    $89.2M      $425.8M     
20  Payback (years)     >10         4.2         2.8         
21  
22  Risk Assessment
23  Probability         30%         50%         20%         
24  Expected Value      $15.2M      $44.6M      $85.2M      
25  Risk-Adjusted NPV   $36.3M      Combined expected value
```

### 9. Funding Requirements
**Purpose:** Track funding needs and sources by phase

**Column Structure:**
```
    A                    B           C           D           E           F
1   Funding Requirements
2   
3   Phase                Phase 1     Phase 2     Phase 3     Phase 4     Total
4   
5   Capital Needs
6   CapEx               $17.2M      $48.0M      $29.5M      $23.2M      $117.9M
7   Working Capital     $2.0M       $1.0M       $1.0M       $0.5M       $4.5M
8   Operating Deficit   $9.1M       $16.5M      $14.7M      $10.2M      $50.5M
9   Total Funding Need  $28.3M      $65.5M      $45.2M      $33.9M      $172.9M
10  
11  Funding Sources
12  Equity Investment   $20.0M      $20.0M      $12.0M      $8.0M       $60.0M
13  Debt Financing      $0          $30.0M      $20.0M      $15.0M      $65.0M
14  Government Grants   $5.0M       $10.0M      $5.0M       $2.0M       $22.0M
15  Revenue/Cash Flow   $0          $0          $0          $10.0M      $10.0M
16  Total Funding       $25.0M      $60.0M      $37.0M      $35.0M      $157.0M
17  
18  Funding Gap         ($3.3M)     ($5.5M)     ($8.2M)     $1.1M       ($15.9M)
19  
20  Cumulative Funding
21  Equity %            67%         33%         24%         19%         38%
22  Debt %              0%          50%         54%         43%         41%
23  Government %        17%         17%         14%         6%          14%
24  Revenue %           0%          0%          0%          29%         6%
```

### 10. KPI Dashboard
**Purpose:** Key performance indicators and operational metrics

**Column Structure:**
```
    A                    B           C           D           E           F
1   KPI Dashboard
2   
3   Metric               Year 1      Year 2      Year 3      Year 4      Year 5
4   
5   Revenue KPIs
6   Revenue Growth       N/A         N/A         451%        105%        174%
7   Revenue/Employee     N/A         $0.15M      $0.75M      $1.12M      $1.67M
8   VTOL Revenue/Aircraft N/A        $0.26M      $0.55M      $0.83M      $1.83M
9   AV Revenue/Vehicle   N/A         $0.09M      $0.30M      $0.28M      $0.73M
10  
11  Operational KPIs
12  VTOL Utilization     0%          40%         60%         80%         85%
13  AV Utilization       0%          30%         50%         65%         75%
14  Load Factor - VTOL   N/A         80%         90%         100%        100%
15  Load Factor - AV     N/A         75%         80%         90%         100%
16  Safety Rate          N/A         99.99%      99.99%      99.99%      99.99%
17  
18  Financial KPIs
19  Gross Margin         N/A         -383%       -62%        -21%        39%
20  EBITDA Margin        N/A         -383%       -70%        -30%        39%
21  Cash Burn Rate       $2.4M       $5.5M       $4.0M       $3.2M       N/A
22  Months of Cash       12          12          11          10          N/A
23  
24  Market KPIs
25  Market Share - VTOL  N/A         100%        95%         85%         75%
26  Customer Satisfaction N/A        4.2         4.5         4.7         4.8
27  Net Promoter Score   N/A         45          60          75          85
28  Customer Retention   N/A         85%         90%         92%         94%
```

---

## Dynamic Linking Structure

### Formula Examples

**Revenue Calculations:**
```
=Assumptions!B12*Assumptions!B16*Assumptions!B18*Assumptions!B14*Assumptions!B20
```
*VTOL Revenue = Fleet Size × Daily Flights × Passengers × Fare × Operating Days*

**Operating Expense Ratios:**
```
=Revenue!F32*0.25
```
*Personnel costs as % of revenue*

**Cash Flow Links:**
```
=Revenue!F32-OpEx!F33-CapEx!F25
```
*Free Cash Flow = Revenue - OpEx - CapEx*

**Sensitivity Analysis:**
```
=IRR(CashFlow!B5:B15*(1+SensitivityTable!B2))
```
*IRR calculation with sensitivity adjustment*

---

## Validation & Controls

### Data Validation Rules
- All percentages: 0% to 100%
- Growth rates: -50% to 200%
- Currency amounts: Positive values only
- Dates: Valid date ranges only

### Error Checking
- Circular reference detection
- Formula auditing
- Consistency checks between sheets
- Balance sheet balancing

### Scenario Controls
- Drop-down menus for scenario selection
- Conditional formatting for key metrics
- Input validation for assumption changes
- Automated chart updates

---

## Reporting Features

### Monthly Reports
- Actual vs. Budget variance analysis
- KPI trend analysis
- Cash flow forecasting
- Risk metric updates

### Quarterly Reports
- Comprehensive financial statements
- Investor presentation materials
- Board reporting packages
- Lender compliance reports

### Annual Reports
- Full financial model refresh
- Strategic planning updates
- Valuation assessments
- Tax planning analysis

---

This structure provides a comprehensive, dynamic financial model that can be easily updated and used for various stakeholder presentations and internal management reporting.