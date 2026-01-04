## Failure Scenarios & Handling

### API Lambda Failure
- API Gateway retries
- Client receives error response

### EventBridge Failure
- EventBridge retries event delivery
- No impact on client latency

### Processor Lambda Failure
- Automatic retries
- Idempotent processing using event_id

### Regional Outage
- Traffic can be routed to another region
- No cross-region dependency in request path

### Consistency Trade-off
- Eventual consistency accepted for background events
- Availability and latency prioritized
