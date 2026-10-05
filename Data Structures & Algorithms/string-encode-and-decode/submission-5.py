class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "#aks"
        s = "_*_".join(s for s in strs)
        return s

    def decode(self, s: str) -> List[str]:
        if s == "#aks":
            return []
        x = s.split("_*_")
        return x