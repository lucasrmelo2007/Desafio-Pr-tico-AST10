from credito import aprovar_emprestimo

def test_aprovacao_por_score():
# Passa com score alto
    assert aprovar_emprestimo(850, 2000.00) is True
def test_aprovacao_por_renda():
# Passa com renda alta
    assert aprovar_emprestimo(500, 8000.00) is True
def test_reprovacao():
# Reprova com tudo baixo
    assert aprovar_emprestimo(300, 1500.00) is False
def test_limite_score():
    
    assert aprovar_emprestimo(700, 2000.00) is True
def test_limite_renda():

    assert aprovar_emprestimo(699, 5000.00) is False
def test_renda():
    assert aprovar_emprestimo(699, 5000.50) is True