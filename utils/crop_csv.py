import csv
from datetime import datetime, timedelta

def crop_file(input_file_path, time_gap_minutes):
    output_file_path = "cropped_export_file.csv"
    time_gap = timedelta(minutes=time_gap_minutes)
    
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Timestamp', 'Text'])  # Write header
        
        start_time = None
        for line in input_file:
            timestamp_str, text = line.strip().split(',', 1)  # Assuming CSV format
            
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            if start_time is None:
                start_time = timestamp
                writer.writerow([timestamp_str, text])
            elif timestamp - start_time <= time_gap:
                writer.writerow([timestamp_str, text])
            else:
                break

# Example usage:
crop_file("input_text_file.txt", 10)  # Crop file with a time gap of 10 minutes
