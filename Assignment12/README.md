
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

# Assignment 12: E-Commerce Order Processing System Using SOLID Principles

## Objective

Design and implement an Order Processing System for an e-commerce platform using either **Java** or **Python**. The system must support multiple payment methods, notification channels, order types, and storage mechanisms while strictly adhering to the **SOLID Design Principles**.

The primary goal of this assignment is to demonstrate how object-oriented design principles can be used to build a flexible, maintainable, and extensible software system.

---

## Problem Statement

An e-commerce platform requires an order processing system capable of:

* Creating customer orders
* Processing payments through different payment methods
* Sending notifications through various communication channels
* Persisting order information using different storage mechanisms

The system should be designed in a way that allows new features to be added with minimal modification to existing code.

---

## Functional Requirements

### 1. Order Management

The system must support multiple order types, such as:

* Regular Order
* Discounted Order
* Priority Order

Each order type may have its own processing behavior while maintaining compatibility with the overall order workflow.

---

### 2. Payment Processing

The system must support multiple payment methods, including but not limited to:

* Credit Card Payment
* UPI Payment
* Wallet Payment

The design should allow additional payment methods to be added in the future without modifying existing business logic.

---

### 3. Notification System

After a successful order and payment process, the system should notify the customer through one or more channels, such as:

* Email Notification
* SMS Notification
* Push Notification

The notification mechanism should be easily extensible for future communication channels.

---

### 4. Order Storage

Order information must be persisted using interchangeable storage mechanisms, such as:

* Database Storage
* File Storage

The system should support adding new storage implementations without changing existing service logic.

---

## Design Constraints

Your implementation must follow all five SOLID principles.

---

## SOLID Principles Requirements

### 1. Single Responsibility Principle (SRP)

Each class should have only one responsibility.

Examples:

* Order-related logic should belong to order classes.
* Payment processing should be handled separately.
* Notification handling should be managed independently.
* Data storage should be isolated from business logic.

A class should have only one reason to change.

---

### 2. Open/Closed Principle (OCP)

The system should be open for extension but closed for modification.

You should be able to add:

* New payment methods
* New notification channels
* New storage mechanisms
* New order types

without modifying existing classes or services.

---

### 3. Liskov Substitution Principle (LSP)

All subclasses should be replaceable through their base types without affecting correctness.

Examples:

* Any payment implementation should be usable wherever a payment abstraction is expected.
* Any order type should function correctly when treated as a generic order.
* Any notification implementation should work through the notification abstraction.

No subclass should violate expected behavior.

---

### 4. Interface Segregation Principle (ISP)

Avoid creating large, monolithic interfaces.

Instead, create focused and role-specific interfaces.

Examples:

* Payment-related interfaces should only contain payment operations.
* Notification-related interfaces should only contain notification operations.
* Storage-related interfaces should only contain persistence operations.

Classes should not be forced to implement methods they do not need.

---

### 5. Dependency Inversion Principle (DIP)

High-level modules must depend on abstractions rather than concrete implementations.

Examples:

* The order processing service should depend on payment abstractions.
* The order processing service should depend on notification abstractions.
* The order processing service should depend on storage abstractions.

Use dependency injection to provide concrete implementations.

---

## Expected Workflow

The system should execute the following sequence:

1. Create an order.
2. Select a payment method.
3. Process the payment.
4. Verify successful payment.
5. Send notification to the customer.
6. Save order details using the configured storage mechanism.
7. Complete the order processing workflow.

---

## Suggested Components

Your design may include abstractions and implementations for:

### Order Types

* Regular Order
* Discounted Order
* Priority Order

### Payment Methods

* Credit Card Payment
* UPI Payment
* Wallet Payment

### Notification Channels

* Email Notification
* SMS Notification
* Push Notification

### Storage Mechanisms

* Database Storage
* File Storage

### Service Layer

* Order Processing Service

---

## Extensibility Requirements

Your design should make it easy to introduce future enhancements such as:

### Additional Payment Methods

Examples:

* Net Banking
* Cryptocurrency
* Buy Now Pay Later (BNPL)

### Additional Notification Channels

Examples:

* WhatsApp Notification
* Telegram Notification
* In-App Notification

### Additional Storage Options

Examples:

* Cloud Storage
* NoSQL Database
* Distributed Storage Systems

These additions should require minimal or no modification to existing classes.

---

## Deliverables

Submit:

1. Source code written in Java or Python.
2. Appropriate class and interface definitions.
3. Demonstration program showing:

   * Order creation
   * Payment processing
   * Notification delivery
   * Order storage
4. Brief explanation of how each SOLID principle is applied in the design.

---

## Evaluation Criteria

Your solution will be evaluated based on:

* Correct application of SOLID principles
* Proper use of abstraction and inheritance
* Extensibility of the design
* Code organization and maintainability
* Separation of concerns
* Use of dependency injection
* Demonstration of the complete order workflow

---

## Learning Outcomes

After completing this assignment, you should be able to:

* Apply SOLID principles in real-world system design.
* Design flexible and maintainable object-oriented systems.
* Use abstraction and dependency inversion effectively.
* Build extensible architectures that support future enhancements.
* Understand how design patterns and interfaces improve software quality.
