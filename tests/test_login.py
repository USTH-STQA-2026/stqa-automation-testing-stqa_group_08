"""
Login Tests (*Kiểm thử Đăng nhập*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

📖 Textbook concepts in this file:
   - RIPR Model (Ch.2): See [R], [I], [P], [R✓] comments in TC-01
   - Data-Driven Testing / @parametrize (Ch.3 §3.3.2): See hint in TC-02/TC-03

This file contains 1 completed example (TC-01).
Students must complete TC-02 and TC-03.

(*File này chứa 1 ví dụ mẫu (TC-01) đã hoàn chỉnh.
Sinh viên cần hoàn thành TC-02 và TC-03.*)
"""
import os
import pytest
from conftest import enable_flutter_semantics, flutter_fill, flutter_click_button, wait_for_flutter, SCREENSHOT_DIR


def test_login_success(page, test_config):
    """TC-01: Login success with valid credentials (*Đăng nhập thành công với thông tin hợp lệ*)

    ✅ COMPLETED — Use as a reference example.
    (*ĐÃ HOÀN THÀNH — Dùng làm ví dụ tham khảo.*)

    📖 RIPR Model (Textbook Ch.2 — Reachability → Infection → Propagation → Revealability):
        Mỗi dòng code trong test tương ứng với 1 bước trong chuỗi RIPR.
        Xem comment [R], [I], [P], [R✓] bên dưới.
    """
    # [R] Reachability: Truy cập trang đăng nhập — chạm tới UI cần test
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000) 

    enable_flutter_semantics(page) 

    # [I] Infection: Nhập dữ liệu hợp lệ — kích hoạt logic đăng nhập trong hệ thống
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")

    # [P] Propagation: Chờ trạng thái lan truyền ra UI — nút "Đăng xuất" xuất hiện
    # (Smart Wait: thay vì time.sleep(5) — nhanh hơn và ổn định hơn)
    wait_for_flutter(page, text="Đăng xuất")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "login_success.png"))

    # [R✓] Revealability: Kiểm tra kết quả — Test Oracle phát hiện lỗi nếu có
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    has_user_name = test_config["display_name"] in sem_text
    has_logout = "Đăng xuất" in sem_text or "Logout" in sem_text
    assert has_user_name or has_logout, \
        f"Login failed: '{test_config['display_name']}' or Logout button not found " \
        f"(Đăng nhập không thành công: không tìm thấy tên hoặc nút Đăng xuất)"


def test_login_fail_wrong_password(page, test_config):
    """TC-02: Login fail – wrong password (*Đăng nhập thất bại – sai mật khẩu*)

    🔴 NOT COMPLETED — Students must implement this test case.
    (*CHƯA HOÀN THÀNH — Sinh viên cần viết code cho test case này.*)

    Description (*Mô tả*):
        Enter correct email but wrong password → system stays on login page
        or shows an error message.
        (*Nhập email đúng nhưng mật khẩu sai → hệ thống không chuyển trang,
        hoặc hiển thị thông báo lỗi.*)

    📖 RIPR — Áp dụng cho test case này:
        [R] page.goto(...) → Chạm tới trang đăng nhập
        [I] flutter_fill(..., "wrongpassword") → Nhiễm trạng thái lỗi
        [P] Hệ thống xử lý login → Lỗi lan truyền ra thông báo
        [R✓] assert ... → Test Oracle kiểm tra thông báo lỗi

    💡 Bonus B2 — Data-Driven Testing:
        TC-02 và TC-03 có cùng pattern (nhập → click → kiểm tra lỗi).
        Bạn có thể gộp bằng @pytest.mark.parametrize:

        @pytest.mark.parametrize("email, password, tc_id", [
            ("valid@email.com", "wrongpass", "TC-02"),
            ("", "", "TC-03"),
        ])
        def test_login_fail(page, test_config, email, password, tc_id):
            ...

        Xem thêm: docs/textbook-concepts.md §3 (Data-Driven Testing)

    Suggested steps (*Gợi ý các bước*):
        1. Navigate to login page (*Truy cập trang đăng nhập*)
        2. Enable Flutter semantics (*Bật Flutter semantics*)
        3. Enter correct Email (from test_config["email"]) (*Nhập Email đúng*)
        4. Enter wrong Password (e.g. "wrongpassword") (*Nhập Mật khẩu sai*)
        5. Click "Đăng nhập" (*Click "Đăng nhập"*)
        6. Assert: URL still on login page OR error message shown
           (*Assert: URL vẫn ở trang đăng nhập HOẶC có thông báo lỗi*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability: Truy cập trang đăng nhập — chạm tới UI cần test
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    
    enable_flutter_semantics(page)

    # [I] Infection: Nhập email hợp lệ nhưng mật khẩu sai - kích hoạt trạng thái lỗi
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", "wrongpassword")
    flutter_click_button(page, "Đăng nhập")
        
    # [P] Propagation: Hệ thống xử lý - lỗi lan truyền ra thông báo
    wait_for_flutter(page, text="Mật khẩu không đúng")
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "login_fail_wrong_password.png"))
    
    # [R✓] Revealability: assert ... - Test Oracle kiểm tra thông báo lỗi
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    has_login = "Đăng xuất" in sem_text or "Logout" in sem_text
    
    error_keywords = ["Mật khẩu không đúng", "Password is incorrect", "incorrect", "không đúng"]
    has_error_message = any(kw in sem_text for kw in error_keywords)

    assert not has_login, \
        "TC-02 FAIL: Hệ thống cho phép đăng nhập với mật khẩu sai — lỗ hổng bảo mật!"
    assert has_error_message, \
        f"TC-02 FAIL: Không thấy thông báo 'Mật khẩu không đúng'." \
        f"sem_text snapshot: {sem_text[:300]}"
    

def test_login_fail_empty_fields(page, test_config):
    """TC-03: Login fail – empty fields (*Đăng nhập thất bại – để trống các trường*)

    🔴 NOT COMPLETED — Students must implement this test case.
    (*CHƯA HOÀN THÀNH — Sinh viên cần viết code cho test case này.*)

    Description (*Mô tả*):
        Leave all fields empty, click Login → system stays on login page.
        (*Không nhập gì, bấm Đăng nhập → hệ thống không chuyển trang.*)

    Suggested steps (*Gợi ý các bước*):
        1. Navigate to login page (*Truy cập trang đăng nhập*)
        2. Enable Flutter semantics (*Bật Flutter semantics*)
        3. Do NOT enter Email/Password — click "Đăng nhập" immediately
           (*KHÔNG nhập Email/Mật khẩu — click "Đăng nhập" ngay*)
        4. Assert: URL still on login page (*Assert: URL vẫn ở trang đăng nhập*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)

    # [R] Reachability: Truy cập trang đăng nhập — chạm tới UI cần test
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    
    # [I] Infection: Không nhập gì — click thẳng "Đăng nhập" ngay lập tức
    flutter_click_button(page, "Đăng nhập")

    # [P] Propagation: Hệ thống xử lý login → Trạng thái không đăng nhập lan truyền ra UI (vẫn ở trang login)
    wait_for_flutter(page, text="Đăng nhập")
    enable_flutter_semantics(page)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "login_fail_empty_fields.png"))

    # [R✓] Revealability: assert ... → Test Oracle kiểm tra hệ thống không cho phép đăng nhập và có thông báo yêu cầu nhập thông tin
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    error_keywords = ["Vui lòng nhập email và mật khẩu", "Please enter email and password", "Vui lòng nhập", "enter email"]
    has_error_message = any(kw.lower() in sem_text.lower() for kw in error_keywords)

    has_login = "Đăng xuất" in sem_text or "Logout" in sem_text

    assert not has_login, \
        "TC-03 FAIL: Hệ thống cho phép đăng nhập khi bỏ trống Email và Mật khẩu — lỗ hổng nghiêm trọng!"
    assert has_error_message, \
        f"TC-03 FAIL: Không thấy thông báo yêu cầu nhập thông tin đầy đủ.\n" \
        f"sem_text: \n{sem_text[:300]}"
    


@pytest.mark.parametrize(
    "input_email, input_password, expected_keywords, tc_id",
    [
        # TC-02: Email đúng + mật khẩu sai → SRS REQ-01: "Mật khẩu không đúng"
        ("USE_CONFIG_EMAIL", "wrongpassword", ["Mật khẩu không đúng", "Password is incorrect", "incorrect", "không đúng"], "TC-02"),
        
        # TC-03: Bỏ trống cả hai → SRS REQ-01: "Vui lòng nhập email và mật khẩu"
        ("", "", ["Vui lòng nhập email và mật khẩu", "Please enter email and password", "Vui lòng nhập", "enter email"], "TC-03"),
    ]
)

def test_login_fail_datadriven(page, test_config, input_email, input_password, expected_keywords, tc_id):
    """TC-02 & TC-03: Login fail (*Đăng nhập thất bại*) — Data-Driven Testing (Bonus B2)

    📖 RIPR Model:
        [R] page.goto(...) → Tiếp cận giao diện đăng nhập
        [I] flutter_fill(...) → Nạp dữ liệu không hợp lệ để làm nhiễm trạng thái
        [P] wait_for_flutter(...) → Trạng thái lỗi lan truyền ra giao diện UI
        [R✓] assert ... → Test Oracle bộc lộ và bắt lỗi

        Data sets:
        TC-02: email đúng + mật khẩu sai  → "Mật khẩu không đúng"
        TC-03: bỏ trống cả hai fields     → "Vui lòng nhập email và mật khẩu"
    """
   
    # [R] Reachability: Tiếp cận vùng cần kiểm thử
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)

    # [I] Infection: Logic xử lý dữ liệu đầu vào theo tham số dữ liệu
    final_email = test_config["email"] if input_email == "USE_CONFIG_EMAIL" else input_email
    
    if final_email:
        flutter_fill(page, "Email", final_email)
    if input_password:
        flutter_fill(page, "Mật khẩu", input_password)
    flutter_click_button(page, "Đăng nhập")

    # [P] Propagation: Chờ hệ thống thông báo trạng thái lỗi và chụp ảnh minh chứng
    wait_for_flutter(page, text="Đăng nhập")
    enable_flutter_semantics(page)
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"login_fail_{tc_id}.png"))

    # [R✓] Revealability: 
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    has_error_message = any(kw.lower() in sem_text.lower() for kw in expected_keywords)
    has_login = "Đăng xuất" in sem_text or "Logout" in sem_text
    assert not has_login, \
        f"{tc_id} FAIL: Hệ thống dính lỗ hổng bảo mật nghiêm trọng, cho phép login thành công!"

    assert has_error_message, \
        f"{tc_id} FAIL: Không tìm thấy thông báo lỗi phù hợp trên giao diện.\n" \
        f"sem_text:\n{sem_text[:300]}"