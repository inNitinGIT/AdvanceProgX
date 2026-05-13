
![C](https://img.shields.io/badge/language-C-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)



1. sb = sb_init(8)
   → Creates buffer: [________] capacity=8, length=0

2. sb_append(sb, "Hello")
   → "Hello" fits (6 bytes needed)
   → Buffer: [Hello___] length=5, capacity=8

3. sb_append(sb, " World")
   → Needs 12 bytes, only have 8 → GROW to 16
   → Buffer: [Hello World_____] length=11, capacity=16

4. sb_append(sb, " This")
   → " This" is 5 chars, total needs 11+5+1=17
   → 17 > 16? Yes! GROW to 32
   → Buffer: [Hello World This__________] length=15, capacity=32

5. sb_append(sb, " is")
   → 15+2+1=18, fits in 32 ✓
   → Buffer: [Hello World This is________] length=17, capacity=32

6. sb_append(sb, " Dynamic")
   → 17+7+1=25, fits ✓
   → Buffer: [Hello World This is Dynamic____] length=24, capacity=32

7. sb_append(sb, " Buffer")
   → 24+6+1=31, fits ✓
   → Buffer: [Hello World This is Dynamic Buffer] length=30, capacity=32

8. sb_free(sb)
   → Frees data buffer, then frees struct
   → NO MEMORY LEAK!



Heap Memory:

┌─────────────────────┐     ┌─────────────────────────┐
│  StringBuffer       │     │  Data Buffer            │
│  (struct)           │     │                         │
│  ┌───────────────┐  │     │  ┌─────┬─────┬─────┐   │
│  │ data ─────────┼──┼────→│  │  H  │  i  │ \0  │   │
│  │ length = 2    │  │     │  └─────┴─────┴─────┘   │
│  │ capacity = 8  │  │     │                         │
│  └───────────────┘  │     └─────────────────────────┘
└─────────────────────┘



$ ./app
Hello World This is Dynamic Buffer

Append Operation:
- Average Time Complexity: O(1)
- Worst Case (resize): O(n)


## Future Improvements

- Insert at index
- Delete substring
- Reserve capacity
- Shrink buffer
- UTF-8 support