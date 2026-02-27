# Petit Message Queue (PMQ)

**Petit** (French for “small” or “little”) reflects the goal of this project: a deliberately minimal message queue that focuses on fundamentals rather than scale.

PMQ is a minimal message queue service built in Python to demonstrate the core mechanics behind real-world queue systems: enqueue, lease-based delivery, acknowledgements, retries, and dead-letter handling. The goal is to keep the implementation small, readable, and easy to learn from.

## Motivation

Most production systems rely on managed queues (SQS, Service Bus, Pub/Sub) or brokers (RabbitMQ, Kafka). They solve hard problems well, but they also hide the fundamentals.

MMQ is motivated by building a small, practical queue from scratch to deeply understand:
- how message delivery works under failures
- why “acknowledgements” and “visibility timeouts” exist
- what guarantees are realistic (and what tradeoffs come with them)
- how storage and recovery influence correctness

---

## How It Works

### Message Lifecycle
MMQ follows a lease-based lifecycle:

- **READY**: message is available for consumption
- **IN_FLIGHT**: message is leased to a consumer until a deadline (visibility timeout)
- **ACKED**: message is confirmed processed and removed
- **DLQ**: message is moved to a dead-letter queue after exceeding retry limits

If a consumer does not ack before the lease expires, the message becomes eligible for redelivery.

### Delivery Semantics
MMQ provides **at-least-once delivery**:
- a message will be delivered one or more times until it is acknowledged
- duplicates are possible (e.g., consumer crash after processing but before ack)
- consumers should be idempotent when processing messages

---

## Technical Specification

### Features
- Named queues
- Enqueue messages
- Lease-based consumption (visibility timeout)
- Ack / Nack (requeue) support
- Retry tracking with max-attempts
- Dead-letter queue (DLQ)
- Basic stats and health endpoints (for observability)

### Built With
- **Python** (stdlib-only in production)
- **uv** for project and dependency management
- **HTTP API** for producer/consumer interaction
- **gRPC** support planned as an optional gateway layer

### Architecture
MMQ is designed with a clear separation of concerns:

- **Queue Engine (core)**: owns message state machine, leasing, retries, DLQ rules
- **Storage Layer**: responsible for persistence and recovery (pluggable backends)
- **Protocol Adapters**:
  - HTTP adapter maps requests to core engine commands
  - gRPC adapter (optional) exposes the same engine capabilities via RPC

---

## License

MIT