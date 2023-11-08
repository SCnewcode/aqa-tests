from selenium.webdriver.common.action_chains import ActionChains


def hover_to_element(driver, element):
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()