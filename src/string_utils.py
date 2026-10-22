"""문자열 처리 유틸리티 모듈 (담당: 이진걸)."""

def to_snake_case(text: str) -> str:
    """공백, 하이픈(-), 또는 언더스코어(_)로 구분된 문자열을 소문자 snake_case로 변환합니다.

    Examples:
        >>> to_snake_case("Codyssey Git Collaboration")
        'codyssey_git_collaboration'
        >>> to_snake_case("hello--world__test")
        'hello_world_test'
        >>> to_snake_case("")
        ''
    """
    if not text or not text.strip():
        return ""

    # 하이픈(-)과 기존 언더스코어(_)를 공백으로 치환하여 연속 분리 처리
    cleaned = text.replace("-", " ").replace("_", " ")
    words = [word.lower() for word in cleaned.split() if word]

    return "_".join(words)

def reverse_words(text: str) -> str:
    """문장 내 단어 순서를 역순으로 뒤집어 반환합니다."""
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    print(to_snake_case("Codyssey Git Collaboration"))  # codyssey_git_collaboration
    print(reverse_words("hello codyssey world"))        # world codyssey hello
