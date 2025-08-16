import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_analyze_data():
    """Load retention data and perform comprehensive analysis"""
    
    # Load the data
    df = pd.read_csv('data/retention_data.csv')
    
    # Basic statistics
    print("=== CUSTOMER RETENTION ANALYSIS ===")
    print(f"Dataset shape: {df.shape}")
    print(f"\nQuarterly Retention Rates:")
    for _, row in df.iterrows():
        print(f"{row['Quarter']}: {row['Retention_Rate']:.2f}%")
    
    # Calculate key metrics
    average_retention = df['Retention_Rate'].mean()
    industry_target = 85.0
    gap_to_target = industry_target - average_retention
    
    print(f"\nKey Metrics:")
    print(f"Average Retention Rate: {average_retention:.2f}%")
    print(f"Industry Target: {industry_target:.2f}%")
    print(f"Gap to Target: {gap_to_target:.2f} percentage points")
    
    # Trend analysis
    retention_trend = df['Retention_Rate'].pct_change().fillna(0) * 100
    print(f"\nTrend Analysis:")
    for i, (_, row) in enumerate(df.iterrows()):
        if i > 0:
            change = retention_trend.iloc[i]
            direction = "↑" if change > 0 else "↓" if change < 0 else "→"
            print(f"{row['Quarter']}: {change:+.2f}% {direction}")
    
    return df, average_retention, industry_target, gap_to_target

def create_visualizations(df, average_retention, industry_target):
    """Create comprehensive visualizations for the analysis"""
    
    # 1. Quarterly Performance Line Chart
    plt.figure(figsize=(12, 8))
    plt.plot(df['Quarter'], df['Retention_Rate'], 
             marker='o', linewidth=3, markersize=8, 
             color='#2E8B57', label='Actual Retention Rate')
    plt.axhline(y=average_retention, color='#FF6B6B', 
                linestyle='--', linewidth=2, label=f'Average ({average_retention:.2f}%)')
    plt.axhline(y=industry_target, color='#4ECDC4', 
                linestyle='-', linewidth=2, label=f'Industry Target ({industry_target}%)')
    
    plt.title('Customer Retention Rate - 2024 Quarterly Performance', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Quarter', fontsize=12, fontweight='bold')
    plt.ylabel('Retention Rate (%)', fontsize=12, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.ylim(65, 90)
    
    # Add value labels on data points
    for i, row in df.iterrows():
        plt.annotate(f'{row["Retention_Rate"]:.2f}%', 
                    (row['Quarter'], row['Retention_Rate']),
                    textcoords="offset points", xytext=(0,10), ha='center',
                    fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('visualizations/quarterly_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Benchmark Comparison Bar Chart
    plt.figure(figsize=(10, 6))
    categories = ['Current Average', 'Industry Target']
    values = [average_retention, industry_target]
    colors = ['#FF6B6B', '#4ECDC4']
    
    bars = plt.bar(categories, values, color=colors, alpha=0.8, width=0.6)
    plt.title('Retention Rate: Current vs Industry Benchmark', 
              fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Retention Rate (%)', fontsize=12, fontweight='bold')
    plt.ylim(60, 90)
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{value:.2f}%', ha='center', va='bottom', fontweight='bold')
    
    # Add gap annotation
    plt.annotate(f'Gap: {industry_target - average_retention:.2f}pp', 
                xy=(0.5, (average_retention + industry_target)/2), 
                xytext=(0.5, (average_retention + industry_target)/2 + 3),
                ha='center', fontweight='bold', color='red',
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    
    plt.tight_layout()
    plt.savefig('visualizations/benchmark_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Retention Trend with Annotations
    plt.figure(figsize=(14, 8))
    plt.plot(df['Quarter'], df['Retention_Rate'], 
             marker='s', linewidth=4, markersize=10, 
             color='#2E8B57', markerfacecolor='white', 
             markeredgewidth=2, markeredgecolor='#2E8B57')
    
    plt.fill_between(df['Quarter'], df['Retention_Rate'], 
                     alpha=0.3, color='#2E8B57')
    
    plt.axhline(y=industry_target, color='#4ECDC4', 
                linestyle='-', linewidth=3, alpha=0.7, 
                label=f'Industry Target ({industry_target}%)')
    
    plt.title('Customer Retention Trend Analysis - 2024', 
              fontsize=18, fontweight='bold', pad=25)
    plt.xlabel('Quarter', fontsize=14, fontweight='bold')
    plt.ylabel('Retention Rate (%)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.ylim(65, 90)
    
    # Add detailed annotations
    annotations = [
        (0, "Q1: Starting point\n71.68%"),
        (1, "Q2: Slight improvement\n+0.39pp"),
        (2, "Q3: Significant drop\n-2.40pp"),
        (3, "Q4: Recovery attempt\n+2.24pp")
    ]
    
    for i, (idx, text) in enumerate(annotations):
        plt.annotate(text, (df.iloc[idx]['Quarter'], df.iloc[idx]['Retention_Rate']),
                    xytext=(20, 20 if i % 2 == 0 else -30), 
                    textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    plt.tight_layout()
    plt.savefig('visualizations/retention_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Dashboard-style Summary
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Quarterly bars
    ax1.bar(df['Quarter'], df['Retention_Rate'], color='#2E8B57', alpha=0.8)
    ax1.axhline(y=industry_target, color='red', linestyle='--', linewidth=2)
    ax1.set_title('Quarterly Performance', fontweight='bold')
    ax1.set_ylabel('Retention Rate (%)')
    
    # Gap analysis
    gap_data = [industry_target - rate for rate in df['Retention_Rate']]
    ax2.bar(df['Quarter'], gap_data, color='#FF6B6B', alpha=0.8)
    ax2.set_title('Gap to Industry Target', fontweight='bold')
    ax2.set_ylabel('Gap (percentage points)')
    
    # Trend line
    ax3.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=3, markersize=8)
    ax3.fill_between(df['Quarter'], df['Retention_Rate'], alpha=0.3)
    ax3.set_title('Retention Trend', fontweight='bold')
    ax3.set_ylabel('Retention Rate (%)')
    
    # Summary stats
    ax4.axis('off')
    summary_text = f"""
    KEY METRICS SUMMARY
    
    Average Retention: {average_retention:.2f}%
    Industry Target: {industry_target:.2f}%
    Gap to Target: {industry_target - average_retention:.2f}pp
    
    Volatility: {df['Retention_Rate'].std():.2f}%
    Best Quarter: {df.loc[df['Retention_Rate'].idxmax(), 'Quarter']} ({df['Retention_Rate'].max():.2f}%)
    Worst Quarter: {df.loc[df['Retention_Rate'].idxmin(), 'Quarter']} ({df['Retention_Rate'].min():.2f}%)
    
    URGENT ACTION REQUIRED
    """
    ax4.text(0.1, 0.9, summary_text, transform=ax4.transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    plt.suptitle('Customer Retention Dashboard - 2024 Analysis', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('visualizations/dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ All visualizations created successfully!")

def generate_insights(df, average_retention, industry_target, gap_to_target):
    """Generate actionable insights from the analysis"""
    
    print("\n=== ACTIONABLE INSIGHTS ===")
    
    # Performance insights
    best_quarter = df.loc[df['Retention_Rate'].idxmax()]
    worst_quarter = df.loc[df['Retention_Rate'].idxmin()]
    volatility = df['Retention_Rate'].std()
    
    insights = {
        'performance': {
            'average': average_retention,
            'target': industry_target,
            'gap': gap_to_target,
            'best_quarter': best_quarter,
            'worst_quarter': worst_quarter,
            'volatility': volatility
        },
        'trends': {
            'q1_to_q2': df.iloc[1]['Retention_Rate'] - df.iloc[0]['Retention_Rate'],
            'q2_to_q3': df.iloc[2]['Retention_Rate'] - df.iloc[1]['Retention_Rate'],
            'q3_to_q4': df.iloc[3]['Retention_Rate'] - df.iloc[2]['Retention_Rate'],
        }
    }
    
    print(f"1. PERFORMANCE GAP: {gap_to_target:.2f} percentage points below industry standard")
    print(f"2. VOLATILITY: High variance ({volatility:.2f}%) indicates unstable retention")
    print(f"3. Q3 CRISIS: Significant {insights['trends']['q2_to_q3']:.2f}pp drop needs investigation")
    print(f"4. RECOVERY SIGNAL: Q4 showed {insights['trends']['q3_to_q4']:+.2f}pp improvement")
    
    return insights

def calculate_business_impact(average_retention, industry_target):
    """Calculate the business impact of retention gap"""
    
    print("\n=== BUSINESS IMPACT ANALYSIS ===")
    
    # Assumptions for impact calculation
    avg_customer_value = 500  # Annual customer value
    total_customers = 10000   # Customer base
    
    current_retained = total_customers * (average_retention / 100)
    target_retained = total_customers * (industry_target / 100)
    lost_revenue = (target_retained - current_retained) * avg_customer_value
    
    print(f"Annual Revenue Impact:")
    print(f"• Current retained customers: {current_retained:,.0f}")
    print(f"• Target retained customers: {target_retained:,.0f}")
    print(f"• Lost customers: {target_retained - current_retained:,.0f}")
    print(f"• Lost annual revenue: ${lost_revenue:,.0f}")
    
    return lost_revenue

def main():
    """Main analysis pipeline"""
    print("Starting Customer Retention Analysis...")
    print("=" * 50)
    
    # Load and analyze data
    df, average_retention, industry_target, gap_to_target = load_and_analyze_data()
    
    # Create visualizations
    create_visualizations(df, average_retention, industry_target)
    
    # Generate insights
    insights = generate_insights(df, average_retention, industry_target, gap_to_target)
    
    # Calculate business impact
    lost_revenue = calculate_business_impact(average_retention, industry_target)
    
    print("\n" + "=" * 50)
    print("Analysis completed successfully!")
    print("Check the 'visualizations' folder for charts and graphs.")

if __name__ == "__main__":
    main()
