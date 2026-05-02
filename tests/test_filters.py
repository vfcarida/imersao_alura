import pandas as pd
from src.filters import apply_filters

def test_apply_filters_empty_df():
    """Testa se a função retorna df vazio quando recebe df vazio."""
    df_empty = pd.DataFrame()
    result = apply_filters(df_empty, [2023], ["Junior"], ["CLT"], ["Pequena"])
    assert result.empty

def test_apply_filters_with_data():
    """Testa se a filtragem funciona corretamente."""
    data = {
        'ano': [2022, 2023, 2023],
        'senioridade': ['Junior', 'Pleno', 'Junior'],
        'contrato': ['CLT', 'PJ', 'CLT'],
        'tamanho_empresa': ['Pequena', 'Media', 'Grande'],
        'usd': [30000, 60000, 35000]
    }
    df = pd.DataFrame(data)
    
    # Filtrando por 2023 e Junior
    res = apply_filters(df, anos=[2023], senioridades=['Junior'], contratos=['CLT'], tamanhos=['Grande'])
    
    assert len(res) == 1
    assert res.iloc[0]['usd'] == 35000
    assert res.iloc[0]['tamanho_empresa'] == 'Grande'

def test_apply_filters_no_match():
    """Testa o caso em que nenhum dado corresponde ao filtro."""
    data = {
        'ano': [2022, 2023],
        'senioridade': ['Junior', 'Pleno'],
        'contrato': ['CLT', 'PJ'],
        'tamanho_empresa': ['Pequena', 'Media'],
        'usd': [30000, 60000]
    }
    df = pd.DataFrame(data)
    
    # Procurando Senior, que não existe
    res = apply_filters(df, anos=[2023], senioridades=['Senior'], contratos=['CLT'], tamanhos=['Pequena'])
    
    assert res.empty
