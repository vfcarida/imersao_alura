import pandas as pd
from unittest.mock import patch
from src.components.sidebar import render_sidebar

@patch('src.components.sidebar.st.sidebar')
def test_render_sidebar_empty(mock_sidebar):
    """Testa comportamento da sidebar com DataFrame vazio."""
    df_empty = pd.DataFrame()
    anos, sen, cont, tam = render_sidebar(df_empty)
    assert anos == []
    assert sen == []
    assert cont == []
    assert tam == []
    mock_sidebar.warning.assert_called_once()
