"""텍스트 및 컬렉션 빈도 계산 유틸리티 모듈 (담당: 민병우)."""


def count_words(text: str) -> dict[str, int]:
   """문자열 내 단어별 등장 횟수를 소문자 기준으로 집계합니다."""
   counts: dict[str, int] = {}
   for word in text.lower().split():
       counts[word] = counts.get(word, 0) + 1
   return counts


def count_vowels(text: str) -> int:
   """문자열에 포함된 영문 모음(a, e, i, o, u)의 개수를 반환합니다."""
   vowels = set("aeiouAEIOU")
   return sum(1 for char in text if char in vowels)


if __name__ == "__main__":
   print(count_words("git flow git pr flow git"))  # {'git': 3, 'flow': 2, 'pr': 1}
   print(count_vowels("Codyssey Collaboration"))   # 8