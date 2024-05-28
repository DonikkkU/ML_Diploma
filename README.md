<h1 align="center">Risk Management Model</h1>
<h2>Data: https://drive.google.com/drive/folders/1t55_IpGozKeYocJcxBtJ2eLFY62-PHJN?usp=sharing </h2>
Data Atributes:
id — request identifier. Applications are numbered so that more
the number corresponds to the later application date.
 rn is the serial number of the loan product in the credit history.
A higher number corresponds to a product with a later opening date.
 pre_since_opened — number of days from the loan opening date to the date
data collection (binarized*).
 pre_since_confirmed — number of days from the date of confirmation
information on the loan before the date of data collection (binarized*).
 pre_pterm — planned number of days from the loan opening date to the date
closures (binarized*).
 pre_fterm — actual number of days from the loan opening date to
closing dates (binarized*).
 6
pre_till_pclose — planned number of days from the date of data collection to the date
closing a loan (binarized*).
 pre_till_fclose - actual number of days from the date of data collection to
loan closing dates (binarized*).
 pre_loans_credit_limit — credit limit (binarized*).
 pre_loans_next_pay_summ — the amount of the next loan payment
(binarized*).
 pre_loans_outstanding — remaining unpaid loan amount
(binarized*).
 pre_loans_total_overdue — current overdue debt
(binarized*).
 pre_loans_max_overdue_sum - maximum overdue
debt (binarized*).
 pre_loans_credit_cost_rate — total cost of the loan (binarized*).
 pre_loans5 — number of overdues up to 5 days (binarized*).
 pre_loans530 — number of overdue payments from 5 to 30 days (binarized*).
 pre_loans3060 — number of overdue payments from 30 to 60 days (binarized*).
 pre_loans6090 — number of overdues from 60 to 90 days (binarized*).
 pre_loans90 — number of overdues by more than 90 days (binarized*).
 is_zero_loans_5 — flag: no overdue payments up to 5 days.
 is_zero_loans_530 — flag: no overdue from 5 to 30 days.
 is_zero_loans_3060 — flag: no overdue payments from 30 to 60 days.
 is_zero_loans_6090 - flag: no overdue from 60 to 90 days.
 is_zero_loans90 — flag: no overdue payments for more than 90 days.
 pre_util — ratio of the remaining unpaid loan amount 
 to the credit limit (binarized*).
 pre_over2limit — ratio of current overdue debt 
 to the credit limit (binarized*).
 7
pre_maxover2limit — ratio of maximum overdue
debt to credit limit (binarized*).
 is_zero_util - flag: ratio of the remaining unpaid amount
credit to credit limit equals 0.
 is_zero_over2limit — flag: ratio of the current overdue
debt to credit limit is 0.
 is_zero_maxover2limit — flag: ratio of maximum overdue
debt to credit limit is 0.
 enc_paym_{0..N} — statuses of monthly payments for the last N
months (coded**).
 enc_loans_account_holder_type - type of loan relationship
(encoded**).
 enc_loans_credit_status — loan status (encoded**).
 enc_loans_account_cur — loan currency (encoded**).
 enc_loans_credit_type — loan type (encoded**).
 pclose_flag — flag: planned number of days from the loan opening date
until the closing date has not been determined.
 fclose_flag - flag: actual number of days from the opening date
loan until closing date not determined
Атрибуты данных:
 id — идентификатор заявки. Заявки пронумерованы так, что большему 
номеру соответствует более поздняя дата заявки.
 rn — порядковый номер кредитного продукта в кредитной истории. 
Большему номеру соответствует продукт с более поздней датой открытия.
 pre_since_opened — количество дней с даты открытия кредита до даты 
сбора данных (бинаризовано*).
 pre_since_confirmed — количество дней с даты подтверждения 
информации по кредиту до даты сбора данных (бинаризовано*).
 pre_pterm — плановое количество дней с даты открытия кредита до даты 
закрытия (бинаризовано*).
 pre_fterm — фактическое количество дней с даты открытия кредита до 
даты закрытия (бинаризовано*).
 6
pre_till_pclose	— плановое количество дней с даты сбора данных до даты 
закрытия кредита (бинаризовано*).
 pre_till_fclose	— фактическое количество дней с даты сбора данных до 
даты закрытия кредита (бинаризовано*).
 pre_loans_credit_limit	 — кредитный лимит (бинаризовано*).
 pre_loans_next_pay_summ — сумма следующего платежа по кредиту 
(бинаризовано*).
 pre_loans_outstanding — оставшаяся невыплаченная сумма кредита 
(бинаризовано*).
 pre_loans_total_overdue — текущая просроченная задолженность 
(бинаризовано*).
 pre_loans_max_overdue_sum — максимальная просроченная 
задолженность (бинаризовано*).
 pre_loans_credit_cost_rate — полная стоимость кредита (бинаризовано*).
 pre_loans5 — число просрочек до 5 дней (бинаризовано*).
 pre_loans530 — число просрочек от 5 до 30 дней (бинаризовано*).
 pre_loans3060 — число просрочек от 30 до 60 дней (бинаризовано*).
 pre_loans6090 — число просрочек от 60 до 90 дней (бинаризовано*).
 pre_loans90 — число просрочек более чем на 90 дней (бинаризовано*).
 is_zero_loans_5 — флаг: нет просрочек до 5 дней.
 is_zero_loans_530 — флаг: нет просрочек от 5 до 30 дней.
 is_zero_loans_3060 — флаг: нет просрочек от 30 до 60 дней.
 is_zero_loans_6090 — флаг: нет просрочек от 60 до 90 дней.
 is_zero_loans90 — флаг: нет просрочек более чем на 90 дней.
 pre_util — отношение оставшейся невыплаченной суммы кредита 
 к кредитному лимиту (бинаризовано*).
 pre_over2limit	— отношение текущей просроченной задолженности 
 к кредитному лимиту (бинаризовано*).
 7
pre_maxover2limit — отношение максимальной просроченной 
задолженности к кредитному лимиту (бинаризовано*).
 is_zero_util — флаг: отношение оставшейся невыплаченной суммы 
кредита к кредитному лимиту равно 0.
 is_zero_over2limit — флаг: отношение текущей просроченной 
задолженности к кредитному лимиту равно 0.
 is_zero_maxover2limit — флаг: отношение максимальной просроченной 
задолженности к кредитному лимиту равно 0.
 enc_paym_{0..N} — статусы ежемесячных платежей за последние N 
месяцев (закодировано**).
 enc_loans_account_holder_type — тип отношения к кредиту 
(закодировано**).
 enc_loans_credit_status — статус кредита (закодировано**).
 enc_loans_account_cur — валюта кредита (закодировано**).
 enc_loans_credit_type — тип кредита (закодировано**).
 pclose_flag — флаг: плановое количество дней с даты открытия кредита 
до даты закрытия не определено.
 fclose_flag — флаг: фактическое количество дней с даты открытия 
кредита до даты закрытия не определено
