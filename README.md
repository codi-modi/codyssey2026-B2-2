# Codyssey 2026 B2-2: Python Utility & Git Workflow Lab

4인 개발팀(이진걸, 송근영, 김동조, 민병우)이 Python 유틸리티 모듈을 함께 만들며 GitHub Flow, Pull Request, 코드 리뷰, 충돌 해결, 트러블슈팅을 실습하는 협업 저장소입니다.

이 저장소는 단순히 Python 함수를 작성하는 것에 그치지 않고, 실제 팀 개발에서 자주 만나는 이슈 생성, 브랜치 분기, PR 작성, 리뷰 반영, 병합 충돌 해결, Git 명령 실수 복구 과정을 문서와 코드로 남기는 것을 목표로 합니다.

## 프로젝트 목표

- GitHub Flow 기반 협업 흐름을 실습합니다.
- 팀원별 Python 유틸리티 모듈을 구현합니다.
- Pull Request와 코드 리뷰를 통해 변경 사항을 검증합니다.
- 의도적인 충돌 상황을 재현하고 해결 과정을 기록합니다.
- `amend`, `reset --soft`, `revert`, `stash` 같은 Git 트러블슈팅 시나리오를 실습합니다.
- 협업 규칙, 충돌 해결 기록, 트러블슈팅 로그를 문서화합니다.

## 팀 소개

- 이진걸: 문자열 유틸리티 담당
- 송근영: 계산 및 기초 통계 유틸리티 담당
- 김동조: 리스트 유틸리티 담당
- 민병우: 텍스트 및 컬렉션 카운트 유틸리티 담당

## GitHub Flow 선택 이유

1. `main`과 `feature/*` 브랜치만 사용하므로 브랜치 구조가 단순하고 이해하기 쉽습니다.
2. 모든 변경 사항을 Pull Request 단위로 검토할 수 있어 코드 리뷰와 피드백 반영 기록을 남기기 좋습니다.
3. 짧은 기간의 4인 협업 프로젝트에서 복잡한 Git Flow보다 빠르게 실습하고 병합하기 적합합니다.

## 프로젝트 구조

```text
codyssey2026-B2-2/
├── README.md
├── src/
│   ├── string_utils.py
│   ├── math_utils.py
│   ├── list_utils.py
│   ├── count_utils.py
│   └── test.py
└── docs/
    ├── CONTRIBUTING.md
    ├── conflict-resolution.md
    ├── troubleshooting-log.md
    ├── b2_2_basic_plan.md
    ├── b2_2_action_plan.md
    ├── b2_2_mission.md
    ├── b2_2_Eval.md
    ├── .github/
    │   ├── CODEOWNERS
    │   └── pull_request.template.md
    ├── raw_logs/
    └── screenshots/
```

## 실행 방법

저장소 루트에서 각 유틸리티 모듈을 직접 실행할 수 있습니다.

```powershell
python src/string_utils.py
python src/math_utils.py
python src/list_utils.py
python src/count_utils.py
```

## 유틸리티 모듈 사용 예시

### 문자열 유틸리티: `src/string_utils.py`

담당: 이진걸

주요 함수:

- `to_snake_case(text: str) -> str`
- `reverse_words(text: str) -> str`

사용 예시:

```python
from src.string_utils import to_snake_case, reverse_words

print(to_snake_case("Codyssey Git Collaboration"))
# codyssey_git_collaboration

print(reverse_words("hello codyssey world"))
# world codyssey hello
```

설명:

- `to_snake_case()`는 공백, 하이픈, 언더스코어로 구분된 문자열을 소문자 `snake_case`로 변환합니다.
- `reverse_words()`는 문장 안의 단어 순서를 반대로 뒤집습니다.

### 계산 및 기초 통계 유틸리티: `src/math_utils.py`

담당: 송근영

주요 함수:

- `calculate_average(numbers: list[float], ndigits: int | None = None) -> float`
- `factorial(n: int) -> int`
- `calculate_median(numbers: list[float]) -> float`

사용 예시:

```python
from src.math_utils import calculate_average, factorial, calculate_median

print(calculate_average([10, 20, 30]))
# 20.0

print(calculate_average([1, 2, 2], ndigits=2))
# 1.67

print(factorial(5))
# 120

print(calculate_median([3, 1, 2]))
# 2.0
```

설명:

- `calculate_average()`는 숫자 리스트의 평균을 계산합니다. 빈 리스트는 평균을 계산할 수 없으므로 `0.0`을 반환합니다.
- `ndigits`를 전달하면 `round()`를 사용해 평균값의 소수점 자릿수를 조절합니다.
- `factorial()`은 음이 아닌 정수의 팩토리얼을 계산합니다. 음수 입력 시 `ValueError`를 발생시킵니다.
- `calculate_median()`은 숫자 리스트의 중앙값을 계산합니다.

### 리스트 유틸리티: `src/list_utils.py`

담당: 김동조

주요 함수:

- `deduplicate_preserve_order(items: list[Any]) -> list[Any]`
- `chunk_list(items: list[Any], size: int) -> list[list[Any]]`

사용 예시:

```python
from src.list_utils import deduplicate_preserve_order, chunk_list

print(deduplicate_preserve_order([3, 1, 2, 3, 2, 4]))
# [3, 1, 2, 4]

print(chunk_list([1, 2, 3, 4, 5], 2))
# [[1, 2], [3, 4], [5]]
```

설명:

- `deduplicate_preserve_order()`는 원래 순서를 유지하면서 중복 값을 제거합니다.
- `chunk_list()`는 리스트를 지정한 크기 단위로 나눕니다. `size`가 0 이하이면 `ValueError`를 발생시킵니다.

### 카운트 유틸리티: `src/count_utils.py`

담당: 민병우

주요 함수:

- `count_words(text: str) -> dict[str, int]`
- `count_vowels(text: str) -> int`

사용 예시:

```python
from src.count_utils import count_words, count_vowels

print(count_words("git flow git pr flow git"))
# {'git': 3, 'flow': 2, 'pr': 1}

print(count_vowels("Codyssey Collaboration"))
# 8
```

설명:

- `count_words()`는 문자열을 소문자로 변환한 뒤 단어별 등장 횟수를 계산합니다.
- 쉼표, 마침표, 물음표, 느낌표 등 기본 문장 부호를 제거하고 집계합니다.
- `count_vowels()`는 문자열 안의 영문 모음 `a`, `e`, `i`, `o`, `u` 개수를 계산합니다.

## 협업 문서 바로가기

- [팀 협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 로그](docs/troubleshooting-log.md)
- [기본 계획서](docs/b2_2_basic_plan.md)
- [실행 계획서](docs/b2_2_action_plan.md)
- [미션 문서](docs/b2_2_mission.md)
- [평가 문서](docs/b2_2_Eval.md)
- [CODEOWNERS](docs/.github/CODEOWNERS)
- [Pull Request 템플릿](docs/.github/pull_request.template.md)
- [충돌 원본 로그](docs/raw_logs/conflict-resolution_raw.md)
- [트러블슈팅 원본 로그](docs/raw_logs/troubleshooting_raw.md)

## 협업 규칙 요약

### 브랜치 전략

- `main` 브랜치는 항상 안정적인 상태로 유지합니다.
- 기능 추가, 문서 수정, 버그 수정은 `feature/*` 브랜치에서 진행합니다.
- 작업 브랜치 이름은 `feature/<작성자이름>-<작업주제>` 형식을 권장합니다.

예:

```text
feature/jglee-string-utils
feature/kysong-math-utils
feature/djkim-list-utils
feature/bwmin-count-utils
```

### 커밋 메시지

커밋 메시지는 변경 목적이 드러나도록 작성합니다.

예:

```text
feat: add string utility functions
fix: strip punctuation before counting words
docs: update troubleshooting log
refactor: rename math utils module
```

### Pull Request

PR에는 아래 항목을 포함합니다.

- 연결 이슈: `Closes #이슈번호`
- 변경 사항: 어떤 파일과 기능을 바꿨는지
- 변경 이유: 왜 필요한 작업인지
- 테스트/검증 방법: 실행 명령과 확인 결과
- 리뷰 요청 사항: 리뷰어가 중점적으로 봐야 할 부분

## 충돌 해결 실습

충돌 해결 기록은 [docs/conflict-resolution.md](docs/conflict-resolution.md)에 정리되어 있습니다.

실습한 충돌 유형:

- `README.md` 동일 구간 동시 수정 충돌
- `src/math_utils.py`에서 파일 이름 변경과 내용 수정이 겹친 비자명 충돌

각 충돌 기록에는 상황, 충돌 원인, 해결 전략, 실제 명령어, 스크린샷 증빙이 포함되어 있습니다.

## Git 트러블슈팅 실습

트러블슈팅 기록은 [docs/troubleshooting-log.md](docs/troubleshooting-log.md)에 정리되어 있습니다.

실습한 시나리오:

- `git commit --amend`: 직전 커밋 메시지 수정
- `git reset --soft HEAD~1`: 로컬 커밋 취소 및 변경 유지
- `git revert`: push된 커밋을 안전하게 취소
- `git stash` / `git stash pop`: 작업 중 변경사항 임시 보관 후 복원

## 리뷰 책임

리뷰 책임은 [docs/.github/CODEOWNERS](docs/.github/CODEOWNERS)에 정의되어 있습니다.

예:

```text
/src/string_utils.py
/src/math_utils.py
/src/list_utils.py
/src/count_utils.py
/docs/
```

GitHub에서는 CODEOWNERS 설정을 통해 특정 파일이나 폴더 변경 시 담당자에게 리뷰를 요청할 수 있습니다.

## 참고

- 이 프로젝트는 Git 협업 실습을 위한 교육용 저장소입니다.
- 일부 문서는 실습 과정에서 발생한 실제 충돌과 터미널 출력, 스크린샷을 포함합니다.
- `src/test.py`는 실습용 빈 테스트 파일로 유지되어 있습니다.