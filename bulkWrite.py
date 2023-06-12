from pymongo import InsertOne, MongoClient
from pymongo.errors import BulkWriteError
import json
import os
# Upload JSON to MongoDB collection in bulk
def upload_to_mongodb(json_data, collection_name):
    client = MongoClient('mongodb+srv://techloset:techloset1214@cluster0.zkvgw.mongodb.net/resumas?retryWrites=true&w=majority')
    db = client['resumas']
    collection = db[collection_name]
    
    bulk_operations = [InsertOne(doc) for doc in json_data]
    failed_documents = bulk_operations[:]  # Copy all documents initially
    
    while failed_documents:
        try:
            result = collection.bulk_write(failed_documents, ordered=False)
            print(f"Inserted {result.inserted_count} documents.")
            break  # Exit the loop if all documents are inserted successfully
        except BulkWriteError as e:
            print(f"BulkWriteError occurred: {e.details}")
            failed_documents = [bulk_operations[idx] for idx in e.details['writeErrors']]
    
    client.close()

# Rest of the code remains the same...

# Path to your CSV file
# csv_file_path = '<path_to_your_csv_file>'

# # Collection name in MongoDB
collection_name = 'suggestionTest'

# # Convert CSV to JSON
# json_data = csv_to_json(csv_file_path)

# jsonFile = open('output/part1.json', 'r')
# json_data = json.load(jsonFile)

# # Upload JSON to MongoDB
# upload_to_mongodb(json_data, collection_name)

# all json files in the folder

json_folder = 'output'
json_files = [pos_json for pos_json in os.listdir(json_folder) if pos_json.endswith('.json')]
for json_file in json_files:
    jsonFile = open(json_folder + '/' + json_file, 'r')
    json_data = json.load(jsonFile)
    upload_to_mongodb(json_data, collection_name)
    print(json_file + ' uploaded to MongoDB')
