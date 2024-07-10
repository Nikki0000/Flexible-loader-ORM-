import logging
import pandas as pd

logging.basicConfig(filename='files/log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Logger:
    def __init__(self, log_excel_path='files/log.xlsx'):
        self.log_excel_path = log_excel_path
        self.log_data = {
            'Questionnaire': [],
            'QuestionnaireHeader': [],
            'Question': [],
            'QuestionConfiguration': []
        }

    def log_to_file(self, message):
        logging.info(message)

    def log_to_excel(self, table, data):
        self.log_data[table].append(data)

    def save_excel_log(self):
        writer = pd.ExcelWriter(self.log_excel_path, engine='xlsxwriter')
        for table, data in self.log_data.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=table, index=False)
        writer.save()