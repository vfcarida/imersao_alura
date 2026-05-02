import pandas as pd
from unittest.mock import patch
from src.data_loader import load_data

@patch('src.data_loader.pd.read_csv')
def test_load_data_success(mock_read_csv):
    """Testa o sucesso no carregamento dos dados."""
    mock_df = pd.DataFrame({'ano': [2023], 'usd': [50000]})
    mock_read_csv.return_value = mock_df
    
    # Simulando o clear_cache para não usar cache em teste
    load_data.clear()
    
    df = load_data()
    assert not df.empty
    assert len(df) == 1
    assert df.iloc[0]['usd'] == 50000
    mock_read_csv.assert_called_once()

@patch('src.data_loader.pd.read_csv')
def test_load_data_failure(mock_read_csv):
    """Testa o fallback para DataFrame vazio em caso de erro na rede ou CSV."""
    mock_read_csv.side_effect = Exception("Network error")
    
    load_data.clear()
    
    df = load_data()
    assert df.empty
