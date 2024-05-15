import pandas as pd
import os

class U_Sort:
    @staticmethod
    def sort_excel_file():
        # Read the Excel file and store the data in a pandas DataFrame
        def read_data(file_name):
            return pd.read_excel(file_name)

        # Define a function to sort the data
        def sort_data(data, column, order):
            if order == 'asc':
                return data.sort_values(by=column)
            elif order == 'desc':
                return data.sort_values(by=column, ascending=False)
            else:
                print("Invalid order. Please choose 'asc' or 'desc'.")

        # Function to save sorted data to a new Excel file
        def save_as_excel(file_name, sorted_data):
            new_file_name = input("Enter the new file name (including .xlsx extension): ")
            sorted_data.to_excel(new_file_name, index=False)
            print(f"Sorted data saved to {new_file_name}.")

        # Function to overwrite original Excel file with sorted data
        def save_overwrite_excel(file_name, sorted_data):
            sorted_data.to_excel(file_name, index=False)
            print(f"Sorted data overwritten to {file_name}.")

        # Get user input for file name, column, and order
        file_name = input("Enter the file name (including .xlsx extension): ")
        column = input("Choose a column to sort (NIM, NAMA, NILAI): ")
        order = input("Choose an order (asc, desc): ")

        # Read the data from the Excel file
        data = read_data(file_name)

        # Sort the data
        sorted_data = sort_data(data, column, order)

        # Check if sorting is successful before saving
        if sorted_data is not None:
            # Ask user for saving option
            save_option = input("Choose an option:\n1. Save as (With new name)\n2. Save (Overwrite)\nEnter the option number: ")
            
            if save_option == '1':
                save_as_excel(file_name, sorted_data)
            elif save_option == '2':
                save_overwrite_excel(file_name, sorted_data)
            else:
                print("Invalid option. Please choose 1 or 2.")

        # Print the sorted data
        print(sorted_data.to_string(index=False))

    @staticmethod
    def sort_text_file():
        # Read the file and store the data in a list of dictionaries
        def read_data(file_name):
            with open(file_name, 'r') as f:
                headers = f.readline().strip().split()
                data = []
                for line in f:
                    row = line.strip().split()
                    data.append({header: value for header, value in zip(headers, row)})
            return data

        # Define a function to sort the data
        def sort_data(data, column, order):
            if order == 'asc':
                sorted_data = sorted(data, key=lambda x: x[column])
            elif order == 'desc':
                sorted_data = sorted(data, key=lambda x: x[column], reverse=True)
            else:
                print("Invalid order. Please choose 'asc' or 'desc'.")
                return None
            return sorted_data

        # Function to save sorted data to a new file
        def save_as(file_name, sorted_data):
            new_file_name = input("Enter the new file name (including .txt extension): ")
            with open(new_file_name, 'w') as f:
                # Write headers
                f.write('\t'.join(sorted_data[0].keys()) + '\n')
                # Write sorted data
                for row in sorted_data:
                    f.write('\t'.join(row.values()) + '\n')
            print(f"Sorted data saved to {new_file_name}.")

        # Function to overwrite original file with sorted data
        def save_overwrite(file_name, sorted_data):
            with open(file_name, 'w') as f:
                # Write headers
                f.write('\t'.join(sorted_data[0].keys()) + '\n')
                # Write sorted data
                for row in sorted_data:
                    f.write('\t'.join(row.values()) + '\n')
            print(f"Sorted data overwritten to {file_name}.")

        # Get user input for file name, column, and order
        file_name = input("Enter the file name (including .txt extension): ")
        column = input("Choose a column to sort (NIM, NAMA, NILAI): ")
        order = input("Choose an order (asc, desc): ")

        # Read the data from the file
        data = read_data(file_name)

        # Sort the data
        sorted_data = sort_data(data, column, order)

        # Check if sorting is successful before saving
        if sorted_data:
            # Ask user for saving option
            save_option = input("Choose an option:\n1. Save as (With new name)\n2. Save (Overwrite)\nEnter the option number: ")
            
            if save_option == '1':
                save_as(file_name, sorted_data)
            elif save_option == '2':
                save_overwrite(file_name, sorted_data)
            else:
                print("Invalid option. Please choose 1 or 2.")

        # Print sorted data
        for row in sorted_data:
            print("{:<10} {:<15} {:<5}".format(row['NIM'], row['NAMA'], row['NILAI']))

    @staticmethod
    def sorting_menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nMenu Sorting dari Data file:")
            print("1. Sorting dari file Excel")
            print("2. Sorting dari file teks")
            print("3. Kembali ke menu utama")

            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                U_Sort.sort_excel_file()
                input("Tekan Enter untuk kembali ke menu Sorting.")
            elif pilihan == '2':
                # Panggil fungsi sorting untuk file teks jika diperlukan
                U_Sort.sort_text_file()
                input("Tekan Enter untuk kembali ke menu Sorting.")
            elif pilihan == '3':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
