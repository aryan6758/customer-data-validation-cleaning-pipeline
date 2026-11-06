from abc import ABC, abstractmethod
import pandas as pd

class BaseCleaner(ABC):
    @abstractmethod
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
