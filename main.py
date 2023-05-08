from robert_half.robert_half import scrape_rf
from google_sheets.csv_to_sheet import create_sheet


def main(job, zip_code, all):
    df = scrape_rf(job, zip_code, all)
    print(df)
    create_sheet('robert_half.csv',job)
    
if __name__ == '__main__':
    main('','94706', False)
