import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_shorts(self) -> None:
        self.driver.find_element(by=AppiumBy.ID,
                                 value='new UiSelector().resourceId("com.google.android.youtube:id/image").instance(2)').click()

    def test_tap(self) -> None:
        self.driver.tap([(399, 2072)])

    def test_scroll(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(4)')
        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(5)')
        self.driver.scroll(el1, el2)

    def test_swipe(self) -> None:
        self.driver.tap([(505, 725)])
        time.sleep(2)
        self.driver.swipe(32, 356, 346, 356)

    def test_home(self) -> None:
        self.driver.find_element(by=AppiumBy.ID,
                                 value='new UiSelector().resourceId("android:id/navigationBarBackground")').click()
