# Hotel Management System - Producer Consumer Problem

## Overview

The **Hotel Management System** demonstrates the **Producer-Consumer problem** in an operating system context. It simulates a hotel kitchen scenario where **chefs (producers)** prepare dishes and **waiters (consumers)** serve them to customers. The system ensures synchronization using techniques like **semaphores** to prevent race conditions and maintain proper workflow.

---

## Features

### System Features

* **Producer (Chef) Operations:** Prepare dishes and add them to the serving queue.
* **Consumer (Waiter) Operations:** Serve dishes from the queue to customers.
* **Synchronization:** Prevents race conditions using semaphores or mutex locks.
* **Queue Management:** Ensures the buffer (serving table) does not overflow or underflow.
* **Real-time Simulation:** Display real-time production and consumption status.

---

## Technology Stack

| Layer                     | Technology Used           |
| ------------------------- | ------------------------- |
| Programming               | C / C++ / Java            |
| Synchronization           | Semaphores / Mutex        |
| Operating System Concepts | Producer-Consumer Problem |
| Optional                  | GUI (for visualization)   |

---

## Project Structure

```
Hotel-Management-System/
│
├── src/
│   ├── main.c / main.cpp   # Main program demonstrating Producer-Consumer
│   ├── producer.c          # Producer (Chef) operations
│   ├── consumer.c          # Consumer (Waiter) operations
│   └── buffer.c            # Shared buffer management
│
├── include/
│   └── buffer.h            # Header files for buffer and synchronization
│
├── README.md               # Project documentation
└── Makefile                # For compilation (if using C/C++)
```

---

## Problem Description

* **Producers (Chefs):** Prepare dishes at random intervals and add them to a fixed-size buffer.
* **Consumers (Waiters):** Remove dishes from the buffer and serve customers.
* **Synchronization Mechanism:**

  * **Full Semaphore:** Ensures consumers do not take dishes from an empty buffer.
  * **Empty Semaphore:** Ensures producers do not place dishes in a full buffer.
  * **Mutex Lock:** Prevents simultaneous access to the buffer by multiple threads.

---

## Installation & Execution

1. **Clone Repository**

```bash
git clone https://github.com/your-username/Hotel-Management-System.git
cd Hotel-Management-System
```

2. **Compile Program**

   * For C/C++:

```bash
gcc src/*.c -o hotel_management -lpthread
```

* For Java:

```bash
javac src/*.java
```

3. **Run Program**

   * For C/C++:

```bash
./hotel_management
```

* For Java:

```bash
java src/Main
```

---

## Usage

1. Initialize buffer size for the serving table.
2. Start producer (chef) and consumer (waiter) threads.
3. Monitor console output to see dishes being prepared and served in real-time.
4. Observe synchronization and buffer management in action.

---

## Future Enhancements

* Implement **graphical visualization** for production and consumption.
* Add multiple producer and consumer types (e.g., different chefs and waiters).
* Incorporate **priority queues** for high-demand dishes.
* Extend system for full **hotel management simulation** including billing and inventory.

---

## Contributors

| Name           | Role                             |
| -------------- | -------------------------------- |
| Anishk Singh   | Producer-Consumer Implementation |
| Shaurya Dobhal | Producer-Consumer Implementation |
| Ayush Tomar    | Concept Design & Testing         |
| Harshit Kumar Shrotriya    | Concept Design & Testing         |

---

## License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## Contact

For any queries, please contact **Shaurya Dobhal** at [shauryadobhal6@gmail.com].
