# GPS2Traj
A Simplified Python Version of https://github.com/cyang-kth/gps2traj

A Python-based command-line utility to convert raw GPS data into a trajectory format, suitable for further analysis or visualization. This tool reads GPS data from a CSV file, where each row represents a point with an ID, x and y coordinates, and a timestamp. The output is a CSV file with each row representing a LineString or trip, sorted by the timestamp and grouped by the ID.

# Key Features
CSV Input/Output: The tool accepts CSV files as input and produces CSV files as output, maintaining compatibility with various data processing workflows.
Custom Column Names: Users can specify the column names for ID, x, y, and timestamp, accommodating different data schemas.
Sorting and Grouping: The tool automatically sorts the GPS points by timestamp and groups them by ID for trajectory construction.
Simple LineString Output: The converted trajectories are output as LineStrings, a common format for representing sequences of geographic points.

# Installation
To use the GPS to Trajectory Converter, simply clone the repository and run the script with the necessary arguments. No installation is required.

git clone https://github.com/your-username/GPS2Traj.git
cd GPS2Traj
python convert_gps_to_traj.py -i /path/to/input.csv -o /path/to/output.csv -d ',' --id id_col -x x_col -y y_col -t timestamp_col

(Replace /path/to/input.csv and /path/to/output.csv with the paths to your input and output files, respectively. Use the -d flag to specify a delimiter if different from the default comma. Use the --id, -x, -y, and -t flags to specify the column names for ID, x-coordinate, y-coordinate, and timestamp.)

# Dependencies
Python 3.8 or higher
Pandas library (for data manipulation)

