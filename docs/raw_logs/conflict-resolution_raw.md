Step4. 의도된 충돌 해결 실습 2회
4.2 충돌 #2 - 비자명 충돌 (파일 이름 변경 vs. 파일 내용 수정) - 송근영 & 민병우 페어
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout main && git pull origin main && git checkout -b feature/bwmin-update-math
M       src/count_utils.py
이미 'main'에 있습니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (3/3), 1.26 KiB | 643.00 KiB/s, 완료.
https://github.com/codi-modi/codyssey2026-B2-2 URL에서
 
branch            main       -> FETCH_HEAD
 7901bf2..26d6f69  main       -> origin/main
업데이트 중 7901bf2..26d6f69
Fast-forward
 src/math_utils.py | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)
 create mode 100644 src/math_utils.py
새로 만든 'feature/bwmin-update-math' 브랜치로 전환합니다
bwmin696907@c4r10s5 codyssey2026-B2-2 % 
 
민병우 님 브랜치
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.



마리너_송근영 — 어제 오후 4:05
PS C:\Codyssey26\codyssey2026-B2-2> git checkout main
Switched to branch 'main'
Your branch is behind 'origin/main' by 4 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
PS C:\Codyssey26\codyssey2026-B2-2>  git pull origin main
remote: Enumerating objects: 26, done.
remote: Counting objects: 100% (26/26), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 19 (delta 8), reused 10 (delta 3), pack-reused 0 (from 0)
Unpacking objects: 100% (19/19), 5.72 KiB | 48.00 KiB/s, done.
From https://github.com/codi-modi/codyssey2026-B2-2
branch            main       -> FETCH_HEAD
9e1f2cb..26d6f69  main       -> origin/main
Updating d7aabbe..26d6f69
Fast-forward
 docs/.github/CODEOWNERS               |   7 ++
 docs/.github/pull_request.template.md |  23 +++++++
 docs/CONTRIBUTING.md                  | 126 ++++++++++++++++++++++++++++++++++
 src/count_utils.py                    |  22 ++++++
 src/math_utils.py                     |  25 +++++++
 src/string_utils.py                   |  30 ++++++++
 src/test.py                           |   0
 7 files changed, 233 insertions(+)
 create mode 100644 docs/.github/CODEOWNERS
 create mode 100644 docs/.github/pull_request.template.md
 create mode 100644 docs/CONTRIBUTING.md
 create mode 100644 src/count_utils.py
 create mode 100644 src/math_utils.py
 create mode 100644 src/string_utils.py
 create mode 100644 src/test.py


송근영 님 브랜치
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.

PS C:\Codyssey26\codyssey2026-B2-2> git checkout -b
>> feature/kysong-rename-math
error: switch `b' requires a value
feature/kysong-rename-math : 'feature/kysong-rename-math' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행
할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포함된 경우 경로가 올
바른지 검증한 다음 다시 시도하십시오.
위치 줄:2 문자:1
+ feature/kysong-rename-math
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (feature/kysong-rename-math:String) [], CommandNotFound
   Exception
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Codyssey26\codyssey2026-B2-2> git checkout -b feature/kysong-rename-math
Switched to a new branch 'feature/kysong-rename-math'
PS C:\Codyssey26\codyssey2026-B2-2>
DOCSTRING 변경 후 merge

이후 송근영 님 브랜치에 커밋:
PS C:\Codyssey26\codyssey2026-B2-2> git add -A
PS C:\Codyssey26\codyssey2026-B2-2> git status
On branch feature/kysong-rename-math
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    src/math_utils.py -> src/calculator_utils.py

PS C:\Codyssey26\codyssey2026-B2-2> git commit -m "refactor: rename math_utils.py to calculator_units.py for clarity"
[feature/kysong-rename-math 0adda57] refactor: rename math_utils.py to calculator_units.py for clarity 
 1 file changed, 1 insertion(+), 1 deletion(-)
 rename src/{math_utils.py => calculator_utils.py} (92%)
PS C:\Codyssey26\codyssey2026-B2-2> git push -u origin feature/kysong-rename-math
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 975 bytes | 325.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'feature/kysong-rename-math' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/kysong-rename-math
remote:
To https://github.com/codi-modi/codyssey2026-B2-2.git
[new branch]      feature/kysong-rename-math -> feature/kysong-rename-math
branch 'feature/kysong-rename-math' set up to track 'origin/feature/kysong-rename-math'.
PS C:\Codyssey26\codyssey2026-B2-2>
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.



GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.


마리너_송근영 — 어제 오후 4:16
CODEOWNERS 파일도 업데이트 진행

PS C:\Codyssey26\codyssey2026-B2-2> git add .
PS C:\Codyssey26\codyssey2026-B2-2> git status
On branch feature/kysong-rename-math
Your branch is up to date with 'origin/feature/kysong-rename-math'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   docs/.github/CODEOWNERS

PS C:\Codyssey26\codyssey2026-B2-2> git commit -m "refactor: change .github/CODEOWNERS file accordinglt to match the changed filename"
[feature/kysong-rename-math ce16370] refactor: change .github/CODEOWNERS file accordinglt to match the changed filename
 1 file changed, 1 insertion(+), 1 deletion(-)
PS C:\Codyssey26\codyssey2026-B2-2> git push -u origin feature/kysong-rename-math
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 595 bytes | 198.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/codi-modi/codyssey2026-B2-2.git
   0adda57..ce16370  feature/kysong-rename-math -> feature/kysong-rename-math
branch 'feature/kysong-rename-math' set up to track 'origin/feature/kysong-rename-math'.
PS C:\Codyssey26\codyssey2026-B2-2>
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.

마리너_송근영 — 어제 오후 4:23
PR 올리기 (1/2)

마리너_민병우 — 어제 오후 4:27
병우님의 1/2 승인

bwmin696907@c4r10s5 codyssey2026-B2-2 % git add .
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-update-math
커밋할 변경 사항:
  (use "git restore --staged <file>..." to unstage)
        수정함:        src/count_utils.py
        수정함:        src/math_utils.py

bwmin696907@c4r10s5 codyssey2026-B2-2 % git diff
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-update-math
커밋할 변경 사항:
  (use "git restore --staged <file>..." to unstage)
        수정함:        src/count_utils.py
        수정함:        src/math_utils.py

bwmin696907@c4r10s5 codyssey2026-B2-2 % git commit -m "feat: add calculate_median function to math_utils"
[feature/bwmin-update-math 8c554a7] feat: add calculate_median function to math_utils
 2 files changed, 19 insertions(+), 1 deletion(-)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git push -u origin feature/bwmin-update-math
오브젝트 나열하는 중: 22, 완료.
오브젝트 개수 세는 중: 100% (22/22), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (12/12), 완료.
오브젝트 쓰는 중: 100% (12/12), 4.25 KiB | 4.25 MiB/s, 완료.
Total 12 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
remote: 
remote: Create a pull request for 'feature/bwmin-update-math' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/bwmin-update-math
remote: 
To https://github.com/codi-modi/codyssey2026-B2-2.git
[new branch]      feature/bwmin-update-math -> feature/bwmin-update-math
branch 'feature/bwmin-update-math' set up to track 'origin/feature/bwmin-update-math'.
bwmin696907@c4r10s5 codyssey2026-B2-2 % 

병우님 브랜치에서 작업 후 커밋 상황
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.



GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.


마리너_민병우 — 어제 오후 4:42

bwmin696907@c4r10s5 codyssey2026-B2-2 % git commit -m "feat: add calculate_median function to math_utils"
[feature/bwmin-update-math 8c554a7] feat: add calculate_median function to math_utils
 2 files changed, 19 insertions(+), 1 deletion(-)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git push -u origin feature/bwmin-update-math
오브젝트 나열하는 중: 22, 완료.
오브젝트 개수 세는 중: 100% (22/22), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (12/12), 완료.
오브젝트 쓰는 중: 100% (12/12), 4.25 KiB | 4.25 MiB/s, 완료.
Total 12 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
remote: 
remote: Create a pull request for 'feature/bwmin-update-math' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/bwmin-update-math
remote: 
To https://github.com/codi-modi/codyssey2026-B2-2.git
[new branch]      feature/bwmin-update-math -> feature/bwmin-update-math
branch 'feature/bwmin-update-math' set up to track 'origin/feature/bwmin-update-math'.
bwmin696907@c4r10s5 codyssey2026-B2-2 % git fetch origin
remote: Enumerating objects: 25, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 14 (delta 5), reused 13 (delta 5), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (14/14), 2.87 KiB | 293.00 KiB/s, 완료.
https://github.com/codi-modi/codyssey2026-B2-2 URL에서
   f00289b..6e7ee24  feature/djkim-list-utils   -> origin/feature/djkim-list-utils
 
[새로운 브랜치]   feature/kysong-rename-math -> origin/feature/kysong-rename-math
 26d6f69..6a5499e  main                       -> origin/main
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.



GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
bwmin696907@c4r10s5 codyssey2026-B2-2 % git merge origin/main
자동 병합: src/calculator_utils.py
Merge made by the 'ort' strategy.
 docs/.github/CODEOWNERS                    | 2 +-
 src/{math_utils.py => calculator_utils.py} | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
 rename src/{math_utils.py => calculator_utils.py} (95%)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-update-math
브랜치가 'origin/feature/bwmin-update-math'보다 4개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

어설프게 하는 경우:  Git이 'ort' 전략(파일 명 및 변경 내용을 자동으로 추적해서 병합해줌)을 사용해서 자동 병합 실패도 띄우기 힘듬

bwmin696907@c4r10s5 codyssey2026-B2-2 % git add .
bwmin696907@c4r10s5 codyssey2026-B2-2 % git commit -m "test: 충돌 일으켜 보기"
[feature/bwmin-update-math a13faf7] test: 충돌 일으켜 보기
 1 file changed, 1 insertion(+), 1 deletion(-)
 rename src/{calculator_utils.py => math_utils.py} (95%)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git merge main
이미 업데이트 상태입니다.
bwmin696907@c4r10s5 codyssey2026-B2-2 % git switch
fatal: missing branch or commit argument
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-update-math
브랜치가 'origin/feature/bwmin-update-math'보다 5개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'보다 3개 커밋 뒤에 있고, 앞으로 돌릴 수 있습니다.
  (로컬 브랜치를 업데이트하려면 "git pull"을 사용하십시오)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git add .
bwmin696907@c4r10s5 codyssey2026-B2-2 % git commit -m "test: 충돌을 위한 main에서의 파일 변경"
[main a12aeb7] test: 충돌을 위한 main에서의 파일 변경
 1 file changed, 1 insertion(+), 1 deletion(-)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout bwmin-update-math
error: pathspec 'bwmin-update-math' did not match any file(s) known to git
bwmin696907@c4r10s5 codyssey2026-B2-2 % git branch
  feature/bwmin-count-utils
  feature/bwmin-stash-practice
  feature/bwmin-update-math
main
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout feature/bwmin-update-math
'feature/bwmin-update-math' 브랜치로 전환합니다
브랜치가 'origin/feature/bwmin-update-math'보다 5개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git merge main
자동 병합: src/math_utils.py
충돌 (내용): src/math_utils.py에 병합 충돌
자동 병합이 실패했습니다. 충돌을 바로잡고 결과물을 커밋하십시오.
bwmin696907@c4r10s5 codyssey2026-B2-2 %
[로컬에서 충돌이 성공한 케이스]
마리너_민병우 — 어제 오후 4:50
git status를 활용한 미병합 내용 확인

병합하지 않은 경로가 있습니다.
  (충돌을 바로잡고 "git commit"을 실행하십시오)
  (병합을 중단하려면 "git merge --abort"를 사용하십시오)

병합하지 않은 경로:
  (해결했다고 표시하려면 "git add <파일>..."을 사용하십시오)
        양쪽에서 수정:  src/math_utils.py

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git add src/math_utils.py
bwmin696907@c4r10s5 codyssey2026-B2-2 % git commit -m "fix: resolve merge conflict from main"
[feature/bwmin-update-math 5afa470] fix: resolve merge conflict from main
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-update-math
브랜치가 'origin/feature/bwmin-update-math'보다 7개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
bwmin696907@c4r10s5 codyssey2026-B2-2 % git push origin feature/bwmin-update-math
오브젝트 나열하는 중: 25, 완료.
오브젝트 개수 세는 중: 100% (25/25), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (16/16), 완료.
오브젝트 쓰는 중: 100% (16/16), 1.97 KiB | 1.97 MiB/s, 완료.
Total 16 (delta 11), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (11/11), completed with 6 local objects.
To https://github.com/codi-modi/codyssey2026-B2-2.git
   8c554a7..5afa470  feature/bwmin-update-math -> feature/bwmin-update-math
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.

마리너_송근영 — 어제 오후 5:07

InKaManDa — 어제 오후 5:22
4.1 충돌 #1 - (인접 라인 동시 수정 충돌)  - 이진걸 & 김동조 페어
InKaManDa — 오전 10:12
README.md 를 다음과 같이 수정(이진걸)

jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git pull
Already up to date.
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git checkout main && git pull origin main && git checkout -b fea
ture/jglee-readme-intro
Already on 'main'
Your branch is up to date with 'origin/main'.
From https://github.com/codi-modi/codyssey2026-B2-2
branch            main       -> FETCH_HEAD
Already up to date.
Switched to a new branch 'feature/jglee-readme-intro'
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git add .
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git status
On branch feature/jglee-readme-intro
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git commit -m "docs: add team overview header to README"
[feature/jglee-readme-intro 2089649] docs: add team overview header to README
 1 file changed, 2 insertions(+), 1 deletion(-)
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git push -u origin feature/jglee-readme-intro
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 15 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 467 bytes | 467.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'feature/jglee-readme-intro' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/jglee-readme-intro
remote: 
To https://github.com/codi-modi/codyssey2026-B2-2.git
[new branch]      feature/jglee-readme-intro -> feature/jglee-readme-intro
branch 'feature/jglee-readme-intro' set up to track 'origin/feature/jglee-readme-intro'.
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 %
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.



GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
InKaManDa — 오전 10:21
PR 요청

김동조 — 오전 11:20
<<<<<<< HEAD
    # Python Utility & Git Workflow Lab (Team B2-2)
실무 중심의 PR 코드 리뷰, 충돌 해결, 트러블슈팅을 체득하는 협업 레포지토리입니다.
=======
codyssey2026-B2-2: 실전 Git 협업 프로젝트
>4인 개발팀(이진걸, 송근영, 김동조, 민병우)의 Github Flow 및 Python 유틸리티 실습 저장소입니다.
>>>>>>> origin/main

김동조 — 오전 11:37
mpeg46551@c4r10s1 codyssey2026-B2-2 % git checkout -b feature/djkim-readme-intro
Switched to a new branch 'feature/djkim-readme-intro'
mpeg46551@c4r10s1 codyssey2026-B2-2 % git status
On branch feature/djkim-readme-intro
nothing to commit, working tree clean
mpeg46551@c4r10s1 codyssey2026-B2-2 % git reset --hard ee51120
HEAD is now at ee51120 Merge pull request #11 from codi-modi/feature/djkim-list-utils
mpeg46551@c4r10s1 codyssey2026-B2-2 % git add README.md
mpeg46551@c4r10s1 codyssey2026-B2-2 % git commit -m "docs: update README title with workflow lab description"
[feature/djkim-readme-intro 715bdc8] docs: update README title with workflow lab description
 Committer: 김동조 mpeg46551@c4r10s1.codyssey.kr
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 2 insertions(+), 1 deletion(-)
mpeg46551@c4r10s1 codyssey2026-B2-2 %  git push origin feature/djkim-readme-intro
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 487 bytes | 487.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'feature/djkim-readme-intro' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/djkim-readme-intro
remote: 
To https://github.com/codi-modi/codyssey2026-B2-2
[new branch]      feature/djkim-readme-intro -> feature/djkim-readme-intro
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.



GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.

mpeg46551@c4r10s1 codyssey2026-B2-2 % git fetch origin
mpeg46551@c4r10s1 codyssey2026-B2-2 % git merge origin/main
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
mpeg46551@c4r10s1 codyssey2026-B2-2 % git add README.md
mpeg46551@c4r10s1 codyssey2026-B2-2 %    git commit -m "docs: resolve merge conflict in README intro by combining both descriptions"
[feature/djkim-readme-intro 1aef0a8] docs: resolve merge conflict in README intro by combining both descriptions
 Committer: 김동조 mpeg46551@c4r10s1.codyssey.kr
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

mpeg46551@c4r10s1 codyssey2026-B2-2 % git push origin feature/djkim-readme-intro
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 609 bytes | 609.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/codi-modi/codyssey2026-B2-2
   715bdc8..1aef0a8  feature/djkim-readme-intro -> feature/djkim-readme-intro
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.


