import pandas as pd

def save_data_to_csv(data, filename='processed_invoices.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    data = [
        {"invoice_number": "123456", "date": "2023-12-15", "amount": "RM2700", "vendor": "TS Rajan Auto Parts", "category": "Auto Parts"}
    ]
    save_data_to_csv(data)

