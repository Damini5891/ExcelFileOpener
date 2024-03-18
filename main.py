import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox


def open_excel_file():
    file_path = filedialog.askopenfilename(
        title='Open Excel File',
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )

    if file_path:
        try:
            df = pd.read_excel(file_path)
            display_data(df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")


def display_data(df):
    # Here, you can implement your desired way to display the data, for example:
    print(df.head())  # Display first few rows of the DataFrame
    # You can further process or visualize the data as needed


def main():
    root = tk.Tk()
    root.title('Open Excel File')
    root.geometry('300x100')

    open_button = tk.Button(root, text='Open Excel File', command=open_excel_file)
    open_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
