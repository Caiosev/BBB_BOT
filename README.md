# BBB_BOT
Script feito para a automação de votações nos paredões do BBB 21, sem a menor intenção de prejudicar ou interferir de maneira inumana o programa.

## Requisitos
Instalar Python na versão 3.9 ou superior (https://www.python.org/downloads/).
Após a instalação do Python,
abrir o cmd e utilizar os seguintes comandos:
`pip install pillow`, (para a instalação do pillow);
`pip install pyautogui`,(para a instalação do pyautogui).

### Opcional: 
Instalar Lightshot para captura de tela (https://app.prntscr.com/pt-br/)

# Como funciona?
O script compara imagens que estão sendo visualizadas na sua tela com as imagens salvas na sua pasta, quando identificado uma imagem igual ele faz a ação de clicar. Há também um delay entre as ações para que o site não negue as requisições ou comece a mostrar testes captcha.

## Recomendações
Recomenda-se que após efetuar o login no site, diminua o zoom de seu navegador para 75% (na página onde há a opção dos candidatos).
Antes de executar o script, é altamente recomendado tirar print do nome do participante que você deseja votar, e da caixa do captcha. E substituir essas imagens na pasta BBB_BOT (nome = print do nome do participante / check = print do captcha).
De preferência, não deixe a janela de seu navegador maximizada, deixe-a lado a lado com o prompt.

# Como utilizar?
Abra o site da votação e deixe-o na página onde aparece as pessoas que estão concorrendo no paredão. Abra o script.py e logo depois, rapidamente, clique uma alguma parte em branco do site e espere a mágica acontecer.

## Possíveis Erros
Nome NÃO encontrado: o script não conseguiu encontrar nenhuma imagem em sua tela que seja parecida com o nome.
Resolução: Tire outro print do nome do participante e deixe a janela do navegador em evidência.

"Captcha NÃO Encontrado": o script não conseguiu comparar as imagens do captcha (check.png) com o captcha em seu navegador, É normal acontecer algumas vezes, ele irá tentar reconhecer a imagem novamente automaticamente. Se o erro persistir, tire outro print do captcha e substitua o check.png com ele.

# Atenção
O script não irá burlar o teste do captcha. Se ele aparecer, feche a janela e tente novamente depois de algumas horas. O delay alto entre as ações é afim de evitar isso (o delay pode ser mudado no código-fonte, não recomendo).
