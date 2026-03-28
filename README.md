# Quantum Computing: Foundations & IBM Quantum Integration ⚛️

[![Qiskit](https://img.shields.io/badge/Framework-Qiskit-6129ff)](https://qiskit.org/)
[![Python](https://img.shields.io/badge/Language-Python-3776ab)](https://www.python.org/)
[![IBM Quantum](https://img.shields.io/badge/Hardware-IBM%20Quantum-052f61)](https://quantum.ibm.com/)

Este repositório documenta uma jornada técnica em **Computação Quântica**, abrangendo desde simulações teóricas de estados fundamentais até a implementação de fluxos de trabalho em **processadores quânticos reais (QPUs)** da IBM.

## 🎯 Objetivos do Projeto
* Implementar estados de **Sobreposição** e **Emaranhamento**.
* Automatizar a autenticação e gestão de jobs no **IBM Quantum Platform**.
* Desenvolver lógica de extração de dados brutos (BitArrays) para lidar com resultados de hardware real.

## 📂 Estrutura do Repositório
```bash
quantum-computing-fundamentals/
│
├── experiments/
│   ├── entanglement.py
│   ├── superposition.py
│   ├── wave_function_collapse.py
│
├── principal_experiment/
│   ├── authentication.py
│   ├── real_wave_function_collapse.py
│   ├── teste.py
│
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
```

### 🔬 Fundamentos (Simuladores)
* **`superposition.py`**: Criação de estados equiprováveis via porta Hadamard ($H$).
* **`entanglement.py`**: Geração de **Estados de Bell** (emaranhamento máximo) utilizando portas $H$ e CNOT ($CX$).
* **`wave_function_collapse.py`**: Demonstração do impacto estatístico da medição no colapso da função de onda.

### 🤖 Integração com Hardware Real
* **`autentification.py`**: Script utilitário para configurar e persistir o token da API IBM localmente.
* **`teste.py`**: Validação rápida de conectividade e listagem de backends disponíveis.
* **`real_wave_function_collapse.py`**: Implementação avançada com transpilação adaptada ao ISA do hardware e tratamento manual de `SamplerPubResult` para contagem de bits.

## 🛠️ Configuração do Ambiente

1. **clone o repositorio**
    ```bash
    https://github.com/Vitor985-hub/Quantum-Computing-Foundations-IBM-Quantum-Integration.git
    ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. Configure suas credenciais IBM:
Abra o arquivo autentification.py, insira sua API Key e execute:
    ```bash
    python autentification.py
    ```
4. Valide a conexão:
    ```bash
    python teste.py
    ```

🚀 Execução em Hardware
Após validar a conexão, você pode submeter circuitos diretamente para as QPUs da IBM utilizando o script real_wave_function_collapse.py. O código está preparado para selecionar automaticamente o melhor backend operacional e gerenciar a fila de execução.

📊 Considerações Técnicas
Diferente dos simuladores (AerSimulator), os resultados em hardware real apresentam ruído quântico (decoerência e erros de gate). Este projeto inclui rotinas de pós-processamento para converter os dados complexos retornados pelo serviço em distribuições de probabilidade legíveis.
   
