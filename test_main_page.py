from .pages.main_page import MainPage

main_link = "http://selenium1py.pythonanywhere.com/"

def test_quest_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_should_be_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()
    