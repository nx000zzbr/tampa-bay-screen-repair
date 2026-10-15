# Tampa Bay Screen Repair · proposta de site

Site de quatro páginas para a Tampa Bay Screen Repair (Jerry Toloff, Plant City, FL), feito para a apresentação ao cliente.
Abra `index.html` em qualquer navegador ou sirva a pasta com um servidor estático (`python3 -m http.server`).
O estudo que fundamenta o site está em `../estudo-tampa-bay-screen-repair.html`.

## A ideia

**O site é o orçamento por escrito do Jerry.** A avaliação mais citada diz "what I was quoted is actually what I was billed". Então toda a página é papelaria: um cartão impresso ao lado da piscina, um talão que o visitante preenche, pastas com os trabalhos, papeizinhos rasgados com o que as pessoas disseram, uma folha de guia de telas, uma carta assinada, um cartão de visita sobre o mapa do condado de 1882, e o verso do cartão como rodapé.

- **Paleta:** papel osso (`#f0f0eb`), tinta (`#1b1b1a`), laranja de colete (`#ff6a1a`) só em botões e campos, sobre uma "mesa" carvão (`#1f1e1b`).
- **Tipos:** Barlow Condensed (tudo que é impresso grande) e Public Sans (tudo que se lê). Cinco tamanhos.
- **A faixa listrada** no topo do cartão vem dos toldos listrados do centro de Plant City (foto no rodapé). Volta no rodapé e sob os botões no hover.
- **Nada de contorno:** todas as formas são preenchimentos e `clip-path` (zigue-zague, escalopes, picote, aba de pasta).

## A coisa viva: "Count your panels"

O talão na home. O visitante conta painéis de parede, de teto e portas, escolhe a tela, e o canhoto mostra um valor típico. "Send to Jerry" abre um formulário curto (nome, telefone, cidade, observações) que gera um e-mail com as linhas preenchidas; "Text it instead" abre o SMS já escrito. Sem script, continua sendo uma lista de preços legível com os links de ligar e mandar texto.

**Os valores são amostra** (parede a partir de $45, teto $75, porta $95, no-see-um +$6, pet +$15, retelagem completa a partir de $1.200). Estão marcados na página como "typical" e precisam do aval do Jerry antes de ir ao ar.

## Páginas

- `index.html`: home completa, 12 seções, escrita à mão.
- `services.html`, `areas.html`, `screen-guide.html`: geradas por `python3 build.py` a partir de um só cabeçalho e rodapé. Edite `build.py` e rode de novo.
- `styles.css`, `main.js`: um CSS, um JS, sem frameworks, sem build obrigatório.
- `assets/`: fotos licenciadas e `credits.json` com fonte e licença de cada uma.

## O que o cliente precisa confirmar ou fornecer

1. **Domínio.** `tampabayscreenrepair.com` está registrado na GoDaddy desde 2012, sem site. Se for dele, é o domínio. Se não, `.net`, `tampabayscreenrepairfl.com`, `screenrepairtampabay.com` e `tbscreenrepair.com` estavam livres em 15/10/2026.
2. **Fotos dos trabalhos.** Toda foto do site é de arquivo (pool cages da Flórida, Plant City, o mapa) e está legendada como tal. As do Jerry entram no hero, nas pastas de "Recent jobs" e nas folhas de serviço.
3. **Preços "a partir de"** do talão e do guia (veja acima).
4. **"Since 2012"** no hero: inferido do domínio e das avaliações mais antigas. Confirmar o ano.
5. **Horário:** "Monday to Saturday, 8 am to 7 pm" é amostra; o Google só diz "fecha às 19h".
6. **Garantia:** nenhuma é prometida no site. Se ele pratica alguma, cabe uma linha no talão e no rodapé.
7. **Cidades atendidas** e a regra de "no trip charge in East Hillsborough"; as descrições por cidade em `areas.html` são amostra.
8. **E-mail:** o site usa `TampaBayScreenRepair@gmail.com` (o das respostas no Google). O Facebook usa outro.
9. **Dennis e Brian** aparecem na carta e nas pastas por serem citados nas avaliações. Confirmar.
10. **Formulário:** hoje gera e-mail (`mailto:`) e SMS; não há backend. Para receber fotos pelo site, ligar o `<form>` a Formspree, Web3Forms ou similar (grátis nesse volume).
11. **Avaliações citadas** são reais e públicas no Google (Jennifer K., James P., Erik Q., Allen W., Ralph O., Dawn S.), abreviadas pelo sobrenome. Pedir ok do Jerry.
12. **FAQ:** "nothing up front", "we don't build new cages", "no trip charge" são suposições razoáveis a confirmar.

## Como foi verificado

- As quatro páginas foram testadas em 1440, 768 e 390 px: títulos em no máximo duas linhas, contraste de texto, nada rolando de lado, nada cobrindo título.
- Sem vídeo de propósito: não existe clipe honesto do assunto com licença livre. Um clipe curto do Jerry esticando uma tela substituiria o crossfade do hero.
- Próximo passo de maior impacto: fotos dos trabalhos do próprio Jerry no lugar das de arquivo.

## Imagens usadas e créditos

Nenhuma é apresentada como sendo da empresa. Os créditos estão no rodapé da home e em `assets/credits.json`.

| Arquivo | Título | Autor / fonte | Licença |
| --- | --- | --- | --- |
| sarasota-swimming-pool-2010.jpg | Sarasota – Swimming Pool (2010) | roger4336, Flickr | CC BY-SA 2.0 |
| sarasota-swimming-pool-in-new-home-1994.jpg | Sarasota – Swimming Pool in New Home (1994) | roger4336, Flickr | CC BY-SA 2.0 |
| sarasota-house-from-back-yard-2010.jpg | Sarasota – House from Back Yard (2010) | roger4336, Flickr | CC BY-SA 2.0 |
| seminole-saturday-spring-swim.jpg | Seminole Saturday Spring Swim | Michel Curi, Flickr | CC BY 2.0 |
| pool-screen-repair.jpg | Pool-screen-repair | SergioMiami, Wikimedia Commons | CC BY-SA 4.0 |
| pool-screen-repair-estimate.jpg | Pool-screen-repair-estimate | SergioMiami, Wikimedia Commons | CC BY-SA 4.0 |
| window-screen-2878481856.jpg | Window Screen | daryl_mitchell, Wikimedia Commons | CC BY-SA 2.0 |
| plant-city-fl-downtown-comm-dist05.jpg · -dist02.jpg | Plant City FL Downtown Commercial District | Ebyabe, Wikimedia Commons | CC BY-SA 3.0 |
| 19970917-09-csx-plant-city-florida-6064973647.jpg | CSX, Plant City, Florida, 1997 | David Wilson, Wikimedia Commons | CC BY 2.0 |
| florida-strawberry-festival-from-fl-574-2.jpg | Florida Strawberry Festival from FL 574 | DanTD, Wikimedia Commons | CC BY-SA 4.0 |
| quarters-no-9-unit-3-interior-screened.jpg | Screened porch, U.S. Naval Air Station Pensacola (HABS) | Library of Congress | Domínio público |
| map-of-hillsborough-county-florida-loc-2012592403.jpg | Map of Hillsborough County, Florida, 1882 | Florida Land and Improvement Co., Library of Congress | Domínio público |

Não usadas (baixadas durante a pesquisa, podem ser apagadas): `sarasota-new-home-from-back-yard-1994.jpg`, `detail-of-screen-porch-on-west-side.jpg`, `porch-screen-enclosure-piney-point-light-station.jpg`.

As fotos CC BY-SA só foram recortadas e redimensionadas, não alteradas; se forem combinadas ou recoloridas, a versão alterada precisa manter a mesma licença.
