from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time
from Data import demo_reading

locat_obj = demo_reading.read_locators()

class DemoFile:

    def __init__(self,driver):
        self.driver = driver

    def demo_electronic(self):
        element = self.driver.find_element(*locat_obj['txt_electronics'])
        ac_obj = ActionChains(self.driver)
        ac_obj.move_to_element(element).perform()



        element1 = self.driver.find_element(*locat_obj['txt_camera'])
        ac_obj.click(element1).perform()

    def demo_sort_A_to_Z(self):
        element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        sel_obj = Select(element2)
        sel_obj.select_by_visible_text("Position")

        ac_obj = ActionChains(self.driver)

        sel_obj.select_by_visible_text("Name: A to Z")

        ac_obj.send_keys(Keys.PAGE_DOWN).perform()

        ac_obj.send_keys(Keys.PAGE_UP)

    def demo_sort_Z_to_A(self):
        element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        sel_obj = Select(element2)

        ac_obj = ActionChains(self.driver)

        sel_obj.select_by_visible_text("Name: Z to A")

        ac_obj.send_keys(Keys.PAGE_DOWN).perform()

        ac_obj.send_keys(Keys.PAGE_UP)

    def demo_sort_Low_to_High(self):
        element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        sel_obj = Select(element2)

        ac_obj = ActionChains(self.driver)

        sel_obj.select_by_visible_text("Price: Low to High")

        ac_obj.send_keys(Keys.PAGE_DOWN).perform()

        ac_obj.send_keys(Keys.PAGE_UP)

    def demo_sort_High_to_Low(self):
        element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        sel_obj = Select(element2)

        ac_obj = ActionChains(self.driver)

        sel_obj.select_by_visible_text("Price: High to Low")

        ac_obj.send_keys(Keys.PAGE_DOWN).perform()

        ac_obj.send_keys(Keys.PAGE_UP)

    def demo_cearted_on(self):
        element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        sel_obj = Select(element2)

        ac_obj = ActionChains(self.driver)

        sel_obj.select_by_visible_text("Created on")

        ac_obj.send_keys(Keys.PAGE_DOWN).perform()

        ac_obj.send_keys(Keys.PAGE_UP)

    def cam_dispaly1(self):

        element3 = self.driver.find_element(*locat_obj['txt_display'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(0)

    def cam_dispaly2(self):

        element3 = self.driver.find_element(*locat_obj['txt_display'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(1)

    def cam_dispaly3(self):

        element3 = self.driver.find_element(*locat_obj['txt_display'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(2)

    def cam_view1(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("List")

        ac_obj = ActionChains(self.driver)
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)

    def cam_view2(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("Grid")

        ac_obj = ActionChains(self.driver)
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)

    def cam_filter(self):
        self.driver.find_element(*locat_obj['txt_price1']).click()
        time.sleep(2)
        ac_obj = ActionChains(self.driver)

        self.driver.find_element(*locat_obj['txt_price_remove1']).click()

        self.driver.find_element(*locat_obj['txt_price2']).click()

        self.driver.find_element(*locat_obj['txt_price_remove2']).click()


    def cam_des(self):
        list1 = ['1MP 60GB Hard Drive Handycam Camcorder', 'Camcorder', 'Digital SLR Camera 12.2 Mpixel',
                 'High Definition 3D Camcorder']
        for element in list1:
            self.driver.find_element("xpath", f"//a[text()='{element}']").click()
            self.driver.back()


class Democell:
    def __init__(self,driver):
        self.driver = driver

    def cell(self):

        element = self.driver.find_element(*locat_obj['txt_electro'])

        ac_obj = ActionChains(self.driver)

        ac_obj.move_to_element(element).perform()

        element1 = self.driver.find_element(*locat_obj['txt_cell'])

        ac_obj.click(element1).perform()

    def cell_sort1(self):

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)

        sel_obj.select_by_visible_text("Name: A to Z")

        self.driver.back()

    def cell_sort2(self):

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)

        sel_obj.select_by_visible_text("Name: Z to A")

        self.driver.back()

    def cell_sort3(self):

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)

        sel_obj.select_by_visible_text("Price: Low to High")

        self.driver.back()

    def cell_sort4(self):

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)

        sel_obj.select_by_visible_text("Price: High to Low")

        self.driver.back()

    def cell_sort5(self):

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)

        sel_obj.select_by_visible_text("Created on")

        self.driver.back()


    def cell_display1(self):
        element3 = self.driver.find_element(*locat_obj['txt_display_cell'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(0)



    def cell_display2(self):
        element3 = self.driver.find_element(*locat_obj['txt_display_cell'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(1)



    def cell_display3(self):
        element3 = self.driver.find_element(*locat_obj['txt_display_cell'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(2)

        self.driver.back()



    def cell_view(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby_cell'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("List")

        self.driver.back()

    def cell_view2(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby_cell'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("Grid")

        self.driver.back()


    def cell_des(self):

        list2 = ['Smartphone', 'Used phone', 'Phone Cover']
        for item in list2:
            self.driver.find_element("xpath", f"//a[text()='{item}']").click()

            self.driver.back()


    def cell_addto(self):
        self.driver.find_element(*locat_obj['txt_add1']).click()

        self.driver.find_element(*locat_obj['txt_add2']).click()


