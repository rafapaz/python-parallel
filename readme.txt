
Existem 4 formas básicas de se fazer paralelismo com python. As outras formas são mais complexas e envolvem profundo conhecimento de bibliotecas de terceiros.

1 - Subprocessos
Quando se quer fazer chamadas a processos externos de forma paralela, aguardando o retorno dos processos filhos assincronamente.


2 - Threads
Threads em python não são de fato paralelas, mas simulam um paralelismo. A GIL (Global Interpreter Lock) impede que o python use mais de uma CPU em paralelo. Na verdade, se o código a ser paralelizado conter chamadas de sistema de I/O, o python libera a GIL e estas chamadas serão de fato paralelizadas. Ou seja, só faz sentido usar Threads caso queira paralelizar alguma tarefa de I/O (acesso a disco, redes, etc). A desvantagem é que cada Thread consome um overhead de 8 Mb de memória, o que pode onerar muito quando se precisa disparar milhares de threads. Obs: Deve-se tomar cuidado com race conditions.


3 - Corotinas com async/await
Corrotinas são a forma "pytônica" de se simular threads, mas sem o overhead das Threads. Também só faz sentido usar para tarefas que exigem I/O.


4 - concurrent.futures
Permite um paralelismo real de CPU e I/O, não somente de I/O. O custo porém é um overhead de CPU. Deve ser utilizado para tarefas isoladas e de alta alavancagem. Por isoladas, entendemos funções que não precisam compartilhar seus estados com outras partes do programa. Por alta alavancagem, entendemos situações nais quais apenas uma pequena porção dos dados precisa ser transferida entre os processos pai e filho, mas mesmo assim a computação efetuada é bastante intensa.

Fonte: "Python Eficaz" - Brett Slatkin