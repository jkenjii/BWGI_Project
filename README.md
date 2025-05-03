# Projeto BWGI 

Estrutura:
- core/: lógica de negócio
- data_utils/: utilitários de dados
- strategies/: tarefas implementadas com Strategy
- facade.py: gerencia estratégias
- main.py: ponto de entrada


Para rodar:
cd src
python -m bwgi_project.main

Os testes estão localizados na pasta `tests/` e podem ser executados com:

```bash
python -m unittest discover -s tests
```
