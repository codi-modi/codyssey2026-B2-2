Step 4. 의도된 충돌 해결 실습 2회 (자명 충돌 1회 + 비자명 충돌 1회)
과제 요구사항 4-7절에 따라 팀 전체 최소 2회 이상 충돌 해결 기록(그중 최소 1회는 비자명 충돌 필수)을 남깁니다.

4.1 충돌 #1 (인접 라인 동시 수정 충돌) — 이진걸 & 김동조 페어
같은 파일(README.md)의 같은 라인 구간(프로젝트 한 줄 소개 섹션)을 서로 다르게 수정하여 충돌을 발생시킵니다.

[이진걸 & 김동조] 동시에 같은 main 커밋에서 각자 브랜치 생성:
이진걸: git checkout main && git pull origin main && git checkout -b feature/jgli-readme-intro
김동조: git checkout main && git pull origin main && git checkout -b feature/djkim-readme-intro
[이진걸] README.md 1~3번째 줄을 아래와 같이 수정 후 PR 생성 → 먼저 main에 병합:
# Codyssey 2026 B2-2: 실전 Git 협업 프로젝트
> 4인 개발팀(이진걸, 송근영, 김동조, 민병우)의 GitHub Flow 및 Python 유틸리티 실습 저장소입니다.

커밋(docs: add team overview header to README) 및 푸시 후 PR 생성 → 김동조님이 리뷰/Approve → 먼저 Merge합니다.
[김동조] 로컬의 구버전 기반 브랜치에서 README.md의 동일한 1~3번째 줄을 다르게 수정 후 커밋:
# Python Utility & Git Workflow Lab (Team B2-2)
> 실무 중심의 PR 코드 리뷰, 충돌 해결, 트러블슈팅을 체득하는 협업 레포지토리입니다.

커밋(docs: update README title with workflow lab description) 후 푸시하고 PR을 열면 GitHub 화면에 This branch has conflicts that must be resolved 경고가 표시됩니다.
[김동조] 로컬에서 충돌 재현 및 수동 해결:
git fetch origin
git merge origin/main
# Auto-merging README.md
# CONFLICT (content): Merge conflict in README.md 발생!

README.md를 열면 아래와 같은 충돌 마커가 나타납니다 (이 마커 원문을 복사해 docs/conflict-resolution.md에 그대로 기록합니다):
<<<<<<< HEAD
# Python Utility & Git Workflow Lab (Team B2-2)
> 실무 중심의 PR 코드 리뷰, 충돌 해결, 트러블슈팅을 체득하는 협업 레포지토리입니다.
=======
# Codyssey 2026 B2-2: 실전 Git 협업 프로젝트
> 4인 개발팀(이진걸, 송근영, 김동조, 민병우)의 GitHub Flow 및 Python 유틸리티 실습 저장소입니다.
>>>>>>> origin/main

두 설명의 장점을 모두 살리는 방향(keep both / 통합 리팩토링)으로 마커를 지우고 아래와 같이 정리합니다:
# Codyssey 2026 B2-2: 실전 Git 협업 프로젝트 (Python Utility & Git Workflow Lab)
> 4인 개발팀(이진걸, 송근영, 김동조, 민병우)이 실무 중심의 GitHub Flow, PR 코드 리뷰, 충돌 해결, 트러블슈팅을 체득하는 협업 저장소입니다.

해결 커밋 및 푸시 후 PR을 병합합니다:
git add README.md
git commit -m "docs: resolve merge conflict in README intro by combining both descriptions"
git push origin feature/djkim-readme-intro

4.2 충돌 #2 (비자명 충돌: 파일 이름 변경 vs 파일 내용 수정) — 송근영 & 민병우 페어
과제 명세서 4-7절의 비자명 충돌 조건("한쪽은 파일 이동/이름 변경, 다른 한쪽은 내용 수정")을 정확히 구현합니다.

[송근영 & 민병우] 동시에 최신 main에서 각자 브랜치 분기:
송근영: git checkout main && git pull origin main && git checkout -b feature/kysong-rename-math
민병우: git checkout main && git pull origin main && git checkout -b feature/bwmin-update-math
[송근영] src/math_utils.py를 src/calculator_utils.py로 파일명 변경(git mv) 및 일부 수정 후 먼저 Merge:
git mv src/math_utils.py src/calculator_utils.py
# 파일 상단 독스트링도 "계산기 및 통계 유틸리티 모듈"로 1줄 수정
git add -A
git commit -m "refactor: rename math_utils.py to calculator_utils.py for clarity"
git push -u origin feature/kysong-rename-math

송근영님이 PR을 생성하고(이때 .github/CODEOWNERS의 /src/math_utils.py 경로도 /src/calculator_utils.py로 함께 업데이트하면 더욱 깔끔합니다), 민병우님이 리뷰/Approve하여 main에 먼저 병합합니다.
[민병우] 구버전 브랜치에서 기존 src/math_utils.py 파일 내부에 함수를 추가하거나 수정 후 커밋:
민병우님의 브랜치에는 아직 src/math_utils.py가 존재합니다. 이 파일의 상단 독스트링과 내용을 수정하고 calculate_median 함수를 추가한 뒤 커밋합니다:
git add src/math_utils.py
git commit -m "feat: add calculate_median function to math_utils"
git push -u origin feature/bwmin-update-math

[민병우] 로컬에서 origin/main 병합 시 이름 변경 충돌(CONFLICT (modify/delete) 또는 rename conflict) 확인 및 해결:
git fetch origin
git merge origin/main

git status로 충돌 상태를 확인하고, 민병우님이 작성한 calculate_median 코드를 새 파일인 src/calculator_utils.py로 통합 반영한 뒤(구 파일이 남아 있다면 git rm src/math_utils.py), 정상 실행 여부를 검증하고 커밋·푸시합니다:
python3 src/calculator_utils.py
git add src/calculator_utils.py
git commit -m "fix: resolve rename-modify conflict by migrating median function to calculator_utils.py"
git push origin feature/bwmin-update-math

송근영님이 PR을 리뷰 및 Approve하면 민병우님이 병합합니다.
Step 5. 2차 스프린트 — 필수 협업 문서 3종 완성 및 SUBMISSION.md 작성
이제 4명이 각자 2번째(또는 추가) PR을 올려 문서 3종 + README.md + SUBMISSION.md를 완성하고, 전원 PR 2개·리뷰 2개 요건을 최종 달성합니다.

5.1 [김동조] PR #2차: docs/conflict-resolution.md 작성 (리뷰어: 민병우)
이슈 생성 후 feature/djkim-conflict-log 브랜치에서 docs/conflict-resolution.md를 작성합니다.
Step 4에서 수행한 충돌 기록 #1(이진걸 & 김동조, README.md 동일 라인 수정)과 충돌 기록 #2(송근영 & 민병우, math_utils.py → calculator_utils.py 파일 이름 변경 vs 내용 수정 비자명 충돌)에 대해:
참여자(작성자/상대) / 상황(What happened) / 충돌 내용(Conflict markers 원문) / 해결 과정(How - 선택한 전략과 실제 실행 명령어) / 결과(Outcome - 관련 PR 및 커밋 링크) / 배운 점(Learnings) 6개 하위 섹션을 빠짐없이 채웁니다.