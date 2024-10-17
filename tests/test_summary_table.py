from titanic_analysis.summary_table import create_summary_table

def test_create_summary_table():
    # Mock a DataFrame
    mock_df = {
        'Age': [22, 38, 26, 35, None],
        'Sex': ['male', 'female', 'female', 'male', 'male'],
        'Survived': [0, 1, 1, 0, 1]
    }
    
    summary_df = create_summary_table(mock_df)
    
    assert 'Feature Name' in summary_df.columns, "Summary should include 'Feature Name'"
    assert 'Data Type' in summary_df.columns, "Summary should include 'Data Type'"
    assert 'Has Missing Values?' in summary_df.columns, "Summary should include 'Has Missing Values?'"
