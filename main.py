from models import Base, get_engine
from services.data_loader import DataLoader
from services.data_processor import DataProcessor
from config import db_connection

def main():
    file_path = 'files/filev2.xlsx'

    engine = get_engine(db_connection)
    Base.metadata.create_all(engine)

    data_loader = DataLoader(file_path)
    questionnaire_name, visit_types, specializations, header_and_question_df = data_loader.load_data()

    data_processor = DataProcessor(engine)
    data_processor.insert_data(questionnaire_name, visit_types, specializations, header_and_question_df)

if __name__ == '__main__':
    main()
    