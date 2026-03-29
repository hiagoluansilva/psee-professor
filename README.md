# psee-professor

Aplicativo mobile para o professor do sistema **PSEE** (Sistema de Pequena Escala de Ensino), desenvolvido em Python/Kivy.

## Descrição

App do lado professor do PSEE. Permite configurar os parâmetros da planta didática, definir tensões de referência e gerenciar os exercícios apresentados aos alunos.

## Funcionalidades

- Configuração do número de tensões de referência
- Validação de entrada com tratamento de erros
- Fluxo de confirmação antes de enviar configurações
- Interface com múltiplas telas

## Estrutura de telas

```
Menu → Tela1 (config) → Tela3 (confirmar) → Tela4 (botões)
                      → Tela2 (erro)
```

## Requisitos

```
Python 3.x
kivy
pyserial
```

```bash
pip install kivy pyserial
```

## Como executar

```bash
python psee-professor.py
```

## Projeto relacionado

- [psee-aluno](https://github.com/hiagoluansilva/psee-aluno) — App do aluno
- [esp32-serial-display-adc](https://github.com/hiagoluansilva/esp32-serial-display-adc) — Firmware ESP32

## Escola

Centro Tecnológico Liberato — Novo Hamburgo/RS
TCC — Trabalho de Conclusão de Curso
