"""
Coaching Staff Data Management Tool
Helps organize and manage college football coaching staff information
"""

import pandas as pd
from pathlib import Path

class CoachingDataManager:
    def __init__(self, csv_path='coaching_staff_template.csv'):
        self.csv_path = csv_path
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load the coaching staff data from CSV"""
        try:
            self.df = pd.read_csv(self.csv_path)
            print(f"✓ Loaded {len(self.df)} records from {self.csv_path}")
        except FileNotFoundError:
            print(f"File not found. Creating new template at {self.csv_path}")
            self.create_template()
    
    def create_template(self):
        """Create a new empty template"""
        self.df = pd.DataFrame(columns=[
            'College', 'Coach_Name', 'Position', 'Phone_Number', 
            'Email', 'Twitter', 'Instagram', 'Additional_Notes'
        ])
        self.save_data()
    
    def add_coach(self, college, name, position='', phone='', email='', 
                  twitter='', instagram='', notes=''):
        """Add a new coach to the database"""
        new_row = {
            'College': college,
            'Coach_Name': name,
            'Position': position,
            'Phone_Number': phone,
            'Email': email,
            'Twitter': twitter,
            'Instagram': instagram,
            'Additional_Notes': notes
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        print(f"✓ Added {name} - {position} at {college}")
    
    def search_by_college(self, college_name):
        """Search for all coaches at a specific college"""
        results = self.df[self.df['College'].str.contains(college_name, case=False, na=False)]
        return results
    
    def search_by_position(self, position):
        """Search for coaches by position"""
        results = self.df[self.df['Position'].str.contains(position, case=False, na=False)]
        return results
    
    def save_data(self):
        """Save the data back to CSV"""
        self.df.to_csv(self.csv_path, index=False)
        print(f"✓ Saved data to {self.csv_path}")
    
    def export_to_excel(self, output_path='coaching_staff_data.xlsx'):
        """Export data to Excel with formatting"""
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            self.df.to_excel(writer, sheet_name='Coaching Staff', index=False)
            
            # Get the worksheet
            worksheet = writer.sheets['Coaching Staff']
            
            # Adjust column widths
            column_widths = {
                'A': 20,  # College
                'B': 25,  # Coach_Name
                'C': 25,  # Position
                'D': 15,  # Phone_Number
                'E': 30,  # Email
                'F': 20,  # Twitter
                'G': 20,  # Instagram
                'H': 30   # Additional_Notes
            }
            
            for col, width in column_widths.items():
                worksheet.column_dimensions[col].width = width
        
        print(f"✓ Exported to Excel: {output_path}")
    
    def get_stats(self):
        """Get statistics about the data"""
        stats = {
            'Total Coaches': len(self.df),
            'Total Colleges': self.df['College'].nunique(),
            'Coaches with Email': self.df['Email'].notna().sum(),
            'Coaches with Twitter': self.df['Twitter'].notna().sum(),
            'Coaches with Instagram': self.df['Instagram'].notna().sum(),
        }
        return stats
    
    def display_stats(self):
        """Display statistics"""
        stats = self.get_stats()
        print("\n=== Coaching Staff Database Stats ===")
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("=" * 35)


def main():
    """Main function with example usage"""
    manager = CoachingDataManager('coaching_staff_template.csv')
    
    # Example: Add a coach (you would do this manually for each coach)
    # manager.add_coach(
    #     college='Alabama',
    #     name='Nick Saban',
    #     position='Head Coach',
    #     phone='555-123-4567',
    #     email='example@example.com',
    #     twitter='@AlabamaFTBL',
    #     instagram='@alabamafootball',
    #     notes='Hall of Fame Coach'
    # )
    
    # Display stats
    manager.display_stats()
    
    # Save changes
    # manager.save_data()
    
    # Export to Excel
    # manager.export_to_excel('coaching_staff_data.xlsx')
    
    print("\nTo use this tool:")
    print("1. Edit coaching_staff_template.csv directly in Excel")
    print("2. Or use the add_coach() method in Python")
    print("3. Run export_to_excel() to create formatted Excel file")


if __name__ == '__main__':
    main()

