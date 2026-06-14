"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
import os
import pytest
from conftest import enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter, login, SCREENSHOT_DIR


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → find an "Available" book → click "Mượn sách này" → confirm dialog
        → verify book status changes to "Borrowed".
        (*Đăng nhập → tìm sách "Có sẵn" → click "Mượn sách này" → xác nhận dialog
        → kiểm tra sách chuyển sang trạng thái "Đang mượn".*)

    Suggested steps (*Gợi ý các bước*):
        1. login(page, test_config)
        2. Find available book: page.locator('flt-semantics[role="group"][aria-label*="Có sẵn"]')
           (*Tìm sách Có sẵn*)
        3. Click "Mượn sách này" button inside that book card
           (*Click nút "Mượn sách này" trong sách đó*)
        4. Wait for confirmation dialog, re-enable semantics
           (*Đợi dialog xác nhận, bật lại semantics*)
        5. Click "Mượn" button (confirm button in dialog)
           (*Click nút "Mượn" — nút xác nhận trong dialog*)
        6. Assert: "Đang mượn" or "thành công" appears
           (*Assert: "Đang mượn" hoặc "thành công" xuất hiện*)
    """
    
    # [R] Reachability
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
   
    flutter_fill(page, "Email", "dam.tran@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection
    book_card = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK001"]').last
    book_card.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').last.click()

    wait_for_flutter(page, text = "Xác nhận mượn sách")
    enable_flutter_semantics(page)
    flutter_click_button(page, "Mượn")
    
    # [P] Propagation
    wait_for_flutter(page, text="Mượn sách thành công!")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_book.png"))
    
    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    book = page.locator("flt-semantics", has_text="Mã: BOOK001").last
    book_text = " ".join(book.all_text_contents()).lower()
    
    success_keywords = ["đang mượn", "thành công", "borrowed", "success", "successfully"]
    has_success_signal = any(kw in book_text or kw in sem_text for kw in success_keywords)

    assert has_success_signal, "FAIL: Borrow action did not complete successfully."


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    
    # [R] Reachability
    login(page, test_config)
    
    # [I] Infection
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    enable_flutter_semantics(page)
    
    # [P] Propagation
    wait_for_flutter(page, text="Trả sách")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrowed_books.png"))
    
    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đang mượn" in sem_text or "Trả sách" in sem_text, "FAIL: No borrowed books are shown in \"Mượn / Trả\" tab."    


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    
    # [R] Reachability
    login(page, test_config)
    
    # [I] Infection
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Trả sách")
    
    record = page.locator('flt-semantics[role="group"][aria-label*="Mã phiếu: BR001"]')
    record.locator('flt-semantics[role="button"]:has-text("Trả sách")').click()
    
    # [P] Propagation
    wait_for_flutter(page, text="Trả sách thành công.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "return_book.png"))
    
    # [R✓] Revealability
    book = page.locator("flt-semantics", has_text="Mã phiếu: BR001").last
    book_text = " ".join(book.all_text_contents())

    assert "Đã trả" in book_text, "FAIL: Book was not returned successfully."


def test_overdue_check(page, test_config):
    """TC-13: Librarian check overdue books"""
    
    # [R] Reachability
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    # [I] Infection
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()
    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Tất cả phiếu mượn")

    page.locator('flt-semantics[role="button"]:has-text("Kiểm tra sách quá hạn")').click()
    
    # [P] Propagation
    wait_for_flutter(page, text="Đã cập nhật:")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "overdue_check.png"))
    
    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đã cập nhật:" in sem_text, "FAIL: Overdue books are not displayed correctly."


def test_borrow_expired(page, test_config):
    """TC-14: Expired member can't borrow a book"""

    # [R] Reachability
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)

    flutter_fill(page, "Email", "binh.pham@email.com")
    flutter_fill(page, "Mật khẩu", "password123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection
    book_card = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK001"]').last
    book_card.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').last.click()

    enable_flutter_semantics(page)
    wait_for_flutter(page, text="Xác nhận mượn sách")
    flutter_click_button(page, "Mượn")

    # [P] Propagation
    wait_for_flutter(page, text="Không thể mượn sách.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_expired.png"))

    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    updated_book = page.locator("flt-semantics", has_text="Mã: BOOK001").last
    book_text = " ".join(updated_book.all_text_contents()).lower()

    has_correct_reason = any(kw in sem_text for kw in ["hết hạn", "expired"])
    assert has_correct_reason, "FAIL: Error message display wrong."

    is_borrowed = "đang mượn" in book_text or "borrowed" in book_text
    assert not is_borrowed, "FAIL: Expired member successfully borrowed a book — should be rejected."


@pytest.mark.xfail(reason="BUG: Incorrect rejection reason: suspended member labeled as expired. — violates REQ-04")

def test_borrow_sus(page, test_config):
    """TC-15: Suspended member can't borrow a book"""

    # [R] Reachability
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    flutter_fill(page, "Email", "cu.le@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")

    # [I] Infection
    book_card = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK001"]').last
    book_card.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').last.click()

    enable_flutter_semantics(page)
    wait_for_flutter(page, text = "Xác nhận mượn sách")
    flutter_click_button(page, "Mượn")
    
    # [P] Propagation
    wait_for_flutter(page, text="Không thể mượn sách.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_sus.png"))
    
    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    updated_book = page.locator("flt-semantics", has_text="Mã: BOOK001").last
    book_text = " ".join(updated_book.all_text_contents()).lower()
    
    has_correct_reason = any(kw in sem_text for kw in ["tạm ngưng", "suspended"])
    assert has_correct_reason, f"FAIL: Error message display wrong."

    is_borrowed = "đang mượn" in book_text or "borrowed" in book_text
    assert not is_borrowed, f"FAIL: Suspended member successfully borrowed the book — should be rejected."
