#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* =========================================
   STRING BUFFER STRUCT
========================================= */
typedef struct
{
    char *data;
    size_t length;
    size_t capacity;

} StringBuffer;

/* =========================================
   INITIALIZE STRING BUFFER
========================================= */
StringBuffer *sb_init(size_t initial_capacity)
{
    // Allocate memory for struct
    StringBuffer *sb = (StringBuffer *)malloc(sizeof(StringBuffer));

    if (sb == NULL)
    {
        printf("Memory allocation failed for StringBuffer\n");
        return NULL;
    }

    // Allocate memory for character buffer
    sb->data = (char *)malloc(initial_capacity);

    if (sb->data == NULL)
    {
        printf("Memory allocation failed for data buffer\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;

    // Empty string
    sb->data[0] = '\0';

    return sb;
}

/* =========================================
   APPEND STRING
========================================= */
void sb_append(StringBuffer *sb, const char *str)
{
    size_t str_len = strlen(str);

    // Required size including null terminator
    size_t required = sb->length + str_len + 1;

    // Grow buffer if needed
    while (required > sb->capacity)
    {
        size_t new_capacity = sb->capacity * 2;

        printf("\nBuffer full! Growing from %zu to %zu\n",
               sb->capacity,
               new_capacity);

        // Safe realloc
        char *temp = (char *)realloc(sb->data, new_capacity);

        if (temp == NULL)
        {
            printf("Realloc failed!\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;
    }

    // Append new string
    strcat(sb->data, str);

    // Update length
    sb->length += str_len;

    printf("Current String: %s\n", sb->data);
    printf("Length: %zu | Capacity: %zu\n",
           sb->length,
           sb->capacity);
}

/* =========================================
   FREE MEMORY (DESTRUCTOR)
========================================= */
void sb_free(StringBuffer *sb)
{
    if (sb != NULL)
    {
        free(sb->data);
        free(sb);

        printf("\nMemory freed successfully.\n");
    }
}

/* =========================================
   MAIN FUNCTION
========================================= */
int main()
{
    // Small initial capacity
    StringBuffer *sb = sb_init(8);

    if (sb == NULL)
    {
        return 1;
    }

    // Append strings
    sb_append(sb, "Hello");
    sb_append(sb, " World");
    sb_append(sb, " This");
    sb_append(sb, " is");
    sb_append(sb, " Dynamic");
    sb_append(sb, " Buffer");

    // Free memory
    sb_free(sb);

    return 0;
}