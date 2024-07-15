import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try: 
            #Читаем лист Questionnaire
            questionnaire_df = pd.read_excel(self.file_path, sheet_name='Questionnaire')
            if questionnaire_df.empty:
                raise ValueError("Недостаточно данных в листе Questionnaire")
        
            # print(questionnaire_df)
            # print(questionnaire_df.shape)

            questionnaire_name = questionnaire_df.iloc[0, 0]
            visit_type = [vt.strip() for vt in questionnaire_df.iloc[0, 1].split(',')]

            #Читаем лист QuestionAndHeader
            header_and_question_df = pd.read_excel(self.file_path, sheet_name='HeaderAndQuestion')

            if header_and_question_df.empty:
                    raise ValueError("Недостаточно данных в листе 'HeaderAndQuestion'")

            return questionnaire_name, visit_type, header_and_question_df
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            raise