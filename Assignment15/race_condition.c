
#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define INCREMENTS 1000000

long long counter = 0;   // Shared global counter

void* increment_counter(void* arg)
{
    for (int i = 0; i < INCREMENTS; i++)
    {
        counter++;   // Critical section (NOT protected)
    }

    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    // Create threads
    for (int i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    // Wait for all threads to finish
    for (int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("Final Counter Value: %lld\n", counter);
    printf("Expected Value: %lld\n",
           (long long)NUM_THREADS * INCREMENTS);

    return 0;
}