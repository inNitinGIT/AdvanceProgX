/*
=========================================================
MULTITHREADED PRODUCER-CONSUMER USING POSIX THREADS
=========================================================

Concepts Used:
1. pthread_create()
2. pthread_join()
3. Mutex Lock
4. Condition Variables
5. Shared Memory Synchronization
6. Thread Communication

Problem:
- Producer thread adds items into a shared buffer
- Consumer thread removes items from the buffer
- If buffer is FULL -> producer waits
- If buffer is EMPTY -> consumer waits

Compile:
gcc producer_consumer.c -o producer_consumer -lpthread

Run:
./producer_consumer
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define MAX_ITEMS 15

// Shared Buffer
int buffer[BUFFER_SIZE];

int count = 0;
int in = 0;
int out = 0;

// Mutex
pthread_mutex_t mutex;

// Condition Variables
pthread_cond_t not_full;
pthread_cond_t not_empty;

// --------------------------------------------------
// Producer Function
// --------------------------------------------------
void* producer(void* arg)
{
    int item;

    for(item = 1; item <= MAX_ITEMS; item++)
    {
        sleep(1);

        pthread_mutex_lock(&mutex);

        // Wait if buffer is full
        while(count == BUFFER_SIZE)
        {
            printf("Producer waiting... Buffer FULL\n");

            pthread_cond_wait(&not_full, &mutex);
        }

        // Produce item
        buffer[in] = item;

        printf("Producer produced: %d at index %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;
        count++;

        printf("Buffer count after produce: %d\n\n", count);

        // Signal consumer
        pthread_cond_signal(&not_empty);

        pthread_mutex_unlock(&mutex);
    }

    pthread_exit(NULL);
}

// --------------------------------------------------
// Consumer Function
// --------------------------------------------------
void* consumer(void* arg)
{
    int item;

    for(int i = 1; i <= MAX_ITEMS; i++)
    {
        sleep(2);

        pthread_mutex_lock(&mutex);

        // Wait if buffer is empty
        while(count == 0)
        {
            printf("Consumer waiting... Buffer EMPTY\n");

            pthread_cond_wait(&not_empty, &mutex);
        }

        // Consume item
        item = buffer[out];

        printf("Consumer consumed: %d from index %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;
        count--;

        printf("Buffer count after consume: %d\n\n", count);

        // Signal producer
        pthread_cond_signal(&not_full);

        pthread_mutex_unlock(&mutex);
    }

    pthread_exit(NULL);
}

// --------------------------------------------------
// Main Function
// --------------------------------------------------
int main()
{
    pthread_t producerThread;
    pthread_t consumerThread;

    // Initialize mutex
    pthread_mutex_init(&mutex, NULL);

    // Initialize condition variables
    pthread_cond_init(&not_full, NULL);
    pthread_cond_init(&not_empty, NULL);

    // Create threads
    pthread_create(&producerThread, NULL, producer, NULL);
    pthread_create(&consumerThread, NULL, consumer, NULL);

    // Wait for threads
    pthread_join(producerThread, NULL);
    pthread_join(consumerThread, NULL);

    // Destroy synchronization objects
    pthread_mutex_destroy(&mutex);

    pthread_cond_destroy(&not_full);
    pthread_cond_destroy(&not_empty);

    printf("\nAll threads finished successfully.\n");

    return 0;
}