"""
E-commerce Customer Retention Analysis
=====================================

This script analyzes quarterly customer retention data for 2024 
and generates visualizations comparing performance against industry benchmarks.

Author: 23f3003731@ds.study.iitm.ac.in
Date: August 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class RetentionAnalyzer:
    """
    A class to analyze customer retention data and generate insights
    """
    
    def __init__(self):
        """Initialize the analyzer with 2024 quarterly retention data"""
        # Quarterly retention data for 2024
        self.data = {
            'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
            'Retention_Rate': [71.68, 72.07, 69.67, 71.91],
            'Month': [1, 2, 3, 4]  # For trend analysis
        }
        
        # Industry benchmark and targets
        self.industry_target = 85.0
        self.df = pd.DataFrame(self.data)
        
        # Calculate key metrics
        self.avg_retention = np.mean(self.data['Retention_Rate'])
        self.performance_gap = self.industry_target - self.avg_retention
        
        print(f"=== E-commerce Retention Analysis Initialized ===")
        print(f"Average Retention Rate: {self.avg_retention:.2f}%")
        print(f"Industry Target: {self.industry_target}%")
        print(f"Performance Gap: {self.performance_gap:.2f} percentage points")
        print("=" * 50)
    
    def calculate_statistics(self):
        """Calculate comprehensive statistics for the retention data"""
        stats = {
            'mean': np.mean(self.data['Retention_Rate']),
            'median': np.median(self.data['Retention_Rate']),
            'std': np.std(self.data['Retention_Rate']),
            'min': np.min(self.data['Retention_Rate']),
            'max': np.max(self.data['Retention_Rate']),
            'range': np.max(self.data['Retention_Rate']) - np.min(self.data['Retention_Rate']),
            'cv': (np.std(self.data['Retention_Rate']) / np.mean(self.data['Retention_Rate'])) * 100
        }
        
        print("\n=== Statistical Summary ===")
        print(f"Mean Retention Rate: {stats['mean']:.2f}%")
        print(f"Median Retention Rate: {stats['median']:.2f}%")
        print(f"Standard Deviation: {stats['std']:.2f}%")
        print(f"Range: {stats['range']:.2f}% (Min: {stats['min']:.2f}%, Max: {stats['max']:.2f}%)")
        print(f"Coefficient of Variation: {stats['cv']:.2f}%")
        
        return stats
    
    def create_trend_visualization(self, save_path='visualizations/retention_trend.png'):
        """Create a comprehensive trend visualization"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot 1: Quarterly Trend with Benchmark
        quarters = self.df['Quarter']
        retention_rates = self.df['Retention_Rate']
        
        # Line plot for trend
        ax1.plot(quarters, retention_rates, marker='o', linewidth=3, markersize=8, 
                color='#e74c3c', label='Actual Retention Rate')
        
        # Industry benchmark line
        ax1.axhline(y=self.industry_target, color='#27ae60', linestyle='--', 
                   linewidth=2, label=f'Industry Target ({self.industry_target}%)')
        
        # Average line
        ax1.axhline(y=self.avg_retention, color='#f39c12', linestyle=':', 
                   linewidth=2, label=f'Our Average ({self.avg_retention:.2f}%)')
        
        # Formatting
        ax1.set_title('Customer Retention Rate - 2024 Quarterly Performance', 
                     fontsize=16, fontweight='bold', pad=20)
        ax1.set_ylabel('Retention Rate (%)', fontsize=12)
        ax1.set_ylim(65, 90)
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=10)
        
        # Add value labels on points
        for i, (quarter, rate) in enumerate(zip(quarters, retention_rates)):
            ax1.annotate(f'{rate:.2f}%', (i, rate), textcoords="offset points", 
                        xytext=(0,10), ha='center', fontweight='bold')
        
        # Plot 2: Gap Analysis
        gaps = [self.industry_target - rate for rate in retention_rates]
        colors = ['#e74c3c' if gap > 0 else '#27ae60' for gap in gaps]
        
        bars = ax2.bar(quarters, gaps, color=colors, alpha=0.7, edgecolor='black')
        ax2.set_title('Performance Gap vs Industry Target', fontsize=16, fontweight='bold', pad=20)
        ax2.set_ylabel('Gap (Percentage Points)', fontsize=12)
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax2.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar, gap in zip(bars, gaps):
            height = bar.get_height()
            ax2.annotate(f'{gap:.2f}pp', xy=(bar.get_x() + bar.get_width()/2, height),
                        xytext=(0, 3 if height > 0 else -15), textcoords="offset points",
                        ha='center', va='bottom' if height > 0 else 'top', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Trend visualization saved to: {save_path}")
    
    def create_performance_dashboard(self, save_path='visualizations/dashboard.png'):
        """Create a comprehensive performance dashboard"""
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # 1. Main trend chart
        ax1 = fig.add_subplot(gs[0, :2])
        quarters = self.df['Quarter']
        retention_rates = self.df['Retention_Rate']
        
        ax1.plot(quarters, retention_rates, marker='o', linewidth=4, markersize=10, 
                color='#3498db', label='Actual Performance')
        ax1.axhline(y=self.industry_target, color='#27ae60', linestyle='--', 
                   linewidth=3, label=f'Target ({self.industry_target}%)')
        ax1.fill_between(quarters, retention_rates, alpha=0.3, color='#3498db')
        ax1.set_title('2024 Retention Performance Trend', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Retention Rate (%)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Key metrics summary
        ax2 = fig.add_subplot(gs[0, 2])
        ax2.axis('off')
        metrics_text = f"""
        KEY METRICS
        
        Average: {self.avg_retention:.2f}%
        Target: {self.industry_target}%
        Gap: {self.performance_gap:.2f}pp
        
        Best Quarter: Q2 ({max(retention_rates):.2f}%)
        Worst Quarter: Q3 ({min(retention_rates):.2f}%)
        Volatility: {np.std(retention_rates):.2f}%
        """
        ax2.text(0.1, 0.9, metrics_text, transform=ax2.transAxes, fontsize=11,
                verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
        
        # 3. Quarter-over-Quarter change
        ax3 = fig.add_subplot(gs[1, 0])
        qoq_changes = [0] + [retention_rates[i] - retention_rates[i-1] for i in range(1, len(retention_rates))]
        colors = ['green' if x >= 0 else 'red' for x in qoq_changes]
        ax3.bar(quarters, qoq_changes, color=colors, alpha=0.7)
        ax3.set_title('Quarter-over-Quarter Changes', fontsize=12, fontweight='bold')
        ax3.set_ylabel('Change (%)')
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax3.tick_params(axis='x', rotation=45)
        
        # 4. Performance vs Target comparison
        ax4 = fig.add_subplot(gs[1, 1])
        x_pos = np.arange(len(quarters))
        width = 0.35
        ax4.bar(x_pos - width/2, retention_rates, width, label='Actual', color='#e74c3c', alpha=0.8)
        ax4.bar(x_pos + width/2, [self.industry_target]*len(quarters), width, 
               label='Target', color='#27ae60', alpha=0.8)
        ax4.set_title('Actual vs Target Comparison', fontsize=12, fontweight='bold')
        ax4.set_ylabel('Retention Rate (%)')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(quarters, rotation=45)
        ax4.legend()
        
        # 5. Cumulative gap analysis
        ax5 = fig.add_subplot(gs[1, 2])
        cumulative_gap = np.cumsum([self.industry_target - rate for rate in retention_rates])
        ax5.plot(quarters, cumulative_gap, marker='s', linewidth=3, markersize=8, color='#e67e22')
        ax5.fill_between(quarters, cumulative_gap, alpha=0.3, color='#e67e22')
        ax5.set_title('Cumulative Performance Gap', fontsize=12, fontweight='bold')
        ax5.set_ylabel('Cumulative Gap (pp)')
        ax5.tick_params(axis='x', rotation=45)
        ax5.grid(True, alpha=0.3)
        
        # 6. Distribution analysis
        ax6 = fig.add_subplot(gs[2, :])
        # Create a histogram showing retention rate distribution
        ax6.hist(retention_rates, bins=8, color='skyblue', alpha=0.7, edgecolor='black')
        ax6.axvline(self.avg_retention, color='red', linestyle='--', linewidth=2, 
                   label=f'Our Average ({self.avg_retention:.2f}%)')
        ax6.axvline(self.industry_target, color='green', linestyle='--', linewidth=2, 
                   label=f'Industry Target ({self.industry_target}%)')
        ax6.set_title('Retention Rate Distribution Analysis', fontsize=12, fontweight='bold')
        ax6.set_xlabel('Retention Rate (%)')
        ax6.set_ylabel('Frequency')
        ax6.legend()
        
        plt.suptitle('E-commerce Customer Retention Performance Dashboard - 2024', 
                    fontsize=18, fontweight='bold', y=0.98)
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Performance dashboard saved to: {save_path}")
    
    def create_interactive_plotly_chart(self, save_path='visualizations/interactive_retention.html'):
        """Create an interactive Plotly visualization"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Quarterly Trend', 'Performance Gap', 'Cumulative Analysis', 'Target Achievement'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        quarters = self.df['Quarter']
        retention_rates = self.df['Retention_Rate']
        
        # 1. Quarterly Trend
        fig.add_trace(
            go.Scatter(x=quarters, y=retention_rates, mode='lines+markers',
                      name='Actual Retention', line=dict(color='#e74c3c', width=3),
                      marker=dict(size=10)),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=quarters, y=[self.industry_target]*len(quarters),
                      mode='lines', name='Industry Target', 
                      line=dict(color='#27ae60', width=2, dash='dash')),
            row=1, col=1
        )
        
        # 2. Performance Gap
        gaps = [self.industry_target - rate for rate in retention_rates]
        colors = ['red' if gap > 0 else 'green' for gap in gaps]
        fig.add_trace(
            go.Bar(x=quarters, y=gaps, name='Performance Gap',
                  marker_color=colors, opacity=0.7),
            row=1, col=2
        )
        
        # 3. Cumulative Analysis
        cumulative_retention = np.cumsum(retention_rates)
        cumulative_target = np.cumsum([self.industry_target]*len(quarters))
        fig.add_trace(
            go.Scatter(x=quarters, y=cumulative_retention, mode='lines+markers',
                      name='Cumulative Actual', line=dict(color='#3498db', width=3)),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=quarters, y=cumulative_target, mode='lines',
                      name='Cumulative Target', line=dict(color='#27ae60', width=2, dash='dot')),
            row=2, col=1
        )
        
        # 4. Target Achievement Percentage
        achievement_pct = [(rate/self.industry_target)*100 for rate in retention_rates]
        fig.add_trace(
            go.Bar(x=quarters, y=achievement_pct, name='Target Achievement %',
                  marker_color='lightblue', opacity=0.8),
            row=2, col=2
        )
        fig.add_hline(y=100, line_dash="dash", line_color="green", row=2, col=2)
        
        # Update layout
        fig.update_layout(
            title_text="Interactive E-commerce Retention Analysis Dashboard",
            title_x=0.5,
            showlegend=True,
            height=800,
            template="plotly_white"
        )
        
        # Save and show
        fig.write_html(save_path)
        fig.show()
        print(f"Interactive chart saved to: {save_path}")
    
    def generate_insights_report(self):
        """Generate detailed insights and recommendations"""
        stats = self.calculate_statistics()
        
        print("\n" + "="*60)
        print("AUTOMATED INSIGHTS REPORT")
        print("="*60)
        
        # Key findings
        print(f"\n📊 PERFORMANCE ANALYSIS:")
        print(f"   • Current average retention: {self.avg_retention:.2f}%")
        print(f"   • Industry benchmark: {self.industry_target}%")
        print(f"   • Performance gap: {self.performance_gap:.2f} percentage points")
        print(f"   • Quarterly volatility: {stats['std']:.2f}% (CV: {stats['cv']:.1f}%)")
        
        # Quarter analysis
        best_q = self.df.loc[self.df['Retention_Rate'].idxmax(), 'Quarter']
        worst_q = self.df.loc[self.df['Retention_Rate'].idxmin(), 'Quarter']
        best_rate = self.df['Retention_Rate'].max()
        worst_rate = self.df['Retention_Rate'].min()
        
        print(f"\n📈 QUARTERLY INSIGHTS:")
        print(f"   • Best performing quarter: {best_q} ({best_rate:.2f}%)")
        print(f"   • Worst performing quarter: {worst_q} ({worst_rate:.2f}%)")
        print(f"   • Range of performance: {best_rate - worst_rate:.2f} percentage points")
        
        # Trend analysis
        q_over_q = [self.df['Retention_Rate'].iloc[i] - self.df['Retention_Rate'].iloc[i-1] 
                   for i in range(1, len(self.df))]
        
        print(f"\n📉 TREND ANALYSIS:")
        print(f"   • Q1→Q2 change: {q_over_q[0]:+.2f}%")
        print(f"   • Q2→Q3 change: {q_over_q[1]:+.2f}%")
        print(f"   • Q3→Q4 change: {q_over_q[2]:+.2f}%")
        
        # Risk assessment
        print(f"\n⚠️  RISK ASSESSMENT:")
        if stats['cv'] > 2:
            print(f"   • HIGH volatility detected (CV: {stats['cv']:.1f}%)")
        else:
            print(f"   • Moderate volatility (CV: {stats['cv']:.1f}%)")
            
        if self.performance_gap > 10:
            print(f"   • CRITICAL performance gap: {self.performance_gap:.1f}pp below target")
        elif self.performance_gap > 5:
            print(f"   • Significant performance gap: {self.performance_gap:.1f}pp below target")
        
        # Recommendations
        print(f"\n🎯 STRATEGIC RECOMMENDATIONS:")
        print(f"   • Immediate target: Achieve 75% retention (+{75 - self.avg_retention:.1f}pp)")
        print(f"   • 6-month target: Achieve 80% retention (+{80 - self.avg_retention:.1f}pp)")
        print(f"   • 12-month target: Achieve 85% industry benchmark (+{self.performance_gap:.1f}pp)")
        print(f"   • Focus area: Address Q3 seasonal decline (-{q_over_q[1]:.1f}pp)")
        
        return {
            'avg_retention': self.avg_retention,
            'performance_gap': self.performance_gap,
            'volatility': stats['cv'],
            'best_quarter': best_q,
            'worst_quarter': worst_q,
            'recommendations': [
                'Implement targeted retention campaigns',
                'Address Q3 seasonal vulnerabilities',
                'Establish predictive analytics for early intervention',
                'Launch customer loyalty program enhancements'
            ]
        }
    
    def export_data_analysis(self, filename='retention_analysis_results.xlsx'):
        """Export analysis results to Excel file"""
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Raw data
            self.df.to_excel(writer, sheet_name='Raw_Data', index=False)
            
            # Summary statistics
            stats_df = pd.DataFrame({
                'Metric': ['Average Retention Rate', 'Industry Target', 'Performance Gap', 
                          'Standard Deviation', 'Min Rate', 'Max Rate', 'Coefficient of Variation'],
                'Value': [f"{self.avg_retention:.2f}%", f"{self.industry_target:.2f}%", 
                         f"{self.performance_gap:.2f}pp", f"{np.std(self.data['Retention_Rate']):.2f}%",
                         f"{np.min(self.data['Retention_Rate']):.2f}%", f"{np.max(self.data['Retention_Rate']):.2f}%",
                         f"{(np.std(self.data['Retention_Rate']) / self.avg_retention) * 100:.2f}%"]
            })
            stats_df.to_excel(writer, sheet_name='Summary_Statistics', index=False)
            
            # Gap analysis
            gap_df = pd.DataFrame({
                'Quarter': self.df['Quarter'],
                'Actual_Rate': self.df['Retention_Rate'],
                'Target_Rate': self.industry_target,
                'Gap': [self.industry_target - rate for rate in self.df['Retention_Rate']],
                'Achievement_Percentage': [(rate/self.industry_target)*100 for rate in self.df['Retention_Rate']]
            })
            gap_df.to_excel(writer, sheet_name='Gap_Analysis', index=False)
        
        print(f"Analysis results exported to: {filename}")

def main():
    """Main function to run the complete retention analysis"""
    print("Starting E-commerce Customer Retention Analysis...")
    print("Analyst: 23f3003731@ds.study.iitm.ac.in\n")
    
    # Initialize analyzer
    analyzer = RetentionAnalyzer()
    
    # Run statistical analysis
    stats = analyzer.calculate_statistics()
    
    # Generate visualizations
    print("\nGenerating visualizations...")
    analyzer.create_trend_visualization()
    analyzer.create_performance_dashboard()
    analyzer.create_interactive_plotly_chart()
    
    # Generate insights report
    insights = analyzer.generate_insights_report()
    
    # Export results
    analyzer.export_data_analysis()
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print("All visualizations and reports have been generated.")
    print("Check the 'visualizations/' folder for charts and graphs.")
    print("Review 'retention_analysis_results.xlsx' for detailed data export.")
    print("\nKey Finding: Average retention rate is 71.33% vs 85% target")
    print("Recommendation: Implement targeted retention campaigns immediately")

if __name__ == "__main__":
    # Create visualizations directory if it doesn't exist
    import os
    os.makedirs('visualizations', exist_ok=True)
    
    # Run the analysis
    main()
