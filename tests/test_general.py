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
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter,
)


def test_logout(page, test_config):
    """TC-11: Logout success (*Đăng xuất thành công*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

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
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability: Truy cập trang chủ — chạm tới UI cần test
    login(page, test_config) 

    # [I] Infection: Thực hiện hành động đăng xuất — kích hoạt logic logout trong hệ thống
    flutter_click_button(page, "Đăng xuất")

    # [P] Propagation: Chờ trạng thái lan truyền ra UI — trang đăng nhập xuất hiện
    wait_for_flutter(page, text="Đăng nhập")   
    enable_flutter_semantics(page)

    # [R✓] Revealability: Kiểm tra kết quả — Test Oracle phát hiện lỗi nếu có
    assert page.locator('flt-semantics[role="button"]:has-text("Đăng nhập")').is_visible(), "Logout failed: nút Đăng nhập không hiển thị"
    assert page.locator('input[aria-label="Email"]').is_visible(), "Logout failed: ô nhập Email không hiển thị"
    
    # Lưu screenshot minh chứng
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "logout_success.png"))



def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English (*Chuyển ngôn ngữ sang tiếng Anh*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

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
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability: Đăng nhập trang chủ — chạm tới UI cần test
    login(page, test_config)  

    # [I] Infection: Click nút "EN" — Giao diện chuyển sang tiếng Anh
    flutter_click_button(page, "EN") 

    # [P] Propagation: Chờ trạng thái lan truyền ra UI - hiển thị text "Logout"
    wait_for_flutter(page, text="Logout") # Chờ trang
    enable_flutter_semantics(page) #kích hoạt Senmantics để đọc text

    # [R✓] Revealability: Kiểm tra kết quả — Test Oracle phát hiện lỗi nếu có
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Logout" in sem_text, "Không thấy nút 'Log out' sau khi đổi ngôn ngữ"
    assert "Borrow" in sem_text, "Không thấy text 'Borrow' sau khi đổi ngôn ngữ"
    assert "Library" in sem_text, "Không thấy text 'Library' sau khi đổi ngôn ngữ"
    assert "Search" in sem_text, "Không thấy text 'Search' sau khi đổi ngôn ngữ"

    # Screenshot 
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "switch_language_en.png"))
