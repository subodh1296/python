import pandas as pd
import matplotlib.pyplot as plt

# Sample time series data
data = pd.DataFrame({
    'value': [10, 15, 14, 16, 18, 20, 22, 23, 25, 27]
})

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(6, 4))

# Create a lag plot with a lag of 1
pd.plotting.lag_plot(data['value'], lag=1, ax=ax)

# Set title and labels
ax.set_title('Lag Plot with lag=1')
ax.set_xlabel('Current Value')
ax.set_ylabel('Lagged Value')

# Show the plot
plt.show()
