"""텍스트 및 컬렉션 빈도 계산 유틸리티 모듈 (담당: 민병우)."""

def count_words(text: str) -> dict[str, int]:
   """문자열 내 단어별 등장 횟수를 소문자 기준으로 집계합니다. (문장 부호 제거 포함)"""
   counts: dict[str, int] = {}
   # 양끝의 흔한 문장 부호(쉼표, 마침표, 물음표, 느낌표 등)를 제거합니다.
   strip_chars = ",.?!\":;"
   for word in text.lower().split():
       cleaned_word = word.strip(strip_chars)
       if cleaned_word:  # 빈 문자열이 아닐 경우에만 집계
           counts[cleaned_word] = counts.get(cleaned_word, 0) + 1
   return counts

def count_vowels(text: str) -> int:
   """문자열에 포함된 영문 모음(a, e, i, o, u)의 개수를 반환합니다."""
   vowels = set("aeiouAEIOU")
   return sum(1 for char in text if char in vowels)


if __name__ == "__main__":
   print(count_words("git flow git pr flow git"))  # {'git': 3, 'flow': 2, 'pr': 1}
   print(count_vowels("Codyssey Collaboration"))   # 8