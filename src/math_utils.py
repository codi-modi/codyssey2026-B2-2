"""수학 및 기초 통계 유틸리티 모듈 (담당: 송근영)."""
def calculate_average(numbers: list[float], ndigits: int | None = None) -> float:
    """숫자 리스트의 산술 평균을 계산하여 반환합니다."""
    if not numbers:
        # 빈 리스트는 평균을 계산할 수 없으므로, 호출부가 예외 없이 처리할 수 있게 0.0을 반환합니다.
        return 0.0

    average = sum(numbers) / len(numbers)

    if ndigits is not None:
        return round(average, ndigits)

    return average

def factorial(n: int) -> int:
    """음이 아닌 정수 n의 팩토리얼(n!)을 계산합니다."""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.") 
    result = 1
    for i in range(2, n + 1): 
        result *= i
    return result
#충돌 실습을 위해 추가한 함수
def calculate_median(numbers: list[float]) -> float:
    """숫자 리스트의 중앙값(Median)을 계산하여 반환합니다."""
    if not numbers:
        return 0.0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # 짝수 개일 경우 가운데 두 값의 평균
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        # 홀수 개일 경우 정확히 가운데 값
        return float(sorted_numbers[mid])


if __name__ == "__main__":
    print(calculate_average([10, 20, 30])) # 20.0
    print(factorial(5))                    # 120