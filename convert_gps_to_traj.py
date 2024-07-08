import pandas as pd

def convert_gps_to_traj(input_file, output_file, delimiter=',', id_col='id', x_col='x', y_col='y', timestamp_col='timestamp'):
    """
    Convert GPS data into trajectory format.
    
    Parameters:
    - input_file: str, path to the input CSV file with GPS data.
    - output_file: str, path to the output CSV file with trajectory data.
    - delimiter: str, delimiter character used in the CSV file (default is ',').
    - id_col: str, name of the column containing the ID field.
    - x_col: str, name of the column containing the X coordinate.
    - y_col: str, name of the column containing the Y coordinate.
    - timestamp_col: str, name of the column containing the timestamp.
    """
    # Read the GPS data from the CSV file
    df = pd.read_csv(input_file, delimiter=delimiter)
    
    # Ensure the timestamp column is of integer type (Unix timestamp)
    if df[timestamp_col].dtype == 'object':
        df[timestamp_col] = pd.to_numeric(df[timestamp_col], errors='coerce').astype(int)
    
    # Sort the data by the timestamp column
    df = df.sort_values(timestamp_col)
    
    # Group the data by the ID field
    grouped = df.groupby(id_col)
    
    # Write the trajectory data to the output CSV file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("index;id;geom\n")
        for index, (id, group) in enumerate(grouped, start=1):
            # Convert the sorted points to LineString format
            line_string = ",".join(f"{group[x_col].iloc[i]} {group[y_col].iloc[i]}" for i in range(len(group)))
            f.write(f"{index};{id};LineString({line_string})\n")

# Example usage
if __name__ == "__main__":
    # Define the file paths and column names
    input_file_path = 'path_to_your_input_file.csv'  # Replace with the actual file path
    output_file_path = 'path_to_your_output_file.csv'  # Replace with the desired output file path
    id_column_name = 'your_id_column_name'  # Replace with the actual ID column name
    x_column_name = 'your_x_column_name'  # Replace with the actual X column name
    y_column_name = 'your_y_column_name'  # Replace with the actual Y column name
    timestamp_column_name = 'your_timestamp_column_name'  # Replace with the actual timestamp column name

    # Call the function with the specified parameters
    convert_gps_to_traj(input_file_path, output_file_path, 
                        id_col=id_column_name, x_col=x_column_name, 
                        y_col=y_column_name, timestamp_col=timestamp_column_name)
