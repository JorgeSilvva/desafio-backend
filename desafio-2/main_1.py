from typing import List


# Classe com cinco métodos e duas variáveis de instância.


class MyClass1:
    __var1: List[int]
    __var2: str

    # Método construtor que inicializa as variáveis de instância __var1 e __var2, passados como argumentos.

    def __init__(self, var1: List[int], var2: str):
        self.__var1 = var1
        self.__var2 = var2

    # Retorna o valor da variável de instância __var1.

    def get_var1(self):
        return self.__var1

    # Define o valor da variável de instância __var1.

    def set_var1(self, var1: List[int]):
        self.__var1 = var1

    # Retorna o valor da variável de instância __var2.
    def get_var2(self):
        return self.__var2

    # Define o valor da variável de instância __var2.

    def set_var2(self, var2: str):
        self.__var2 = var2

    # Retorna True se houver valores duplicados na lista __var1, caso contrário, retorna False.

    def method1(self) -> bool:
        aux = self.__var1.copy()
        aux.sort()
        for i in range(1, len(aux)):
            if aux[i] == aux[i-1]:
                return True
        return False

    # Recebe um inteiro target como entrada e retorna uma lista de dois inteiros.
    # Procura dois inteiros na lista __var1 que somam target e retorna seus índices.

    def method2(self, target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(self.__var1):
            remaining = target - self.__var1[i]

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i

    # Recebe um inteiro k como entrada e rotaciona a lista __var1 k vezes para a direita.

    def method3(self, k: int) -> List[int]:
        nums = self.__var1.copy()
        k = k % len(nums)
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            pos = (i + k) % len(nums)
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1
        return nums

    # Retorna o reverso da string __var2.

    def method4(self) -> str:
        return self.__var2[::-1]

    # Recebe duas listas de inteiros e retorna a mediana da lista combinada.

    @staticmethod
    def method5(x: List[int], y: List[int]) -> int:

        z = [*x, *y]
        z.sort()
        if len(z) % 2 == 0:
            result = (z[len(z)//2] + z[len(z)//2-1])/2

        else:
            result = z[len(z)//2]

        return result
