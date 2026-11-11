import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_yield_heatmap(csv_filepath, chip_width, chip_height):
    # Load the parsed DRC/LVS error log
    df = pd.read_csv(csv_filepath)
    
    # Set up the figure resembling a silicon die
    plt.figure(figsize=(8, 8))
    plt.xlim(0, chip_width)
    plt.ylim(0, chip_height)
    
    # Plot the individual defects
    sns.scatterplot(
        data=df, x='X_Coord', y='Y_Coord', 
        hue='Rule_Violated', palette='deep', s=60, edgecolor='black', zorder=2
    )
    
    # Overlay a spatial density heatmap to identify systemic layout clustering
    sns.kdeplot(
        x=df['X_Coord'], y=df['Y_Coord'], 
        cmap='Reds', fill=True, alpha=0.5, bw_adjust=0.8, zorder=1
    )
    
    plt.title('DRC Spatial Defect Distribution & Yield Heatmap')
    plt.xlabel('Die X-Coordinate (µm)')
    plt.ylabel('Die Y-Coordinate (µm)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(title='Violation Type')
    
    # Save the output visualization
    plt.savefig('drc_spatial_heatmap.png', dpi=300)
    print("EDA Yield Heatmap generated: drc_spatial_heatmap.png")

if __name__ == "__main__":
    # Simulating a 1000x1000 µm chip die
    generate_yield_heatmap('mock_drc_errors.csv', 1000, 1000)