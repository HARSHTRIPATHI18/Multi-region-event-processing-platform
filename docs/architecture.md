## Architecture Overview

The system is designed as an event-driven backend where
user-facing request handling is decoupled from background processing.

### Request Flow
1. Client sends request to API Gateway (regional)
2. Ingest Lambda validates request and publishes event
3. EventBridge routes the event asynchronously
4. Processor Lambda handles business logic
5. Data is persisted to DynamoDB

### Design Principles
- Low-latency user-facing path
- No cross-region synchronous calls
- Eventual consistency for background processing
- Failure isolation per region
