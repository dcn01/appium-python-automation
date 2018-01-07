import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_desired_capabilities():
    desired_caps = {
        'deviceName': 'iPhone 5c',
        'platformName': 'iOS',
        'platformVersion': '10.3',
        'app': PATH('TIDY-1.7.3.428.ipa'),
        'automationName': 'XCUITest',
        'allowTouchIdEnroll': True
    }

    return desired_caps