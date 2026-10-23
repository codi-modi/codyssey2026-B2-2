Git 트러블슈팅 4종 실습 - 완성 후 docs/trogleshooting-log.md에 저장 예정
시나리오 A - 이진걸: git commit --amend (최근 커밋 메시지 수정)
 
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git checkout -b feature/jglee-amend-practice
Switched to a new branch 'feature/jglee-amend-practice'
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % echo "" >> README.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git add README.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git status
On branch feature/jglee-amend-practice
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git commit -m "docs: updte readme title(typo)"
[feature/jglee-amend-practice 7bb7583] docs: updte readme title(typo)
 1 file changed, 1 insertion(+)
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git log -l --oneline
error: switch `l' expects an integer value with an optional k/m/g suffix
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git log -1 --oneline
7bb7583 (HEAD -> feature/jglee-amend-practice) docs: updte readme title(typo)
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git commit --amend -m "docs: clarify project title and overview 
in README.md"
[feature/jglee-amend-practice 26328d5] docs: clarify project title and overview in README.md
 Date: Thu Oct 22 14:00:55 2026 +0900
 1 file changed, 1 insertion(+)
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 %
이미지
이미지
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git log -5 --oneline
26328d5 (HEAD -> feature/jglee-amend-practice) docs: clarify project title and overview in README.md
7901bf2 (origin/main, origin/HEAD, main) Merge pull request #9 from codi-modi/feature/bwmin-count-utils
00ac08b (origin/feature/bwmin-count-utils) fix: strip punctuation before counting words in count_utils
7f07ac4 Merge pull request #8 from codi-modi/feature/jglee-string-utils
7c9bc42 (origin/feature/jglee-string-utils, feature/jglee-string-utils) refactor(string_utils): to_snake_case 빈 문
자열 처리 및 구분자 중복 방지 개선
마리너_민병우 — 어제 오후 2:13
시나리오 D - 민병우: git stash / git stash pop (작업 임시 보관 후 브랜치 전환
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 사항 없음, 작업 폴더 깨끗함
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout -b feature/bwmin-stash-practice
새로 만든 'feature/bwmin-stash-practice' 브랜치로 전환합니다
bwmin696907@c4r10s5 codyssey2026-B2-2 % echo "# 작업 중인 함수의 초안" >> src/count_utils.py
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-stash-practice
커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
        수정함:        src/count_utils.py

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
이미지
bwmin696907@c4r10s5 codyssey2026-B2-2 % git stash push -m "wip: drafting character frequency helper"
Saved working directory and index state On feature/bwmin-stash-practice: wip: drafting character frequency helper
bwmin696907@c4r10s5 codyssey2026-B2-2 % git stash list
stash@{0}: On feature/bwmin-stash-practice: wip: drafting character frequency helper
bwmin696907@c4r10s5 codyssey2026-B2-2 % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
bwmin696907@c4r10s5 codyssey2026-B2-2 % git pull origin main
https://github.com/codi-modi/codyssey2026-B2-2 URL에서
 
branch            main       -> FETCH_HEAD
이미 업데이트 상태입니다.
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
이미지
bwmin696907@c4r10s5 codyssey2026-B2-2 % git stash pop
현재 브랜치 feature/bwmin-stash-practice
커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
        수정함:        src/count_utils.py

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
Dropped refs/stash@{0} (c168328f6b9b2da90dffbd7b94d2987efab737b6)
bwmin696907@c4r10s5 codyssey2026-B2-2 % git status
현재 브랜치 feature/bwmin-stash-practice
커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
        수정함:        src/count_utils.py

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
마리너_송근영 — 어제 오후 2:18
시나리오 B - 송근영: git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지)
PS C:\Codyssey26\codyssey2026-B2-2> git checkout -b feature/kysong-reset-practice
Switched to a new branch 'feature/kysong-reset-practice'
PS C:\Codyssey26\codyssey2026-B2-2> echo "# TODO: add median function" >> src/math_utils.py
PS C:\Codyssey26\codyssey2026-B2-2> git add src/math_utils.py
PS C:\Codyssey26\codyssey2026-B2-2> git commit -m "feat: add incomplete median note"
[feature/kysong-reset-practice 64409e0] feat: add incomplete median note
 1 file changed, 2 insertions(+), 1 deletion(-)
PS C:\Codyssey26\codyssey2026-B2-2> git reset --soft HEAD~1
PS C:\Codyssey26\codyssey2026-B2-2> git status
On branch feature/kysong-reset-practice
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   src/math_utils.py
이미지
# kysong reset practice log

## 브랜치

`feature/kysong-reset-practice`

## reflog 확인 결과

```text
0a1bf3c feature/kysong-reset-practice@{2026-10-22 15:56:27 +0900}: commit: Update math utils average handling
64a24bd feature/kysong-reset-practice@{2026-10-22 14:08:55 +0900}: reset: moving to HEAD~1
64409e0 feature/kysong-reset-practice@{2026-10-22 14:08:42 +0900}: commit: feat: add incomplete median note
64a24bd feature/kysong-reset-practice@{2026-10-22 14:06:27 +0900}: branch: Created from HEAD


리셋 지점: 64a24bd feature/kysong-reset-practice@{2026-10-22 14:08:55 +0900}: reset: moving to HEAD~1

리셋 전 커밋: 64409e0 feat: add incomplete median note

변경 내용:
src/math_utils.py | 3 ++-
1 file changed, 2 insertions(+), 1 deletion(-)

reset 후 이동 커밋: 
64a24bd feat: support optional rounding precision in calculate_average
```
InKaManDa — 어제 오후 5:23
시나리오 C - 김동조 : git revert(원격에 push된 커밋 안전하게 취소)
김동조 — 오전 10:37
mpeg46551@c4r10s1 codyssey2026-B2-2 % git checkout -b feature/djkim-revert-practice
Switched to a new branch 'feature/djkim-revert-practice'
mpeg46551@c4r10s1 codyssey2026-B2-2 % echo "# 잘못 추가 된 임시 설정" >> src/list_utils.py
mpeg46551@c4r10s1 codyssey2026-B2-2 % git add src/list_utils.py
mpeg46551@c4r10s1 codyssey2026-B2-2 % git commit -m "chore: add temporary debug header to list_utils"
[feature/djkim-revert-practice 4f380a2] chore: add temporary debug header to list_utils
 Committer: 김동조 mpeg46551@c4r10s1.codyssey.kr
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
mpeg46551@c4r10s1 codyssey2026-B2-2 % git push -u origin feature/djkim-revert-practice
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 6 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 420 bytes | 420.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: Create a pull request for 'feature/djkim-revert-practice' on GitHub by visiting:
remote:      https://github.com/codi-modi/codyssey2026-B2-2/pull/new/feature/djkim-revert-practice
remote: 
To https://github.com/codi-modi/codyssey2026-B2-2
[new branch]      feature/djkim-revert-practice -> feature/djkim-revert-practice
branch 'feature/djkim-revert-practice' set up to track 'origin/feature/djkim-revert-practice'.
GitHub
Build software better, together
GitHub is where people build software. More than 225 million people use GitHub to discover, fork, and contribute to over 800 million projects.
이미지
이미지
이미지
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
mpeg46551@c4r10s1 codyssey2026-B2-2 % git revert HEAD --no-edit
[feature/djkim-revert-practice 90216de] Revert "chore: add temporary debug header to list_utils"
 Date: Fri Oct 23 10:34:27 2026 +0900
 Committer: 김동조 mpeg46551@c4r10s1.codyssey.kr
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 deletion(-)
mpeg46551@c4r10s1 codyssey2026-B2-2 % git log -2 --oneline
90216de (HEAD -> feature/djkim-revert-practice) Revert "chore: add temporary debug header to list_utils"
4f380a2 (origin/feature/djkim-revert-practice) chore: add temporary debug header to list_utils
mpeg46551@c4r10s1 codyssey2026-B2-2 % git push origin feature/djkim-revert-practice
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 6 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 412 bytes | 412.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/codi-modi/codyssey2026-B2-2
   4f380a2..90216de  feature/djkim-revert-practice -> feature/djkim-revert-practice
mpeg46551@c4r10s1 codyssey2026-B2-2 % 
mpeg46551@c4r10s1 codyssey2026-B2-2 %
GitHub
GitHub - codi-modi/codyssey2026-B2-2: Git 협업을 위한 레포...
Git 협업을 위한 레포지토리. Contribute to codi-modi/codyssey2026-B2-2 development by creating an account on GitHub.
스샷