from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CodeBlock:
    """Minimal code-block resource model."""

    physical_qubits: int
    logical_qubits: int

    @property
    def encoding_rate(self) -> float:
        if self.physical_qubits <= 0:
            raise ValueError("physical_qubits must be positive")
        return self.logical_qubits / self.physical_qubits


def physical_qubits_required(logical_qubits: int, encoding_rate: float) -> int:
    """Ceiling estimate for physical qubits from logical qubits and code rate."""
    if logical_qubits < 0:
        raise ValueError("logical_qubits must be non-negative")
    if not (0 < encoding_rate <= 1):
        raise ValueError("encoding_rate must be in (0, 1]")
    return int(-(-logical_qubits // encoding_rate))
