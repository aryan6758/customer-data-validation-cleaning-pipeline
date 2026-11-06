from abc import ABC, abstractmethod
import pandas as pd

class BaseValidator(ABC):
    @abstractmethod
    def validate(self, df: pd.DataFrame) -> pd.Series:
        """Returns a boolean Series indicating valid rows."""
        pass
