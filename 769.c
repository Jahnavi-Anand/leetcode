#include <stdio.h>

int maxChunksToSorted(int* arr, int arrSize) {
    int chunks = 0, maxSoFar = 0;

    for (int i = 0; i < arrSize; i++) {
        if (arr[i] > maxSoFar)
            maxSoFar = arr[i];
        if (maxSoFar == i)
            chunks++;
    }

    return chunks;
}
