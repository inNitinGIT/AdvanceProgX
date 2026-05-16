/*
=========================================================
MULTITHREADED PRODUCER-CONSUMER USING SEMAPHORES
=========================================================

Concepts Used:
1. pthread_create()
2. pthread_join()
3. Semaphores
4. Mutex Lock
5. Shared Memory Synchronization
6. Thread Communication

Problem:
- Producer thread adds items into a shared buffer
- Consumer thread removes items from the buffer
- If buffer is FULL -> producer waits
- If buffer is EMPTY -> consumer waits

Semaphores Used:
1. empty -> counts empty slots
2. full  -> counts filled slots

Compile:
gcc producer_consumer_semaphore.c -o producer_consumer_semaphore -lpthread

Run:
./producer_consumer_semaphore
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

#define BUFFER_SIZE 5
#define MAX_ITEMS 15

// Shared Buffer
int buffer[BUFFER_SIZE];

int in = 0;
int out = 0;

// Mutex for critical section
pthread_mutex_t mutex;

// Semaphores
sem_t empty;
sem_t full;

// --------------------------------------------------
// Producer Function
// --------------------------------------------------
void* producer(void* arg)
{
    int item;

    for(item = 1; item <= MAX_ITEMS; item++)
    {
        sleep(1);

        // Wait for empty slot
        sem_wait(&empty);

        // Enter critical section
        pthread_mutex_lock(&mutex);

        // Produce item
        buffer[in] = item;

        printf("Producer produced: %d at index %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;

        // Exit critical section
        pthread_mutex_unlock(&mutex);

        // Signal that buffer has new item
        sem_post(&full);
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

        // Wait for filled slot
        sem_wait(&full);

        // Enter critical section
        pthread_mutex_lock(&mutex);

        // Consume item
        item = buffer[out];

        printf("Consumer consumed: %d from index %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;

        // Exit critical section
        pthread_mutex_unlock(&mutex);

        // Signal empty slot available
        sem_post(&empty);
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

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    // Create threads
    pthread_create(&producerThread, NULL, producer, NULL);
    pthread_create(&consumerThread, NULL, consumer, NULL);

    // Wait for threads to finish
    pthread_join(producerThread, NULL);
    pthread_join(consumerThread, NULL);

    // Destroy mutex
    pthread_mutex_destroy(&mutex);

    // Destroy semaphores
    sem_destroy(&empty);
    sem_destroy(&full);

    printf("\nAll threads finished successfully.\n");

    return 0;
}