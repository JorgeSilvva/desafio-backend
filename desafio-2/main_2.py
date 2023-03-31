from typing import List


# Classe que representa um objeto com duas variáveis: uma lista de inteiros e uma string.


class MyClass1:

    # Inicializa as variáveis do objeto: uma lista de inteiros e uma string.

    def __init__(self, var1: List[int], var2: str):
        self._var1 = var1
        self._var2 = var2

# Define um getter para var1.


@property
def var1(self) -> List[int]:
    return self._var1

# Define um setter para var1


@var1.setter
def var1(self, value: List[int]) -> None:
    self._var1 = value

# Define um getter para var2


@property
def var2(self) -> str:
    return self._var2

# Define um setter para var2


@var2.setter
def var2(self, value: str) -> None:
    self._var2 = value

# Verifica se existem elementos duplicados na lista de inteiros _var1.


def has_duplicates(self) -> bool:
    aux = self._var1.copy()
    aux.sort()
    for i in range(1, len(aux)):
        if aux[i] == aux[i-1]:
            return True
    return False


# Procura por um par de elementos na lista de inteiros _var1 que somados resultam no valor target.

def find_pair(self, target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(self._var1):
        remaining = target - self._var1[i]

        if remaining in seen:
            return [i, seen[remaining]]
        else:
            seen[value] = i

# Rotaciona a lista de inteiros _var1 k vezes.


def rotate_list(self, k: int) -> List[int]:
    nums = self._var1.copy()
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


# Retorna a string var2 invertida

def reverse_string(self) -> str:
    return self._var2[::-1]

# Encontra a mediana de duas listas de inteiros x e y.


@staticmethod
def find_median(x: List[int], y: List[int]) -> int:
    z = [*x, *y]
    z.sort()
    if len(z) % 2 == 0:
        result = (z[len(z)//2] + z[len(z)//2-1])/2
    else:
        result = z[len(z)//2]
    return result
