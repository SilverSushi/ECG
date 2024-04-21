import os
import pandas as pd

def delextrasub(base_directory):
	for subject_number in range(1, 36):
		subject_folder = f'x{subject_number:02d}'
		directory_path = os.path.join(base_directory, subject_folder)

		max_files_csv = f'x{subject_number:02d}apn.csv'
		max_files_folder_path = 'apnlabel_data'
		specific_csv_file = os.path.join(max_files_folder_path, max_files_csv)

		if os.path.exists(directory_path):
			delextra(directory_path, specific_csv_file)
		else:
			print('nah')

def delextra(directory_path, max_files_csv):
	csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
	max_allowed_files_df = pd.read_csv(max_files_csv, header=None)
	max_allowed_files = max_allowed_files_df.shape[0]

	if len(csv_files) > max_allowed_files:
		sorted_files = sorted(csv_files, key=lambda x: int(x.split('_')[1].split('.')[0]), reverse=True)
		files_to_delete = sorted_files[:-max_allowed_files]


		if files_to_delete:
			print(f'Deleting excess files in {directory_path} :')
			for files_to_delete in files_to_delete:
				print(files_to_delete)
				file_path = os.path.join(directory_path, files_to_delete)
				os.remove(file_path)

			print(f'\n{len(files_to_delete)} excess files deleted')
		else:
			print('No files deleted')
	else:
		print('No files deleted')

base_directory = 'csv_data'
delextrasub(base_directory)