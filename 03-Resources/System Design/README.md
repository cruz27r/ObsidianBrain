---
tags: [index, system-design]
created: 2026-03-21
---

# System Design — Index

Key topics for software engineering interviews and real-world architecture decisions.

## Topics to build out
- [ ] [[Caching]] — Redis, CDN, cache invalidation strategies
- [ ] [[Load Balancing]] — horizontal scaling, round-robin, sticky sessions
- [ ] [[Databases]] — SQL vs NoSQL, indexing, sharding, replication
- [ ] [[Message Queues]] — async processing, Kafka, RabbitMQ, pub/sub
- [ ] [[API Rate Limiting]] — token bucket, sliding window
- [ ] [[CAP Theorem]] — consistency, availability, partition tolerance
- [ ] [[CDN]] — content delivery, edge caching
- [ ] [[Microservices vs Monolith]] — tradeoffs, when to split
- [ ] [[Authentication & Authorization]] — JWT, sessions, OAuth

## Framework for answering system design questions
1. Clarify requirements — functional + non-functional (scale, latency, availability)
2. Estimate scale — DAU, requests/sec, storage needs
3. High-level design — boxes and arrows
4. Deep dive — bottlenecks, data model, API design
5. Tradeoffs — explain what you chose and why
