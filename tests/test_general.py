"""
Logout & Language Tests (*Kiểm thử Đăng xuất & Chuyển ngôn ngữ*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 2 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 2 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - Logout button: 'flt-semantics[role="button"]:has-text("Đăng xuất")'
      (*Nút Đăng xuất*)
    - Language switch EN button: 'flt-semantics[role="button"]:has-text("EN")'
      (*Nút chuyển ngôn ngữ EN*)
    - After logout: page returns to login (has "Đăng nhập" button and "Email" input)
      (*Sau đăng xuất: trang quay về login*)
    - After switching to EN: text "Logout", "Borrow", "Search", "Library" may appear
      (*Sau chuyển EN: text tiếng Anh có thể xuất hiện*)
"""
import os
from conftest import flutter_click_button, login, wait_for_flutter, SCREENSHOT_DIR


def test_logout(page, test_config):
    """TC-11: Logout success (*Đăng xuất thành công*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → click Logout → verify page returns to login screen.
        (*Đăng nhập → click Đăng xuất → kiểm tra quay về trang đăng nhập.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "Đăng xuất" button and click (*Tìm nút "Đăng xuất" và click*)
        3. Wait 3s, re-enable semantics (*Đợi 3s, bật lại semantics*)
        4. Assert: "Đăng nhập" button or Email input exists
           (*Assert: có nút "Đăng nhập" hoặc ô input Email*)
    """

    # [R] Reachability
    login(page, test_config) 

    # [I] Infection
    flutter_click_button(page, "Đăng xuất")

    # [P] Propagation
    wait_for_flutter(page, text="Đăng nhập")   
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "logout_success.png"))

    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_login_button = "Đăng nhập" in sem_text
    has_email_input = page.locator('input[aria-label="Email"]').count() > 0

    assert has_login_button or has_email_input, \
        "Logout failed: 'Đăng nhập' button or Email input not found after logout"


def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English (*Chuyển ngôn ngữ sang tiếng Anh*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → click "EN" button → verify UI switches to English.
        (*Đăng nhập → click nút "EN" → kiểm tra giao diện chuyển sang tiếng Anh.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "EN" button and click (*Tìm nút "EN" và click*)
        3. Wait 2s, re-enable semantics (*Đợi 2s, bật lại semantics*)
        4. Get sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
        5. Assert: "Logout" or "Borrow" or "Library" in sem_text
    """

    # [R] Reachability
    login(page, test_config)  

    # [I] Infection
    flutter_click_button(page, "EN") 

    # [P] Propagation
    wait_for_flutter(page, text="Sign out")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "switch_language_en.png"))

    # [R✓] Revealability
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_logout_en  = "Sign out" in sem_text
    has_borrow_en  = "Borrow" in sem_text
    has_library_en = "Library" in sem_text

    assert has_logout_en and has_borrow_en and has_library_en, \
        f"Language switch failed — missing English text in UI. " \
        f"Logout={has_logout_en}, Borrow={has_borrow_en}, Library={has_library_en} "
