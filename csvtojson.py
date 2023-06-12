import json
import csv
import os





def csv_to_json(csv_file_path, json_file_path, num_rows):
    baseName= "part"
    json_file_count= 1
    rows_count=0
    with open(csv_file_path, 'r') as csv_file:
        csv_data = csv.DictReader(csv_file)
        rows = []
        for row in csv_data:
            if rows_count % num_rows == 0:
                if rows_count > 0:
                    json_file_count += 1

                json_file_path = f'{path}/{baseName}{json_file_count}.json'
                json_data = []

            raw_row = {}
            raw_row['SOC'] = row['SOC']
            raw_row['5yr-interest-avg'] = row['5yr-interest-avg']
            raw_row['12m-interest-avg'] = row['12m-interest-avg']
            raw_row['JobTitle'] = row['JobTitle']
            raw_row['JobOccupation'] = row['JobOccupation']
            raw_row['SimilarTitles'] = row['SimilarTitles'].replace(' , ', ',').replace("  ", "").split(',')
            raw_row['50GenSkills'] = row['50GenSkills'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['20SWSkills'] = row['20SWSkills'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['10ExpAch'] = row['10ExpAch'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['40ExpGen'] = row['40ExpGen'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['5SumEntry'] = row['5SumEntry'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['5SumJun'] = row['5SumJun'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['5SumAch'] = row['5SumAch'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['10SumGen'] = row['10SumGen'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['8Certs'] = row['8Certs'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['8Assoc'] = row['8Assoc'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['20Inter'] = row['20Inter'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['5SumSen'] = row['5SumSen'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['50ExpInt'] = row['50ExpInt'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['30SumInt'] = row['30SumInt'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['50ExpGrad'] = row['50ExpGrad'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')
            raw_row['30SumGrad'] = row['30SumGrad'].replace(" | ", "|").replace("| ", "|").replace(" |", "|").replace("   ", "").replace("  ", "").split('|')


            rows.append(raw_row)
            json_data.append(raw_row)
            rows_count += 1
            # if num_rows and len(rows) == num_rows:
            #     break
            if rows_count % num_rows == 0 or rows_count == csv_data.line_num - 1:
                with open(json_file_path, 'w') as json_file:
                    json.dump(json_data, json_file, indent=4)
    #     json_data = json.dumps(rows)

    # with open(json_file_path, 'w') as json_file:
    #     json_file.write(json_data)

# Usage example
csv_file_path = 'FinalData.csv'
json_file_path = 'example.json'
path = "output"
if not os.path.exists(path):
    os.mkdir(path)
num_rows = 1000
csv_to_json(csv_file_path, json_file_path, num_rows)
