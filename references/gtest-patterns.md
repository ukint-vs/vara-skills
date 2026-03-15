# Gtest Patterns

## Default Path

- Prefer `GtestEnv` and generated clients for standard Sails verification.
- Drop to raw `gtest::Program` calls only when you are debugging routing, payload encoding, failure logs, or timing at a lower level than the generated client exposes.

## Raw `send_bytes` Mental Model

- `Program::send_bytes(...)` returns a `MessageId`.
- `System::run_next_block()` returns a `BlockRunResult`.
- Replies and failures are inspected from that `BlockRunResult`, not from the `send_bytes` return value.

```rust
let msg_id = program.send_bytes(sender, payload);
let r = system.run_next_block();

assert!(!r.failed.contains(&msg_id));

let reply = r
    .log()
    .iter()
    .find(|entry| entry.reply_to() == Some(msg_id))
    .expect("reply log missing");
```

## What To Inspect

- `r.log()` contains the block logs and replies that landed in that block.
- `r.failed.contains(&msg_id)` is the first quick check for command-path failure.
- `reply.reply_code()` tells you whether the reply was a success or an error.
- The payload still needs decoding after you extract the matching reply log entry.

## Multi-Block And Delayed Behavior

- Use `system.run_to_block(n)` when delayed sends, wakeups, or reservation expiry depend on block height.
- `run_next_block()` is enough only when the full effect should land in the very next block.
- For Sails `GtestEnv`, choose `BlockRunMode::Next` or `BlockRunMode::Manual` when the test must expose exact timing.

## Reply Decoding Reminder

- Generated clients handle reply prefixes for you.
- In raw tests, the reply payload may still carry route-prefix framing, so decode only after matching the correct log entry.
- If the goal is not codec or routing debugging, go back to the generated client path.

## Setup Ergonomics

- `Program<'_>` borrows `System`, so a helper usually cannot return `(System, Program<'_>)` without running into lifetime friction.
- Prefer either:
  - a helper that returns only `System`, then build `Program` inside each test
  - a helper that performs the setup inline per test when the borrow would otherwise escape

## Failure Patterns

- `ReplyIsMissing` usually means the wrong block mode or missing block advancement.
- `UserspacePanic` is often the expected assertion target for fatal command-path validation.
- For low-level debugging, record the `MessageId`, the block you ran, and the relevant `BlockRunResult` evidence in the test note.
