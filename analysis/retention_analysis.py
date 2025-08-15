"""
E-commerce Customer Retention Analysis
Created with LLM assistance (ChatGPT Codex)
Analyst: 23f3003731@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load retention data
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Retention_Rate': [71.68, 72.07, 69.67, 71.91]
}

df = pd.DataFrame(data)
industry_target = 85.0

# Calculate key metrics
avg_retention = np.mean(df['Retention_Rate'])
performance_gap = industry_target - avg_retention

print(f"=== E-commerce Retention Analysis ===")
print(f"Average Retention Rate: {avg_retention:.2f}%")
print(f"Industry Target: {industry_target}%") 
print(f"Performance Gap: {performance_gap:.2f} percentage points")

# Statistical analysis
print(f"\nQuarterly Performance:")
for _, row in df.iterrows():
    print(f"{row['Quarter']}: {row['Retention_Rate']:.2f}%")

# Trend analysis
q_changes = df['Retention_Rate'].diff().fillna(0)
print(f"\nQuarter-over-Quarter Changes:")
for i, change in enumerate(q_changes):
    if i > 0:
        print(f"Q{i} to Q{i+1}: {change:+.2f}%")

# Key insights
print(f"\n=== KEY INSIGHTS ===")
print(f"• Critical performance gap: {performance_gap:.1f}pp below industry standard")
print(f"• Most volatile period: Q2-Q3 decline of {q_changes[2]:.2f}%")
print(f"• Solution required: implement targeted retention campaigns")
print(f"• Target improvement needed: +{performance_gap:.1f}pp to reach 85% benchmark")

# Create visualization
plt.figure(figsize=(12, 6))
plt.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=3, markersize=8, color='red', label='Actual Retention')
plt.axhline(y=industry_target, color='green', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target}%)')
plt.axhline(y=avg_retention, color='orange', linestyle=':', linewidth=2, label=f'Our Average ({avg_retention:.2f}%)')
plt.title('E-commerce Customer Retention Analysis - 2024', fontsize=16, fontweight='bold')
plt.ylabel('Retention Rate (%)')
plt.ylim(65, 90)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('retention_analysis_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"\nAnalysis completed by: 23f3003731@ds.study.iitm.ac.in")
print(f"LLM Assistance: ChatGPT Codex used for code generation and analysis")
