# Delayed Message Pattern

## Use Case

Use this pattern for future-block work such as reminders, auctions, inactivity cleanup, vesting steps, and timeout enforcement.

## Canonical Self-Message Payload

For a standard Sails self-call by route name, encode service, method, and arguments in order, then concatenate:

```rust
let payload = [
    "ReminderBoard".encode(),
    "TriggerReminder".encode(),
    id.encode(),
]
.concat();
```

- This is the route-prefixed byte shape to use when a delayed internal message cannot go through a generated client call directly.
- Keep the service and method names aligned with the exported Sails routes.

## Sending The Delayed Message

```rust
msg::send_bytes_with_gas_delayed(exec::program_id(), payload, gas_limit, 0, delay)
    .expect("failed to schedule delayed self-message");
```

- Use `exec::program_id()` when the program is scheduling work for itself.
- Budget explicit gas for the future execution.
- Keep transferred value at `0` unless the delayed route truly needs value.

## Internal-Only Guard

- The internal-only check is `msg::source() == exec::program_id()`.
- Enforce it at the start of the exported handler so outside callers cannot trigger the internal route directly.

```rust
#[export]
pub fn trigger_reminder(&mut self, id: u64) {
    assert_eq!(msg::source(), exec::program_id(), "internal only");
    self.finish_trigger(id);
}
```

## Reservation And Gas Notes

- Use `ReservationId` only when later execution budget must survive across blocks.
- If a plain delayed send is enough, keep the flow simpler and use config-driven gas limits.
- Recompute or validate critical state inside the delayed handler instead of trusting stale assumptions from the scheduling block.

## Idempotency Rules

- Delayed routes must be safe if the target item was already canceled, completed, or cleaned up.
- Persist enough state to detect stale work.
- Prefer an idempotent no-op or explicit early return over a half-applied mutation.

## Test Guidance

- Use `run_to_block` for delay-sensitive assertions.
- Assert both the scheduler-side effect and the eventual handler-side effect.
- If debugging the raw byte route, test the payload shape directly before blaming gas or timing.
