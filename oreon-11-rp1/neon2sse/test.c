#include <NEON_2_SSE.h>
#include <stdio.h>

int main() {
    // Initialize two 8-element vectors
    uint64_t a = 0x0102030405060708;
    uint64_t b = 0x0807060504030201;

    // Create NEON vectors
    uint8x8_t va = vcreate_u8(a);
    uint8x8_t vb = vcreate_u8(b);

    // Perform the addition
    uint8x8_t vc = vadd_u8(va, vb);

    // Store the resulting vector for comparison
    union {
        char c[8];
        uint64_t i;
    } result;
    vst1_u8(result.c, vc);

    // Expected result after adding byte by byte
    uint64_t expected = 0x0909090909090909;

    if (result.i == expected) {
        printf("NEON_2_SSE test passed successfully\n");
    } else {
        fprintf(stderr, "NEON_2_SSE test failed\n");
        return 1;
    }

    return 0;
}
