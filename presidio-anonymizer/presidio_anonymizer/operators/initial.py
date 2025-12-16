"""Replaces the PII text entity with it's initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Modify the string into characters - John Doe becomes J.D."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return text
        
        pieces = [p for p in text.strip().split() if p]
        initials = [
            f"{p[0].upper()}."
            for p in pieces 
            if p[0].isalpha()
            ]

        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
