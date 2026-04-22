# Lidiane Turismo - Diretrizes do Projeto (Agent Instructions)

## Objetivo do Projeto
Este projeto tem como objetivo gerenciar e automatizar a criação de ativos de marketing (Landing Pages, Flyers, Vídeos) para a agência de viagens **Lidiane Turismo**. O projeto busca manter um padrão visual de luxo, focado em sofisticação e no clima tropical (quando aplicável ao destino).

## Estrutura de Pastas e Padrão de Organização
A organização do projeto é vital para a escala. O agente deve **SEMPRE** seguir a seguinte arquitetura:

- **`brand/`**: Pasta raiz que contém todos os ativos globais e imutáveis da marca.
  - `logo.png`: Logotipo oficial da Lidiane Turismo. Nenhum projeto individual deve duplicar a logo; todos devem apontar para `../brand/logo.png` (ou o caminho relativo correspondente).
  - Outros assets globais (como fontes baixadas, ícones de marca registrada).

- **`[Nome do Destino]/`**: SEMPRE que o usuário pedir para criar material para um novo destino, o agente **deve criar uma nova pasta na raiz** com o nome do destino (ex: `Costa do Sauipe`, `Gramado`, `Maldivas`).
  - Todo o material da campanha desse destino deve ficar dentro desta pasta.
  - **Landing Page**: Deve se chamar `index.html` com seu arquivo `style.css`.
  - **Flyers**: Devem seguir a nomenclatura `flyer_v[numero].html` (ex: `flyer_v1.html`). Estes são gerados em HTML/CSS na proporção 9:16 (1080x1920) para garantir a legibilidade perfeita das fontes para o Instagram Stories/Reels.
  - **Imagens de Fundo**: Nomenclatura como `bg_landing.png` ou `bg_flyer_v1.png`.

## Identidade Visual
- **Tipografia**: Utilizar `Outfit` para títulos (elegância e modernidade) e `Inter` para textos corridos (legibilidade).
- **Cores Padrão**: 
  - Teal Tropical (Verde-Azulado): `#008080` e `#006666` (remete a confiança e natureza).
  - Laranja Sunset: `#FF7F50` e `#E66A3D` (energia e ação).
  - Areia/Bege: `#F5F1E6` (sofisticação, descanso para os olhos).
- **Estilo Geral**: Uso predominante de *Glassmorphism* (cartões translúcidos), cantos arredondados (`border-radius: 40px` ou `30px` dependendo do contexto), sobras suaves (`box-shadow`), muito espaço em branco (negative space) para um visual *clean* e *premium*.

## Regras de Comportamento do Agente
1. Ao receber um pedido para um novo destino, crie a pasta antes de gerar os arquivos.
2. Certifique-se de que caminhos de imagens em novos arquivos HTML apontem corretamente para os assets na pasta do destino e a logo na pasta `brand/`.
3. Ao gerar Flyers baseados em HTML, mantenha o CSS *inline* ou no `<style>` do próprio arquivo para facilitar a portabilidade, a menos que especificado de outra forma. A resolução base do container do flyer deve ser `1080x1920` com `transform: scale()` para visualização no navegador.
4. Geração de imagens via IA deve focar em cenários sem textos inseridos pelo modelo, utilizando a técnica de sobreposição (overlay) de texto em HTML/CSS para evitar erros tipográficos.
5. **Diretriz de Mídia Obrigatória**: Todas as peças publicitárias (Flyers, LPs, Vídeos) DEVEM conter e priorizar fotos e vídeos reais, atualizados e em alta definição (Alta Qualidade) dos destinos. Evite abstrações e imagens que não reflitam com precisão as instalações e paisagens atuais dos locais.
6. **Distribuição Espacial e Visibilidade**: Evite espaços ociosos excessivos entre elementos cruciais (ex: muito espaço acima do preço ou entre blocos de texto). A logotipo deve estar SEMPRE 100% legível e em destaque. É estritamente proibido o uso de logotipos ofuscados, invisíveis ou como "marcas d'água" que prejudiquem a visibilidade e o reconhecimento rápido da marca Lidiane Turismo.
