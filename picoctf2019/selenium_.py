import time
from selenium import webdriver

import percache
cache = percache.Cache('util')

lasttime = None

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def getPng(input):
    driver.get('https://2019shell1.picoctf.com/problem/59857/?#')
    search_box = driver.find_element_by_id("user_in")
    search_box.clear()
    search_box.send_keys(input)
    search_box.submit()
    driver.save_screenshot(input + '.png')
    return driver.find_element_by_id("Area").get_attribute("src")


for p1 in ['1', '2']:
    for p2 in ['5', '6']:
        for p3 in ['0', '1']:
            res = getPng('45496185' + p1 + p2 + p3 + '12495')


#"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAoCAIAAAAKd49AAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA4SURBVFhH7c4xAQAwDASh+jf9nfCQ4VDA2wElKEEJSlCCEpSgBCUoQQlKUIISlKAEJShBCQ4ktg/JBIyNO+jcbAAAAABJRU5ErkJggg=="


driver.quit()
