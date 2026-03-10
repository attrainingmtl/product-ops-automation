import pandas as pd

# 1. mini mock Shopify export - (no longer work for company and don't have saved exports :(
data = {
    'Product_Name': ['O'Neill Mutant', 'Catch Surf Log', 'Rip Curl Flashbomb'],
    'Description': [
        'Mens 5/4mm hooded wetsuit for cold water surfing.',
        'Beginner surfboard 8ft foamie with fins included.',
        'High performance 3/2mm steamer for summer sessions.'
    ]
}
df = pd.DataFrame(data)

# 2. Define the Taxonomy Logic
def categorize_product(description):
    desc = description.lower()
    
    # Logic to identify 'Category'
    if 'wetsuit' in desc or 'steamer' in desc:
        category = 'Apparel'
    elif 'surfboard' in desc or 'foamie' in desc:
        category = 'Hardgoods'
    else:
        category = 'Other'
        
    # Logic to identify 'Skill Level'
    level = 'Intermediate/Pro'
    if 'beginner' in desc or 'soft' in desc:
        level = 'Beginner'
        
    return pd.Series([category, level])

# 3. Apply taxonomy logic to dataframe
df[['Category', 'Skill_Level']] = df['Description'].apply(categorize_product)

# 4. Show the clean result
print(df[['Product_Name', 'Category', 'Skill_Level']])
