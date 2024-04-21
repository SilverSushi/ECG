import os
import pandas as pd

def split(input_file, output_folder, rows_per_file):
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	chunk_size = rows_per_file
	chunks = pd.read_csv(input_file, chunksize=chunk_size)

	for i, chunk in enumerate(chunks):
		output_file = os.path.join(output_folder, f'split_{i+1}.csv')
		chunk.to_csv(output_file,index=False, header=(i==0))
		print(f'Saved {output_file}')

if __name__ == '__main__':
	base_path = 'csv_data'

	for i in range(1, 36):
		input_csv_file = os.path.join(base_path, f'x{i:02d}.csv')
		output_folder = os.path.join(base_path, f'x{i:02d}')
		rows_per_file = 6000

		split(input_csv_file, output_folder, rows_per_file)