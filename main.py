import pandas as pd
from src.reporter import DataFrameReporter

def main():
    df = pd.read_csv('data/payments.csv', encoding='utf-8')
    reporter = DataFrameReporter(float_format='0.05f', percent_format='0.02%', include_all=False)
    reporter.show_report(df, title='Отчет по данным payments.csv')

if __name__ == '__main__':
    main()