# PSEE Professor — Interface de Configuração do Sistema PSEE

🇧🇷 **Português** | 🇺🇸 [English](#english)

---

## Português

Interface Python/Kivy para professores no sistema PSEE, com configuração de tensão e navegação multi-tela para supervisão dos experimentos.

### O que faz
- Permite ao professor **configurar parâmetros de tensão** dos experimentos
- Interface **multi-tela** (Kivy ScreenManager)
- Supervisiona o estado dos exercícios dos alunos
- Envia configurações via serial para o ESP32

### Diferença em relação à versão aluno
| Versão | Foco |
|---|---|
| Aluno | Execução dos 5 exercícios |
| Professor | Configuração e supervisão |

### Requisitos
```
pip install kivy pyserial
```

### Plataforma
Python 3.x + Kivy + pyserial

---

## English

Python/Kivy interface for teachers on the PSEE platform, with voltage configuration and multi-screen navigation for experiment supervision.

### What it does
- Allows teacher to **configure voltage parameters** for experiments
- **Multi-screen** interface (Kivy ScreenManager)
- Supervises student exercise states
- Sends configurations via serial to ESP32

### Difference from student version
| Version | Focus |
|---|---|
| Student | Executing the 5 exercises |
| Teacher | Configuration and supervision |

### Requirements
```
pip install kivy pyserial
```

### Platform
Python 3.x + Kivy + pyserial
