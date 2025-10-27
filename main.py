import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = r'C:\Users\hunte\Desktop\high_leverage_relievers\2025_relievers_wp.csv'
df_relievers_full = pd.read_csv(csv_file_path)

df_relievers = df_relievers_full[['Name', 'Team', 'WPA', 'pLI']]

team_colors = {
    'NYY': '#132440', 
    'BOS': '#BD3039',  
    'HOU': "#F4911E",  
    'LAD': '#005A9C',  
    'PHI': '#E81828',  
    'TBR': "#75AEE4",  
    'TOR': '#134A8E',  
    'ARI': '#A71930',
    'ATL': '#CE1141',
    'BAL': '#DF4601',
    'CHC': '#0E3386',
    'CHW': '#27251F',
    'CIN': '#C6011F',
    'CLE': '#E50022',
    'COL': '#333366',
    'DET': '#0C2340',
    'KCR': '#004687',
    'LAA': '#BA0021',
    'MIA': '#00A3E0',
    'MIL': '#ffc52f',
    'MIN': '#002B5C',
    'NYM': '#FF5910',
    'ATH': '#003831',
    'PIT': '#FDB827',
    'SDP': '#2F241D',
    'SFG': '#FD5A1E',
    'SEA': '#005C5C',
    'STL': '#C41E3A',
    'TEX': '#003278',
    'WSN': '#AB0003'
}
df_relievers['Last Name'] = df_relievers['Name'].str.split(' ').str[-1]
# 1. Filter for the top 30 relievers by WPA
# The .sort_values() method is used to sort the DataFrame.
# The .head(30) method then selects the first 30 rows of the sorted DataFrame.
df_top_30_wpa = df_relievers.sort_values(by='WPA', ascending=False).head(30)

# Calculate average WPA and pLI
avg_wpa = df_top_30_wpa['WPA'].mean()
avg_pli = df_top_30_wpa['pLI'].mean()

fig, ax = plt.subplots(figsize=(15, 10))

for index, row in df_top_30_wpa.iterrows():
    color = team_colors.get(row['Team'], '#808080')
    ax.scatter(row['pLI'], row['WPA'], color=color, s=50)
    ax.text(row['pLI'], row['WPA'], f" {row['Last Name']}", fontsize=8, ha='left', va='center', color=color)

# Add quadrant lines and labels
ax.axvline(avg_pli, color='black', linestyle='--', lw=1)
ax.axhline(avg_wpa, color='black', linestyle='--', lw=1)

ax.set_title('Top 30 Relievers by WPA', fontsize=16, weight='bold')
ax.set_xlabel('pLI (Average Leverage Index)', fontsize=12, weight='bold')
ax.set_ylabel('WPA (Win Probability Added)', fontsize=12, weight ='bold')
plt.tight_layout()
plt.show()

