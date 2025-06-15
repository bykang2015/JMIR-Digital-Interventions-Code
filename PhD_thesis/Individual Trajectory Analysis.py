"""
Individual Trajectory Analysis for Digital Mental Health Interventions
=====================================================================

This script analyzes individual participant trajectories for PHQ-9 and UCLA loneliness scores
across three intervention groups: Bondee, Woebot, and Happify.

Author: Research Team
Repository: https://github.com/bykang2015/JMIR-Digital-Interventions-Code
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set Korean font for matplotlib (optional - adjust based on your system)
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'Malgun Gothic']
plt.rcParams['axes.unicode_minus'] = False

class TrajectoryAnalyzer:
    """Class for analyzing individual participant trajectories"""
    
    def __init__(self):
        self.trajectory_data = {
            'bondee': [
                {'id': 'P1', 'phq9': [15, 6, 5, 5], 'ucla': [50, 44, 42, 48]},
                {'id': 'P2', 'phq9': [5, 5, 8, 5], 'ucla': [60, 62, 57, 56]},
                {'id': 'P3', 'phq9': [13, 13, 12, 9], 'ucla': [49, 44, 58, 50]}
            ],
            'woebot': [
                {'id': 'P4', 'phq9': [4, 2, 5, 6], 'ucla': [53, 36, 49, 43]},
                {'id': 'P5', 'phq9': [7, 3, 7, 11], 'ucla': [45, 43, 46, 53]},
                {'id': 'P6', 'phq9': [5, 3, 9, 3], 'ucla': [43, 47, 49, 48]},
                {'id': 'P7', 'phq9': [16, 11, 15, 12], 'ucla': [52, 48, 49, 45]},
                {'id': 'P8', 'phq9': [15, 11, 13, 12], 'ucla': [58, 57, 61, 62]},
                {'id': 'P9', 'phq9': [13, 7, 7, 5], 'ucla': [47, 43, 33, 49]},
                {'id': 'P10', 'phq9': [12, 17, 11, 6], 'ucla': [48, 38, 40, 45]},
                {'id': 'P11', 'phq9': [14, 6, 4, 4], 'ucla': [61, 67, 61, 52]},
                {'id': 'P12', 'phq9': [3, 1, 2, 1], 'ucla': [60, 54, 59, 43]},
                {'id': 'P13', 'phq9': [7, 7, 5, 15], 'ucla': [69, 59, 66, 59]},
                {'id': 'P14', 'phq9': [9, 8, 12, 11], 'ucla': [59, 60, 58, 61]},
                {'id': 'P15', 'phq9': [4, 5, 5, 4], 'ucla': [39, 37, 44, 34]},
                {'id': 'P16', 'phq9': [15, 17, 14, 12], 'ucla': [47, 56, 52, 50]},
                {'id': 'P17', 'phq9': [7, 6, 6, 4], 'ucla': [47, 49, 45, 50]},
                {'id': 'P18', 'phq9': [2, 1, 1, 0], 'ucla': [39, 32, 31, 33]}
            ],
            'happify': [
                {'id': 'P19', 'phq9': [4, 1, 2, 0], 'ucla': [48, 44, 50, 52]},
                {'id': 'P20', 'phq9': [5, 6, 1, 2], 'ucla': [42, 50, 39, 36]},
                {'id': 'P21', 'phq9': [10, 6, 4, 7], 'ucla': [63, 67, 62, 67]},
                {'id': 'P22', 'phq9': [12, 4, 9, 7], 'ucla': [59, 51, 51, 55]},
                {'id': 'P23', 'phq9': [9, 11, 7, 5], 'ucla': [55, 60, 47, 47]},
                {'id': 'P24', 'phq9': [14, 19, 13, 6], 'ucla': [62, 57, 57, 49]},
                {'id': 'P25', 'phq9': [7, 3, 3, 1], 'ucla': [39, 32, 24, 31]},
                {'id': 'P26', 'phq9': [3, 5, 3, 3], 'ucla': [45, 43, 44, 42]},
                {'id': 'P27', 'phq9': [11, 6, 3, 12], 'ucla': [50, 44, 45, 42]}
            ]
        }
        
        self.time_points = ['Baseline', '1-month', '2-month', 'Post-intervention']
        self.group_colors = {
            'bondee': '#4A90E2',
            'woebot': '#E67E22', 
            'happify': '#27AE60'
        }
        
    def identify_responders(self, measure='phq9'):
        """
        Identify responders based on clinical improvement criteria
        PHQ-9: ≥5 point reduction (Löwe et al., 2004)
        UCLA: ≥10 point reduction
        """
        responders = {}
        threshold = 5 if measure == 'phq9' else 10
        
        for group, participants in self.trajectory_data.items():
            responders[group] = []
            for participant in participants:
                baseline = participant[measure][0]
                post = participant[measure][3]
                improvement = baseline - post
                
                is_responder = improvement >= threshold
                responders[group].append({
                    'id': participant['id'],
                    'baseline': baseline,
                    'post': post,
                    'improvement': improvement,
                    'is_responder': is_responder
                })
        
        return responders
    
    def identify_patterns(self, measure='phq9'):
        """Identify specific trajectory patterns"""
        patterns = {
            'parabolic': [],  # Goes up then down
            'delayed_response': [],  # Improves later
            'early_response': [],  # Improves early then maintains
            'deterioration': []  # Gets worse
        }
        
        for group, participants in self.trajectory_data.items():
            for participant in participants:
                data = participant[measure]
                participant_info = f"{group.upper()} {participant['id']}: {' → '.join(map(str, data))}"
                
                # Parabolic: increases then decreases
                if data[1] > data[0] and data[3] < data[1]:
                    patterns['parabolic'].append(participant_info)
                
                # Delayed response: worse at 1-month, better at end
                if data[1] >= data[0] and data[3] < data[0]:
                    patterns['delayed_response'].append(participant_info)
                
                # Early response: improves by 1-month and maintains
                if data[1] < data[0] and abs(data[3] - data[1]) <= 2:
                    patterns['early_response'].append(participant_info)
                
                # Deterioration: worse at end than start
                if data[3] > data[0]:
                    patterns['deterioration'].append(participant_info)
        
        return patterns
    
    def plot_individual_trajectories(self, measure='phq9', save_path=None):
        """Create individual trajectory plot"""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Set title and labels
        measure_name = 'PHQ-9 Depression' if measure == 'phq9' else 'UCLA Loneliness'
        ax.set_title(f'Individual Trajectories: {measure_name} Scores', 
                    fontsize=18, fontweight='bold', pad=20)
        
        # Plot trajectories for each group
        for group, participants in self.trajectory_data.items():
            for participant in participants:
                data = participant[measure]
                
                # Determine if responder
                baseline, post = data[0], data[3]
                threshold = 5 if measure == 'phq9' else 10
                is_responder = (baseline - post) >= threshold
                
                # Set line style and markers based on group and responder status
                line_style = '-' if is_responder else '--'
                line_width = 3 if is_responder else 2
                alpha = 0.8 if is_responder else 0.6
                
                # Different markers for each group
                if group == 'bondee':
                    marker = 's'  # square
                    markersize = 8 if is_responder else 6
                elif group == 'woebot':
                    marker = 'o'  # circle
                    markersize = 7 if is_responder else 5
                else:  # happify
                    marker = '^'  # triangle
                    markersize = 9 if is_responder else 7
                
                # Plot line
                ax.plot(range(4), data, 
                       color=self.group_colors[group], 
                       linestyle=line_style,
                       linewidth=line_width,
                       marker=marker,
                       markersize=markersize,
                       alpha=alpha,
                       markeredgecolor='white',
                       markeredgewidth=1.5,
                       label=f'{participant["id"]} ({group.title()})')
        
        # Customize plot
        ax.set_xticks(range(4))
        ax.set_xticklabels(self.time_points, fontsize=12)
        ax.set_xlabel('Time Points', fontsize=14, fontweight='bold')
        
        ylabel = 'PHQ-9 Score' if measure == 'phq9' else 'UCLA Loneliness Score'
        ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
        
        # Set y-axis limits
        y_max = 20 if measure == 'phq9' else 70
        ax.set_ylim(0, y_max)
        
        # Remove grid
        ax.grid(False)
        
        # Add legend with group information only
        legend_elements = []
        for group in self.group_colors.keys():
            legend_elements.append(plt.Line2D([0], [0], color=self.group_colors[group], 
                                            linewidth=3, label=group.title()))
        
        # Add responder/non-responder legend
        legend_elements.extend([
            plt.Line2D([0], [0], color='gray', linewidth=3, linestyle='-', 
                      label='Responder (solid)'),
            plt.Line2D([0], [0], color='gray', linewidth=2, linestyle='--', 
                      label='Non-responder (dashed)')
        ])
        
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generate_summary_report(self):
        """Generate comprehensive summary report"""
        print("=" * 80)
        print("INDIVIDUAL TRAJECTORY ANALYSIS REPORT")
        print("=" * 80)
        
        for measure in ['phq9', 'ucla']:
            measure_name = 'PHQ-9 Depression' if measure == 'phq9' else 'UCLA Loneliness'
            print(f"\n{measure_name.upper()} ANALYSIS")
            print("-" * 50)
            
            # Responder analysis
            responders = self.identify_responders(measure)
            
            print("\n1. RESPONDER ANALYSIS:")
            threshold = 5 if measure == 'phq9' else 10
            print(f"   Improvement threshold: ≥{threshold} points")
            
            total_responders = 0
            total_participants = 0
            
            for group, data in responders.items():
                group_responders = sum(1 for p in data if p['is_responder'])
                group_total = len(data)
                total_responders += group_responders
                total_participants += group_total
                
                print(f"   {group.title()}: {group_responders}/{group_total} "
                      f"({group_responders/group_total*100:.1f}%)")
            
            print(f"   Overall: {total_responders}/{total_participants} "
                  f"({total_responders/total_participants*100:.1f}%)")
            
            # Pattern analysis
            patterns = self.identify_patterns(measure)
            
            print("\n2. TRAJECTORY PATTERNS:")
            for pattern_name, participants in patterns.items():
                if participants:
                    pattern_display = pattern_name.replace('_', ' ').title()
                    print(f"   {pattern_display} ({len(participants)} participants):")
                    for participant in participants:
                        print(f"     • {participant}")
            
            # Notable cases
            print("\n3. NOTABLE CASES:")
            
            # Find extreme values
            all_values = []
            extreme_cases = []
            
            for group, participants in self.trajectory_data.items():
                for participant in participants:
                    data = participant[measure]
                    all_values.extend(data)
                    
                    # Check for extreme starting values
                    if measure == 'phq9' and data[0] >= 14:
                        improvement = data[0] - data[3]
                        extreme_cases.append(f"High baseline: {group.upper()} {participant['id']}: "
                                           f"{' → '.join(map(str, data))} (Δ={improvement})")
                    
                    # Check for maximum values reached
                    max_val = max(data)
                    max_idx = data.index(max_val)
                    if max_val == max(all_values):
                        extreme_cases.append(f"Peak value: {group.upper()} {participant['id']}: "
                                           f"{' → '.join(map(str, data))} (peak={max_val} at {self.time_points[max_idx]})")
            
            for case in extreme_cases[:5]:  # Show top 5
                print(f"   • {case}")
            
            print(f"\n   Data range: {min(all_values)} - {max(all_values)}")
            print()

# Main execution
def main():
    """Main function to run the trajectory analysis"""
    
    print("Starting Individual Trajectory Analysis...")
    print("Repository: https://github.com/bykang2015/JMIR-Digital-Interventions-Code")
    print()
    
    # Initialize analyzer
    analyzer = TrajectoryAnalyzer()
    
    # Generate comprehensive report
    analyzer.generate_summary_report()
    
    # Create visualizations
    print("Generating visualizations...")
    
    # PHQ-9 trajectories
    print("\nPlotting PHQ-9 trajectories...")
    analyzer.plot_individual_trajectories(measure='phq9', 
                                         save_path='phq9_individual_trajectories.png')
    
    # UCLA trajectories  
    print("Plotting UCLA loneliness trajectories...")
    analyzer.plot_individual_trajectories(measure='ucla', 
                                         save_path='ucla_individual_trajectories.png')
    
    print("\nAnalysis completed!")
    print("Generated files:")
    print("  • phq9_individual_trajectories.png")
    print("  • ucla_individual_trajectories.png")

if __name__ == "__main__":
    main()
