# analysis.py
# Author: Generated using GitHub Copilot
# Email: 23f3003731@ds.study.iitm.ac.in
# Purpose: Analyze quarterly customer retention data and compare with industry benchmark

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention": [71.68, 72.07, 69.67, 71.91]
})

# Calculate average retention
average_retention = data["Retention"].mean()
print(f"Average Retention Rate: {average_retention:.2f}")  # Should print 71.33

# Set industry benchmark
industry_target = 85

# Plot retention trend
plt.figure(figsize=(8,5))
plt.plot(data["Quarter"], data["Retention"], marker='o', label="Company Retention")
plt.axhline(y=industry_target, color='r', linestyle='--', label="Industry Target (85)")
plt.title("Quarterly Customer Retention Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.ylim(65, 90)
plt.grid(True)
plt.legend()
plt.savefig("retention_trend.png")
plt.show()

# Generate insights
insights = f"""
Key Insights:
1. The average customer retention rate is {average_retention:.2f}, below the industry target of {industry_target}.
2. Q3 shows the lowest retention at 69.67%, indicating a potential seasonal or operational issue.
3. Q1, Q2, and Q4 hover around 71-72%, which is consistent but still below target.

Business Implications:
- The company is losing customers at a higher rate than industry benchmark.
- Lower retention can impact revenue, customer lifetime value, and brand loyalty.

Recommendations:
1. Implement targeted retention campaigns focused on Q3 to mitigate churn.
2. Analyse customer feedback for potential pain points.
3. Introduce loyalty programs or incentives to improve engagement.
4. Monitor retention monthly to evaluate effectiveness of interventions.
"""

print(insights)
