import pandas as pd
import re

# 1. Mock shopify Dataset - no longer work for company and have no saved exports :( 
data = {
    'Product_Name': [
        'Stormblade 8ft Wood Graphic Foamie', 
        '7ft6 Performance Longboard - Blue', 
        'NSP Elements 9ft2 SUP', 
        'Al Merrick 5ft10 Fish Hardboard',
        'Soft-top Funboard 7ft 2in'
    ]
}
df = pd.DataFrame(data)

def advanced_taxonomy(name):
    name_clean = name.lower()
    
    # --- 1. Extract & Round Length ---
    # Regex looks for a digit followed by 'ft' (e.g., 7ft, 8ft)
    length_match = re.search(r'(\d+)ft', name_clean)
    # Also looks for inches if they exist (e.g., 6in, 11in)
    inch_match = re.search(r'(\d+)in', name_clean) or re.search(r'ft(\d+)', name_clean)
    
    length_val = int(length_match.group(1)) if length_match else None
    
    # Logic: "Anything in between goes to the nearest foot down" (per your instruction)
    # If it's 7ft6, length_val remains 7.
    length_tag = f"{length_val}ft" if length_val else "Unknown"

    # 2. Identify Board Type
    if any(x in name_clean for x in ['foamie', 'soft-top', 'softtop']):
        b_type = 'Foamie/Soft-top'
    elif 'sup' in name_clean:
        b_type = 'SUP'
    else:
        b_type = 'Hardboard'

    # 3. Identify Board Shape
    shapes = ['fish', 'funboard', 'shortboard', 'longboard']
    b_shape = 'Other'
    for s in shapes:
        if s in name_clean:
            b_shape = s.capitalize()
            break
            
    return pd.Series([length_tag, b_type, b_shape])

# 2. Execute engine
df[['Length_Cat', 'Board_Type', 'Shape']] = df['Product_Name'].apply(advanced_taxonomy)

# 3. Final Output
print(df)
