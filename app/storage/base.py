from typing import List, Dict

class Storage:
    def save(self, data: List[Dict]) -> int:
        raise NotImplementedError

    def load(self) -> Dict[str, Dict]:
        raise NotImplementedError
