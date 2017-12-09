# ------------------------------------------------------------------
# coding=utf-8
# Modul zawierajacy pakiet najpopularniejszych technik sortowania.
# Author : Mikołaj Szymczuk.
#
# Moduł zawiera :
# -->  Sortowanie bąbelkowe (bubblesort)
# -->  Sortowanie przez wstawianie (insertionsort)
# -->  Sortowanie przez wymianę/wybór (selectionsort)
# -->  Sortowanie szybkie (quicksort)
# -->  Sortowanie stogowe (heapsort)
# -->  Sortowanie przez zliczanie (countingsort)
# -->  Sortowanie przez scalanie (mergesort)
#
# -------------------------------------------------------------------

from random import randint

class PySorter(object):
    """ Klasa sortujaca przyjmujaca na wejsiu ciag do posortowania.
        Klasa zawiera metody inplementujace rozne algorytmy sortujace. """

    def __init__(self, list_to_sort):
        self.array = list_to_sort

    def __str__(self):
        return str(self.array)

    def CompleteTheList(self, leanght, a, b):
        """ Metoda wypelniajaca liste n losowymi liczbami z podanego przedzialu. """

        for i in range(leanght):
            self.array.append(randint(a, b))

    def __CopyList(self):
        """ Metoda kopiujaca ciag. """

        copy = self.array[:]
        return copy

    def BubbleSort(self):
        """ Sortowanie bombelkowe - Polega na porównywaniu dwóch kolejnych elementów i zamianie ich kolejności,
         jeżeli zaburza ona porządek, w jakim się sortuje tablicę. Sortowanie kończy się,
          gdy podczas kolejnego przejścia nie dokonano żadnej zmiany."""

        n = len(self.array) # Zczytanie dlugosci listy.
        copy_list = self.__CopyList() # Kopia podanego ciagu.

        while n > 1:
            for i in range(n - 1): # Przejscie po elementach listy.
                if copy_list[i] > copy_list[i + 1]: # Sprawdzanie 2 kolejnych liczb.
                    copy_list[i], copy_list[i + 1] = copy_list[i + 1], copy_list[i] # Swap(zamiana) dwoch liczb.

            n -= 1

        return copy_list

    def InsertionSort(self):
        n = len(self.array)
        copy_list = self.__CopyList()

        for i in range(1, n):
            kay = copy_list[i]
            j = i - 1

            while j >= 0 and copy_list[j] > kay:
                copy_list[j + 1] = copy_list[j]
                j -= 1
                copy_list[j + 1] = kay

        return copy_list

    def SelcetionSort(self):
        pass

    def QuickSort(self):
        pass

    def HeapSort(self):
        pass

    def CountingSort(self):
        pass

    def MergeSort(self):
        pass

if __name__ == '__main__':
    pass
