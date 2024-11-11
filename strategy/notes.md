# Strategy Pattern

- for situations where flow is identical but implementation details, i.e. algo or other internals, differ
- often used with abstract class to inherit interface requirements (FancyStrategy < AbstractStrategy)

## Typical Use Case

- payment provider implementations (payment_handler.process_payment -> strategy: BraintreePaymentStrategy)
- sorting implementations (results.sort -> strategy: RelevanceSortStrategy)
- validation (input -> strategy: URLValidationStrategy)
- basically anything where the overarching action is the same but the internals differ meaningfully
