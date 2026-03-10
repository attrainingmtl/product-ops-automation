import matplotlib.pyplot as plt


# We sort descending so the most important categories are first
shape_counts = df['Shape'].value_counts().sort_values(ascending=False)


plt.figure(figsize=(10, 6))
shape_counts.plot(kind='bar', color='skyblue', edgecolor='black')


plt.title('Inventory Distribution by Board Shape', fontsize=14, fontweight='bold')
plt.xlabel('Board Shape', fontsize=12)
plt.ylabel('Total Units (SKUs)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


plt.savefig('inventory_distribution.png')
print("Business Intelligence Report Generated.")
