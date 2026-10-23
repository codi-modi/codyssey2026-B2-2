"""리스트 가공 및 분할 유틸리티 모듈 (담당: 김동조)."""

from typing import Any


def deduplicate_preserve_order(items: list[Any]) -> list[Any]:
    """원소 순서를 유지하면서 중복을 제거한 새 리스트를 반환합니다."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def chunk_list(items: list[Any], size: int) -> list[list[Any]]:
    """리스트를 지정된 크기(size) 단위의 서브 리스트로 분할합니다."""
    if size <= 0:
        raise ValueError("분할 크기(size)는 1 이상이어야 합니다.")
    return [items[i : i + size] for i in range(0, len(items), size)]


if __name__ == "__main__":
    print(deduplicate_preserve_order([3, 1, 2, 3, 2, 4]))  # [3, 1, 2, 4]
    print(chunk_list([1, 2, 3, 4, 5], 2))                  # [[1, 2], [3, 4], [5]]
# 잘못 추가된 임시 설정
