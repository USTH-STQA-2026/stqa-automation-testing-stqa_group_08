# Automation Test Report

---

## 1. Group Information

| Field | Details |
|-------|---------|
| **Group** | Group 8 |
| **Class** | ICT |
| **Semester** | HK2 2025–2026 |
| **Report Date** | 15/06/2026 |
| **System Under Test** | https://stqa.rbc.vn — v1.0 |
| **Repository** | https://github.com/USTH-STQA-2026/stqa-automation-testing-stqa_group_08 |

---

## 2. Results Overview

| Metric | Value |
|--------|-------|
| Total Test Cases | 15 |
| Required (TC-01 → TC-12) | 12 |
| Bonus (TC-13 → TC-15) | 3 |
| Pass | 14 |
| Fail | 1 |
| **Pass Rate** | **93.33%** |

### Distribution by File

| File | TCs | Pass | Fail | Notes |
|------|-----|------|------|-------|
| `test_login.py` | 3 | 3 | 0 | Includes data-driven test |
| `test_search.py` | 4 | 4 | 0 | |
| `test_borrow_return.py` | 6 | 5 | 1 | Includes 3 new test case + 1 bug |
| `test_general.py` | 2 | 2 | 0 | |
| **Total** | **15** | **14** | **1** | |

---

## 3. Test Case Descriptions

### Group 1 — Login (`test_login.py`)

| TC | Function | Description | RIPR | Result |
|----|----------|-------------|------|--------|
| TC-01 | `test_login_success` | Login with valid email, password → AppBar displays name and logout button. | Navigate to login [R] → enter valid input [I] → wait for "Đăng xuất" [P] → assert username and logout button present [R✓] | PASS |
| TC-02 | `test_login_fail` _(param: wrong password)_ | Login with correct email, wrong password → stays on login page, displays "Mật khẩu không đúng." | Navigate to login [R] → enter wrong password [I] → page stays [P] → assert no logout + correct error message [R✓] | PASS |
| TC-03 | `test_login_fail` _(param: empty fields)_ | Login with both fields empty → stays on login page, displays "Vui lòng nhập email và mật khẩu." | Navigate to login [R] → click login with no input [I] → page stays [P] → assert no logout + correct error message [R✓] | PASS |

> **Bonus B2:** TC-02 and TC-03 are merged into one parametrized function — data-driven testing.

---

### Group 2 — Search & Filter (`test_search.py`)

| TC | Function | Description | RIPR | Result |
|----|----------|-------------|------|--------|
| TC-04 | `test_search_book_by_name` | Search keyword "Flutter" → books with "Flutter" in title appear in results. | Login [R] → type "Flutter" into search box [I] → wait for BOOK001 to appear [P] → assert matching `aria-label` count > 0 [R✓] | PASS |
| TC-05 | `test_search_book_no_result` | Non-existent keyword → "Không tìm thấy sách nào." appears, zero book cards shown. | Login [R] → type garbage keyword [I] → wait for empty-state message [P] → assert zero book cards [R✓] | PASS |
| TC-06 | `test_filter_by_category` | Filter by "Công nghệ" → every displayed card contains "Công nghệ" in `aria-label`. | Login [R] → type category [I] → wait for a known Công nghệ book to appear [P] → loop all cards and assert label [R✓] | PASS |
| TC-07 | `test_search_by_author` | Search author "Nguyễn Minh Đức" → books by that author appear in results. | Login [R] → type author name [I] → wait for a known title to appear [P] → assert matching `aria-label` count > 0 [R✓] | PASS |

---

### Group 3 — Borrow & Return (`test_borrow_return.py`)

| TC | Function | Description | RIPR | Result |
|----|----------|-------------|------|--------|
| TC-08 | `test_borrow_book` | Login as `dam.tran` → borrow BOOK001 (available) → confirm dialog → success message appears, book status changes to "Đang mượn". | Login as member [R] → click borrow + confirm dialog [I] → wait for "Mượn sách thành công!" [P] → assert success signal in page text [R✓] | PASS |
| TC-09 | `test_view_borrowed_books` | Login → "Mượn / Trả" tab → at least one active borrow record with "Trả sách" button is visible. | Login [R] → click tab [I] → wait for "Trả sách" button [P] → assert "Đang mượn" or "Trả sách" in semantics [R✓] | PASS |
| TC-10 | `test_return_book` | Login → "Mượn / Trả" tab → return BR001 → record status changes to "Đã trả". | Login [R] → locate BR001 and click return [I] → wait for "Trả sách thành công." [P] → assert "Đã trả" in record text [R✓] | PASS |
| TC-13 | `test_overdue_check` | Login as librarian → trigger "Kiểm tra sách quá hạn" → system updates overdue records and shows "Đã cập nhật:" confirmation. | Login as librarian [R] → click overdue-check button [I] → wait for confirmation message [P] → assert "Đã cập nhật:" in semantics [R✓] | PASS |
| TC-14 | `test_borrow_expired` | Login as `binh.pham` (expired) → attempt borrow → system rejects with "hết hạn" message, book stays available. | Login as expired member [R] → attempt borrow + confirm [I] → wait for rejection [P] → assert correct reason + book not borrowed [R✓] | PASS |
| TC-15 | `test_borrow_sus` _(xfail — BUG-03)_ | Login as `cu.le` (suspended) → attempt borrow → **expected** rejection: "tạm ngưng". <br> **Actual:** system shows "hết hạn" — wrong reason, violates REQ-04. | Same flow as TC-14 [R→P] → assert "tạm ngưng" in message [R✓] — **assertion fails** | FAIL |

---

### Group 4 — General (`test_general.py`)

| TC | Function | Description | RIPR | Result |
|----|----------|-------------|------|--------|
| TC-11 | `test_logout` | Login → click "Đăng xuất" → page returns to login screen (Email input or "Đăng nhập" button visible). | Login [R] → click logout [I] → wait for "Đăng nhập" [P] → assert login elements present [R✓] | PASS |
| TC-12 | `test_switch_language_to_english` | Login → click "EN" → UI switches to English (checks for "Sign out", "Borrow", "Library"). | Login [R] → click EN [I] → wait for "Sign out" button to confirm switch [P] → assert English keywords in semantics [R✓] | PASS |

---

## 4. Bug Found

| Bug ID | TC | Severity | Description | REQ Violated |
|--------|----|----------|-------------|--------------|
| BUG-01 | TC-15 | High | Suspended member (`cu.le`) is correctly rejected from borrowing, but the error message reads "Thành viên đã hết hạn" instead of "đang bị tạm ngưng" — the wrong rejection reason is shown. | REQ-04: _"Thông báo lỗi phải mô tả đúng lý do từ chối (tạm ngưng ≠ hết hạn)"_ |

> TC-15 is marked `@pytest.mark.xfail` to document the known bug without blocking the CI pipeline.

---

## 5. Techniques Applied

| Technique | Applied to | How |
|-----------|-----------|-----|
| **RIPR Model** | All 15 TCs | Each test is structured as Reachability → Infection → Propagation → Revealability with `[R]` / `[I]` / `[P]` / `[R✓]` comments. |
| **Data-Driven Testing** (`@pytest.mark.parametrize`) | TC-02, TC-03 | Two login failure scenarios (wrong password, empty fields) run through one parametrized function, reducing duplication. |
| **Strong Test Oracle** | TC-06, TC-10, TC-14, TC-15 | Assertions check specific `aria-label` content and exact message text, not just URL or element existence. |
| **Smart Wait** (`wait_for_flutter`) | All 15 TCs | Replaces `time.sleep()` — polls the Flutter Semantics Tree until the expected state appears, eliminating flaky timing failures. |

---

## 6. Conclusion

All 12 required test cases pass. The 3 bonus test cases (TC-13, TC-14, TC-15) cover additional scenarios from REQ-04: overdue checking, expired member rejection, and suspended member rejection.

One bug was found (BUG-01): suspended members receive the wrong rejection message, violating REQ-04. The borrow rejection itself works correctly — only the error message is inaccurate.
