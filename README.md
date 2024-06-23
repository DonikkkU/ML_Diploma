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
<h1>Модель кредитного риск-менеджмента</h1>
<h2>Условие задачи</h2>
<p>Необходимо разработать модель кредитного риск-менеджмента для оценки вероятности дефолта клиента по кредиту. Дефолт определяется как непогашение займа в течение 90 дней. Модель должна помочь банкам минимизировать убытки за счет предсказания риска невыполнения кредитных обязательств клиентами. Для этого потребуется обработать и проанализировать большой объем данных, выделить значимые признаки, обучить модель и оценить её качество.</p>
<h2>Цели</h2>
<ol>
  <li><b>Сбор и предварительный анализ данных</b>: Загрузить и проанализировать структуру тренировочного датасета.</li>
  <li><b>Создание и обработка признаков</b>: Определить и сгенерировать полезные признаки для улучшения качества модели.</li>
  <li><b>Объединение данных</b>: Объединить созданные признаки с целевой переменной.</li>
  <li><b>Разделение данных на выборки</b>: Поделить данные на тренировочную и тестовую выборки.</li>
  <li><b>Обучение модели</b>: Обучить модель на тренировочной выборке и оценить её качество на тестовой выборке.</li>
  <li><b>Автоматизация процесса</b>: Разработать автоматизированный пайплайн для подготовки данных и обучения модели.</li>
  <li><b>Сохранение результатов</b>: Сохранить обученную модель и результаты в формате, удобном для дальнейшего использования.</li>
</ol>
<h2>Содержание работы</h2>
<ol>
  <li><b>Введение</b>
    <ul>
      <li>Описание задачи</li>
      <li>Цели и этапы работы</li>
    </ul>
  </li>
  <li><b>Сбор и предварительный анализ данных</b>
    <ul>
      <li>Загрузка данных</li>
      <li>Анализ структуры данных</li>
    </ul>
  </li>
  <li><b>Создание и обработка признаков</b>
    <ul>
      <li>Выделение полезных признаков</li>
      <li>Комментарии по выбору признаков</li>
    </ul>
  </li>
  <li><b>Объединение данных</b>
    <ul>
      <li>Слияние признаков с целевой переменной</li>
      <li>Сохранение итогового датафрейма</li>
    </ul>
  </li>
  <li><b>Разделение данных на выборки</b>
    <ul>
      <li>Поделение данных на тренировочную и тестовую выборки</li>
      <li>Оценка размера выборок</li>
    </ul>
  </li>
  <li><b>Обучение модели</b>
    <ul>
      <li>Выбор и настройка модели</li>
      <li>Обучение и оценка качества модели</li>
    </ul>
  </li>
  <li><b>Автоматизация процесса</b>
    <ul>
      <li>Создание пайплайна для подготовки данных и обучения модели</li>
      <li>Сохранение пайплайна и модели</li>
    </ul>
  </li>
  <li><b>Результаты и выводы</b>
    <ul>
      <li>Результаты обучения модели</li>
      <li>Выводы по результатам работы</li>
    </ul>
  </li>
</ol>
<h2>Выводы</h2>
<p>В ходе работы была создана и протестирована модель для оценки кредитного риска. Модель показала хорошие результаты на тестовых данных, что подтверждается следующими метриками:</p>
<ul>
  <li>Лучший показатель AUC на валидационной выборке: 0.792368002835276</li>
  <li>Среднее значение предсказаний для out-of-fold выборок: 0.3943739841004673</li>
  <li>Кросс-валидационный показатель ROC AUC: 0.7606100113938197</li>
</ul>
<p>Эти результаты свидетельствуют о высокой точности модели в предсказании вероятности дефолта клиентов. Разработанный автоматизированный пайплайн позволяет эффективно готовить данные и обучать модель, что делает процесс оценки кредитоспособности клиентов быстрым и надёжным.</p>
