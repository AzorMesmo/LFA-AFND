# Símbolos De Controle

**Símbolos de Controle** são símbolos que não podem ser utilizados como *tokens* pois são utilizados pela lógica do algoritmo do **Autômato Finito**.

## Estados

No arquivo de *input.txt* os **estados** são representados pelos símbolos **<** e **>** sendo **<** o símbolo que representa o ínicio do nome do estado e **>** o que representao final.

> <S> 

## Separadores

No arquivo de *input.txt* os **separadores** são representados pelo símbolo **|** .

> *token*<A>|*token*<B>|*token*<C>

## Transições

No arquivo de *input.txt* as **transições** são representadas pelo símbolo **:** .

> <S>:*token*<A>|*token*<B>|*token*<C>

## Símbolo Terminal

No arquivo de *input.txt* o símbolo **`** é utilizado como **símbolo terminal**.

> <S>:*token*<A>|*token*<B>|`

## Quebras De Linhas

No arquivo de *input.txt* a **quebra de linha** (**\n**) é utilizada como símbolo terminal de palavras e gramáticas.

> se
> entao
> senao

> <S>:a<A>|e<A>|i<A>|o<A>|u<A>
> 
> <A>:a<A>|e<A>|i<A>|o<A>|u<A>|`

## Múltiplos Conjuntos De Palavras E Gramáticas

No arquivo de *input.txt* após todo conjunto de palavras ou gramáticas deve-se deixar uma linha **vazia** (**\n**) para que o programa possa reconhecer a mudança de contexto.

> se
> 
> entao
> 
> senao
> 
> <S>:a<A>|e<A>|i<A>|o<A>|u<A>
> 
> <A>:a<A>|e<A>|i<A>|o<A>|u<A>|&

> se\n
> 
> entao\n
> 
> senao\n
> 
> \n
> 
> <S>:a<A>|e<A>|i<A>|o<A>|u<A>\n
> 
> <A>:a<A>|e<A>|i<A>|o<A>|u<A>|&\n

> se\nentao\nsenao\n\n<S>:a<A>|e<A>|i<A>|o<A>|u<A>\n<A>:a<A>|e<A>|i<A>|o<A>|u<A>|&\n
