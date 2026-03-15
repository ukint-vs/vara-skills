# Sails RS Imports And Release Defaults

## Current Baseline

- Use `sails-rs 0.10.2` as the pack baseline unless the target repo already pins a newer compatible patch.
- Prefer teaching the current template defaults from that release instead of older blog posts or copied snippets.

## Cargo Defaults

### App Or Wasm Crate

```toml
[dependencies]
sails-rs = "0.10.2"

[build-dependencies]
sails-rs = { version = "0.10.2", features = ["wasm-builder"] }
sails-idl-gen = "0.10.2"

[dev-dependencies]
sails-rs = { version = "0.10.2", features = ["gtest"] }
```

### Dedicated Client Crate

```toml
[dependencies]
sails-rs = "0.10.2"

[build-dependencies]
sails-client-gen = "0.10.2"
sails-idl-gen = "0.10.2"
```

- `sails-rs 0.10.2` still exposes `features = ["build"]` as an alias, and some older repos still use it.
- For new program or wasm crate guidance, prefer `features = ["wasm-builder"]` because that is what the official templates and README teach now.

## Common Imports

```rust
use sails_rs::{cell::RefCell, prelude::*};
use sails_rs::collections::BTreeMap;
use sails_rs::gstd::{exec, msg};
```

- Reach for `RefCell` when the program owns mutable state and services borrow it.
- Use `sails_rs::collections::*` when you want `no_std`-friendly collections through the framework path.
- Import `exec` and `msg` from `sails_rs::gstd` for standard Gear or Vara Sails programs.

## Export And Event Rules

- In `0.10.2`, treat `#[export]` as mandatory for every service method that should be publicly callable.
- Public Rust methods without `#[export]` are implementation details, not remote Sails routes.
- Use `self.emit_event(...)`, not `notify_on(...)`.

```rust
#[derive(Encode, Decode, TypeInfo)]
#[codec(crate = sails_rs::scale_codec)]
#[scale_info(crate = sails_rs::scale_info)]
pub enum Event {
    Updated(u64),
}

#[service(events = Event)]
impl CounterService<'_> {
    #[export]
    pub fn add(&mut self, by: u64) {
        self.value += by;
        self.emit_event(Event::Updated(self.value))
            .expect("Event error");
    }
}
```

## SCALE Derive Boilerplate

- When shared DTOs or events derive SCALE traits in a `no_std` Sails crate, prefer:
  - `#[codec(crate = sails_rs::scale_codec)]`
  - `#[scale_info(crate = sails_rs::scale_info)]`
- This avoids proc-macro confusion when the crate does not depend on `parity-scale-codec` or `scale-info` directly.

## Agent Notes

- If the repo already pins a newer compatible patch, follow the repo version instead of forcing `0.10.2`.
- Do not tell builders to hand-roll routes or event wiring when generated clients and `emit_event` already cover the standard path.
