"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
import pytest
from conftest import flutter_fill, login, wait_for_flutter, SCREENSHOT_DIR


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """

    # [R] Reachability
    login(page, test_config)

    # [I] Infection
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")

    # [P] Propagation
    wait_for_flutter(page, text="BOOK001")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"search_book_by_name.png"))

    # [R✓] Revealability
    result = page.locator('flt-semantics[aria-label*="Flutter"]')

    assert result.count() > 0, \
        f"FAIL: No books are displayed."


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    
    # [R] Reachability
    login(page, test_config)

    # [I] Infection
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "xyz_khong_ton_tai_12345")

    # [P] Propagation
    wait_for_flutter(page, text="Không tìm thấy sách nào.")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "search_book_no_result.png"))

    # [R✓] Revealability
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    assert books.count() == 0, "FAIL: {books.count()} book card(s) still showing for non-existent keyword."


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (*Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
        - Get book list: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
          (*Lấy danh sách sách*)
        - Loop through each book, verify aria-label contains "Công nghệ"
          (*Lặp qua từng sách, kiểm tra aria-label chứa "Công nghệ"*)
    """
    
    # [R] Reachability
    login(page, test_config)

    # [I] Infection
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")

    # [P] Propagation
    wait_for_flutter(page, text="Kiểm thử phần mềm nhập môn")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"filter_by_category.png"))

    # [R✓] Revealability
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')

    assert books.count() > 0, \
        f"FAIL: No books are displayed."

    for i in range(books.count()):
        book = books.nth(i)
        aria_label = book.get_attribute("aria-label")

        assert aria_label is not None, \
            f"FAIL: Book #{i + 1} does not have an aria-label"
        assert "Công nghệ" in aria_label, \
            f"FAIL: Book #{i + 1} is not in category 'Công nghệ': {aria_label}"


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    ✅ COMPLETED
    
    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
        - Verify: page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
    """

    # [R] Reachability
    login(page, test_config)

    # [I] Infection
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")

    # [P] Propagation
    wait_for_flutter(page, text="Nhập môn lập trình Python")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"search_by_author.png"))

    # [R✓] Revealability
    result = page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]')

    assert result.count() > 0, \
        f"FAIL: No books are displayed."
