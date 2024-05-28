<h1 align="center">Risk Management Model</h1>
<h2>Data: https://drive.google.com/drive/folders/1t55_IpGozKeYocJcxBtJ2eLFY62-PHJN?usp=sharing </h2>
Data Atributes:
## Data Attributes

- **id**: Request identifier. Applications are numbered such that a higher number corresponds to a later application date.
- **rn**: Serial number of the loan product in the credit history. A higher number corresponds to a product with a later opening date.
- **pre_since_opened**: Number of days from the loan opening date to the data collection date (binarized*).
- **pre_since_confirmed**: Number of days from the date of confirmation information on the loan to the data collection date (binarized*).
- **pre_pterm**: Planned number of days from the loan opening date to the closing date (binarized*).
- **pre_fterm**: Actual number of days from the loan opening date to the closing date (binarized*).
- **pre_till_pclose**: Planned number of days from the data collection date to the loan closing date (binarized*).
- **pre_till_fclose**: Actual number of days from the data collection date to the loan closing date (binarized*).
- **pre_loans_credit_limit**: Credit limit (binarized*).
- **pre_loans_next_pay_summ**: Amount of the next loan payment (binarized*).
- **pre_loans_outstanding**: Remaining unpaid loan amount (binarized*).
- **pre_loans_total_overdue**: Current overdue debt (binarized*).
- **pre_loans_max_overdue_sum**: Maximum overdue debt (binarized*).
- **pre_loans_credit_cost_rate**: Total cost of the loan (binarized*).
- **pre_loans5**: Number of overdues up to 5 days (binarized*).
- **pre_loans530**: Number of overdue payments from 5 to 30 days (binarized*).
- **pre_loans3060**: Number of overdue payments from 30 to 60 days (binarized*).
- **pre_loans6090**: Number of overdues from 60 to 90 days (binarized*).
- **pre_loans90**: Number of overdues more than 90 days (binarized*).
- **is_zero_loans_5**: Flag: No overdue payments up to 5 days.
- **is_zero_loans_530**: Flag: No overdue payments from 5 to 30 days.
- **is_zero_loans_3060**: Flag: No overdue payments from 30 to 60 days.
- **is_zero_loans_6090**: Flag: No overdue payments from 60 to 90 days.
- **is_zero_loans90**: Flag: No overdue payments for more than 90 days.
- **pre_util**: Ratio of the remaining unpaid loan amount to the credit limit (binarized*).
- **pre_over2limit**: Ratio of current overdue debt to the credit limit (binarized*).
- **pre_maxover2limit**: Ratio of maximum overdue debt to credit limit (binarized*).
- **is_zero_util**: Flag: Ratio of the remaining unpaid loan amount to the credit limit equals 0.
- **is_zero_over2limit**: Flag: Ratio of the current overdue debt to the credit limit is 0.
- **is_zero_maxover2limit**: Flag: Ratio of maximum overdue debt to the credit limit is 0.
- **enc_paym_{0..N}**: Statuses of monthly payments for the last N months (encoded**).
- **enc_loans_account_holder_type**: Type of loan relationship (encoded**).
- **enc_loans_credit_status**: Loan status (encoded**).
- **enc_loans_account_cur**: Loan currency (encoded**).
- **enc_loans_credit_type**: Loan type (encoded**).
- **pclose_flag**: Flag: Planned number of days from the loan opening date until the closing date has not been determined.
- **fclose_flag**: Flag: Actual number of days from the loan opening date until the closing date has not been determined.

\* Binarized: Attributes are converted into binary format for easier processing.

\** Encoded: Attributes are encoded into a specific format for easier processing.

