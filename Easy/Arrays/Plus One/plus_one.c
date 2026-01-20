#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

int* plusOne(int* digits, int digitsSize, int* returnSize) {
    
    bool allNine = true;

    // Step 1: Check if all digits are 9
    // arr[i] == *(&arr + i*sizeof(type))
    for (int i = 0; i < digitsSize; i++) {
        if (digits[i] != 9) {
            allNine = false;
            break;
        }
    }

    // Step 2: If all digits are 9
    if (allNine) {
        int* result = (int*)malloc((digitsSize + 1) * sizeof(int));
        result[0] = 1;

        for (int i = 1; i <= digitsSize; i++) {
            result[i] = 0;
        }

        *returnSize = digitsSize + 1;
        return result;
    }

    // Step 3: If not all digits are 9
    int* result = (int*)malloc(digitsSize * sizeof(int));

    // Copy original digits
    for (int i = 0; i < digitsSize; i++) {
        result[i] = digits[i];
    }

    // Add 1 from the end
    for (int i = digitsSize - 1; i >= 0; i--) {
        if (result[i] == 9) {
            result[i] = 0;
        } else {
            result[i]++;
            break;
        }
    }

    *returnSize = digitsSize;
    return result;
}

int main() {
    int digits[] = {9, 9, 9};
    int digitsSize = 3;
    int returnSize;

    int* result = plusOne(digits, digitsSize, &returnSize);

    printf("Result: ");
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    // Free allocated memory
    free(result);

    return 0;
}
