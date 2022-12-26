# Street Fighter 6 Pipeline with Python and Azure

Olá, pessoal. Espero que todos estejam bem!<img src="https://media.giphy.com/media/zd9l9VRm5tCVO/giphy.gif" width="20">

Eis que aqui vos trago um projeto que irá impactar (acredito eu) muito com o sentimento de nostalgia de alguns de vocês!
Vocês já ouviram falar de um jogo nada conhecido 🙃 do gênero de luta chamado **Street Fighter**? Então, recentemente a nossa querida [Capcom](https://www.capcom.com/) anunciou a data de lançamento do [Street Fighter VI](https://www.streetfighter.com/6/pt-br/) para Junho de 2023.   
Enquanto aguardamos ansiosamente o lançamento, aos poucos, no site oficial, são revelados os personagens. A expectativa para a primeira temporada seja de 22 lutadores.   
Uma coisa super legal que percebi, foi que ao revelar o personagem, também é informado uma descrição e algumas curiosidades nas quais eu não sabia. 

![Ryu's info](./images/site_info.png)

Confesso que adorei isso. Afinal, quem poderia imaginar que logo o Ryu odeia aranhas?

E com isso eu tive uma ideia: Por que não criar um workflow de dados para coletar, armazenar e transformar utlizando Python e a plataforma Azure? Pois vamos ser sinceros, é meio chato ficar acessando cada personagem para verificar essas informações.

Abaixo está um diagrama da proposta:

![Workflow](./images/workflow.png)