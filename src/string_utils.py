"""문자열 처리 유틸리티 모듈 (담당: 이진걸)."""


def to_snake_case(text: str) -> str:
    """공백이나 하이픈으로 구분된 문자열을 snake_case로 변환합니다."""
    cleaned = text.strip().replace("-", " ")
    return "_".join(word.lower() for word in cleaned.split())


def reverse_words(text: str) -> str:
    """문장 내 단어 순서를 역순으로 뒤집어 반환합니다."""
    return " ".join(reversed(text.split()))


if __name__ == "__main__":
    print(to_snake_case("Codyssey Git Collaboration"))  # codyssey_git_collaboration
    print(reverse_words("hello codyssey world"))        # world codyssey hello
