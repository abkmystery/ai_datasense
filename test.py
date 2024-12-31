from ai_datasense.core import DataAnalyzer

# Replace these with your actual details
analyzer = DataAnalyzer(
 api_provider="your_api_provider_here",
    api_key="your_api_key_here",
    api_url="your_api_url_here",
    model="your_model_here"
)
file_paths = ["test_data.csv"]     # CSV file
 #   "data.xlsx",         # Excel file
 #  "report.pdf",        # PDF file
 #   "notes.txt",         # Text file
 #   "image.png"          # Image file


results = analyzer.analyze(file_paths)

# Iterate through results
for file, result in results.items():
    print(f"\n📂 **Results for {file}:**")
    
    try:
        # Extract content from AI response
        content = result['choices'][0]['message']['content']
        
        # Parse Key Insights
        if "### Key Insights" in content:
            insights = content.split("### Key Insights")[1].split("###")[0].strip()
            print("\n🧠 **Key Insights:**")
            print(insights)
        else:
            print("\n🧠 **Key Insights:** No insights provided.")
        
        # Parse Anomalies
        if "### Anomalies" in content:
            anomalies = content.split("### Anomalies")[1].split("###")[0].strip()
            print("\n🚨 **Anomalies:**")
            print(anomalies)
        else:
            print("\n🚨 **Anomalies:** No anomalies detected.")
        
        # Parse Visualization Recommendations
        if "### Visualization Recommendations" in content:
            visualizations = content.split("### Visualization Recommendations")[1].strip()
            print("\n📊 **Visualization Recommendations:**")
            print(visualizations)
        else:
            print("\n📊 **Visualization Recommendations:** No visualization suggestions provided.")
    
    except (KeyError, IndexError, AttributeError) as e:
        print(f"\n❌ Error extracting data from {file}: {e}")