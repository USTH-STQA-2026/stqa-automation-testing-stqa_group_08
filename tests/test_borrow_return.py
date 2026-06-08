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
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter,
    login, SCREENSHOT_DIR,
)


def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

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
    # TODO: Students implement here (Sinh viên viết code ở đây)
    
    #[R]
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
   
    #[I]
    flutter_fill(page, "Email", "dam.tran@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK001"]').locator('flt-semantics[role="button"]:has-text("Mượn sách này")').click()  # Click "Mượn sách này" button of the first available book
    wait_for_flutter(page, text = "Xác nhận mượn sách")  # Wait for the confirmation dialog to appear
    enable_flutter_semantics(page)  # Re-enable semantics after dialog appears
    flutter_click_button(page, "Mượn")
    
    #[P]
    wait_for_flutter(page, text="Mượn sách thành công!")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_book.png"))  # Debug screenshot
    
    #[R✓]
    book = page.locator("flt-semantics", has_text="Mã: BOOK001").last
    assert "Đang mượn" in book.text_content(), "Book was not borrowed successfully"

    


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    
    #[R]
    login(page, test_config)
    
    #[I]
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()  # Switch to "Mượn / Trả" tab
    
    #[P]
    wait_for_flutter(page, text="Trả sách")  # Wait for "Trả sách" button to appear
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrowed_books.png"))  # Debug screenshot
    
    
    #[R✓]
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đang mượn" in sem_text or "Trả sách" in sem_text, "No borrowed books are shown in Mượn / Trả tab"    


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

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
    # TODO: Students implement here (Sinh viên viết code ở đây)
    
    #[R]
    login(page, test_config)
    
    #[I]
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()  # Switch to "Mượn / Trả" tab
    wait_for_flutter(page, text="Trả sách")  # Wait for "Trả sách" button to appear
    page.locator('flt-semantics[role="group"][aria-label*="Mã phiếu: BR001"]').locator('flt-semantics[role="button"]:has-text("Trả sách")').click()  # Click the first "Trả sách" button
    
    #[P]
    wait_for_flutter(page, text="Trả sách thành công.")  # Wait for the book to become available again
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "return_book.png"))  # Debug screenshot
    
    #[R✓]
    book = page.locator("flt-semantics", has_text="Mã phiếu: BR001").last
    assert "Đã trả" in book.text_content(), "Book was not returned successfully"

def test_borrow_sus(page, test_config):
    
    #[R]
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    #[I]
    flutter_fill(page, "Email", "cu.le@email.com")
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK001"]').locator('flt-semantics[role="button"]:has-text("Mượn sách này")').click()
    wait_for_flutter(page, text = "Xác nhận mượn sách")
    enable_flutter_semantics(page)  # Re-enable semantics after dialog appears
    flutter_click_button(page, "Mượn")
    
    #[P]
    wait_for_flutter(page, text="Thành viên đã hết hạn. Không thể mượn sách.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "borrow_sus.png"))  # Debug screenshot
    
    #[R✓]
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    book = page.locator("flt-semantics[role='group'][aria-label*='Mã: BOOK001']")
    assert "Thành viên đã hết hạn" in sem_text, "Error message does not appear correctly"
    assert "Đang mượn" in book.text_content(), "Suspended member borrowed book sucessfully"

def test_overdue_check(page, test_config):
    
    #[R]
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    #[I]
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]').click()  # Switch to "Mượn / Trả" tab
    wait_for_flutter(page, text="Tất cả phiếu mượn")
    page.locator('flt-semantics[role="button"]:has-text("Kiểm tra sách quá hạn")').click()  # Click the first "Kiểm tra sách quá hạn" button
    
    #[P]
    wait_for_flutter(page, text="Đã cập nhật:")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "overdue_check.png"))  # Debug screenshot
    
    #[R✓]
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đã cập nhật:" in sem_text, "Overdue books are not displayed correctly"