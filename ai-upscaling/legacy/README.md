# AI Upscaling — Legacy Layer

This directory contains the legacy upscaling baseline used in the
Engineering by Layers AI Upscaling series.

## What this layer represents

This layer models classical, non-learning image upscaling methods
based entirely on deterministic interpolation rules.

- No training
- No learnable parameters
- No content awareness
- Single-pass, local computation

These methods represent the practical ceiling of rule-based upscaling
as deployed in cameras, video pipelines, and display controllers.

## Implemented methods

- Bilinear interpolation
- Bicubic interpolation (primary reference)
- Lanczos resampling (high-quality classical reference)

## Scaling factors

The baseline is evaluated at:
- 2×
- 3×
- 4×

This progression exposes the point at which classical methods
visibly degrade and fail to recover meaningful detail.

## Scope and limitations

This implementation is intentionally:
- CPU-only
- Single-frame
- Clarity-first

It is not optimised for real-time execution.
In production systems, identical interpolation kernels are implemented
in fixed-function hardware for throughput and power efficiency.

The algorithmic behaviour, however, is identical.

## Why this layer matters

All learning-based models introduced in later layers are evaluated
relative to this baseline. If a method cannot meaningfully outperform
this layer, it does not represent a real advance.
