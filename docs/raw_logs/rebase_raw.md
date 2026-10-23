jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git switch -c feature/jglee-rebase-practice
Switched to a new branch 'feature/jglee-rebase-practice'
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % mkdir -p docs/practice
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % echo "# Interactive Rebase Practice" > docs/practice/rebase-practice.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git add docs/practice/rebase-practice.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git commit -m "docs: add interactive rebase practice note"
[feature/jglee-rebase-practice 6ebf3dc] docs: add interactive rebase practice note
 1 file changed, 1 insertion(+)
 create mode 100644 docs/practice/rebase-practice.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % echo "개인 브랜치의 커밋 두 개를 하나로 정리한다." >> docs/practice/rebase-practice.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git add docs/practice/rebase-practice.md
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git commit -m "docs: explain rebase practice purpose"
[feature/jglee-rebase-practice 67f0552] docs: explain rebase practice purpose
 1 file changed, 1 insertion(+)
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git log -3 --oneline
67f0552 (HEAD -> feature/jglee-rebase-practice) docs: explain rebase practice purpose
6ebf3dc docs: add interactive rebase practice note
1a414fe (feature/jglee-submission-doc) chore: configure CODEOWNERS and update submission evidence
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git rebase -i HEAD~2
[detached HEAD 6c8a668] docs: document interactive rebase practice
 Date: Fri Oct 23 12:42:32 2026 +0900
 1 file changed, 2 insertions(+)
 create mode 100644 docs/practice/rebase-practice.md
Successfully rebased and updated refs/heads/feature/jglee-rebase-practice.
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git log -3 --oneline
6c8a668 (HEAD -> feature/jglee-rebase-practice) docs: document interactive rebase practice
1a414fe (feature/jglee-submission-doc) chore: configure CODEOWNERS and update submission evidence
a8afe68 (origin/main, origin/HEAD, main) Merge pull request #25 from codi-modi/feature/kysong-readme-guide
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % git status
On branch feature/jglee-rebase-practice
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        docs/screenshots/rebase_before.png
        docs/screenshots/rebase_during.png
        docs/screenshots/rebase_during2.png
        docs/screenshots/rebase_duringcommit1.png
        docs/screenshots/rebase_duringcommit2.png

nothing added to commit but untracked files present (use "git add" to track)
jingeollee@Jingeolui-MacBookPro codyssey2026-B2-2 % 