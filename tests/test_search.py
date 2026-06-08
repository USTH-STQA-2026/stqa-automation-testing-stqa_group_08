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
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter,
)


@pytest.mark.parametrize(
    "case_id, keyword",
    [
        ("01", "Flutter"),
        ("02", "flutter"),
        ("03", "FLUTTER"),
        ("04", "fLuTtEr"),
    ]
)
def test_search_book_by_name(page, test_config, keyword, case_id):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    # [I] Infection
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        keyword
    )

    # [P] Propagation
    wait_for_flutter(page)

    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            f"tc04_search_name_{case_id}.png"
        )
    )

    # [R✓] Revealability
    result = page.locator(
        'flt-semantics[aria-label*="Flutter"]'
    )

    assert result.count() > 0, \
        f"Search should be case-insensitive for '{keyword}'"
    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    
    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    # [I] Infection
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        "xyz_khong_ton_tai_12345"
    )

    # [P] Propagation
    wait_for_flutter(page)

    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "tc05_search_book_no_result.png"
        )
    )

    # [R✓] Revealability
    result = page.locator(
        'flt-semantics[aria-label*="xyz_khong_ton_tai_12345"]'
    )

    assert result.count() == 0, \
        "Shows results though keyword does not exist"
    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


@pytest.mark.parametrize(
    "case_id, category",
    [
        ("01", "Công nghệ"),
        ("02", "công nghệ"),
        ("03", "CÔNG NGHỆ"),
        ("04", "cÔnG NgHệ"),
    ]
)

def test_filter_by_category(page, test_config, category, case_id):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

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
    # TODO: Students implement here (Sinh viên viết code ở đây)
    
    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    # [I] Infection
    flutter_fill(
        page,
        "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)",
        category
    )

    # [P] Propagation
    wait_for_flutter(page)

    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            f"tc06_filter_category_{case_id}.png"
        )
    )

    # [R✓] Revealability
    books = page.locator(
        'flt-semantics[role="group"][aria-label*="Mã: BOOK"]'
    )

    assert books.count() > 0, \
        f"No books found for category '{category}'"

    
    for i in range(books.count()):

        book = books.nth(i)

        aria_label = book.get_attribute("aria-label")

        assert aria_label is not None, \
            f"Book #{i + 1} does not have an aria-label"

        assert "Công nghệ" in aria_label, \
            f"Book #{i + 1} is not in category 'Công nghệ': {aria_label}"
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


@pytest.mark.parametrize(
    "case_id, author",
    [
        ("01", "Nguyễn Minh Đức"),
        ("02", "nguyễn minh đức"),
        ("03", "NGUYỄN MINH ĐỨC"),
        ("04", "NgUyỄn MiNh ĐỨc"),
    ]
)

def test_search_by_author(page, test_config, author, case_id):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
        - Verify: page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    # [I] Infection
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        author
    )

    # [P] Propagation
    wait_for_flutter(page)

    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            f"tc07_search_author_{case_id}.png"
        )
    )

    # [R✓] Revealability
    result = page.locator(
        'flt-semantics[aria-label*="Nguyễn Minh Đức"]'
    )

    assert result.count() > 0, \
        f"No search result found for author '{author}'"
    #pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")
