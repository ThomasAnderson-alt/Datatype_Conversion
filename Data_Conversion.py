import json
import re
import csv

# Simple JS to CSV converter
def js_to_csv():
    # Read and clean JS file
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any trailing semicolon if present
    content = content.strip().rstrip(';')
    # Fix unquoted property names
    content = re.sub(r'(\w+):', r'"\1":', content)
    data = json.loads(content)
    
    # Flatten hierarchy to rows
    rows = []
    def flatten(item, path=[]):
        current = path + [item['name']]
        if not item.get('childrenList'):
            rows.append(current)
        else:
            for child in item['childrenList']:
                flatten(child, current)
    
    for item in data:
        flatten(item)
    
    # Write to CSV with grouped formatting
    with open('medical_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        
        # Track previous values to avoid repetition
        prev_row = []
        
        for row in rows:
            # Create output row with blanks for repeated values
            output_row = []
            for i, value in enumerate(row):
                if i < len(prev_row) and value == prev_row[i]:
                    output_row.append('')  # Empty cell for repeated values
                else:
                    output_row.append(value)
                    # Clear subsequent previous values when a change occurs
                    prev_row = prev_row[:i+1]
            
            writer.writerow(output_row)
            prev_row = row.copy()  # Update previous row

js_to_csv()
