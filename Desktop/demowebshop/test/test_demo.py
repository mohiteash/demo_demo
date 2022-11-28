from POM.demo_electronics import DemoFile
from POM.demo_electronics import Democell

class TestDemo:
    def test_demoelec(self,_driver):
        demo = DemoFile(_driver)
        demo.demo_electronic()
        demo.demo_sort_A_to_Z()
        demo.demo_sort_Z_to_A()
        demo.demo_sort_Low_to_High()
        demo.demo_sort_High_to_Low()
        demo.demo_cearted_on()
        demo.cam_dispaly1()
        demo.cam_dispaly2()
        demo.cam_dispaly3()
        demo.cam_view1()
        demo.cam_view2()
        demo.cam_filter()
        demo.cam_des()

    def test_democell(self,_driver):
        demo1 = Democell(_driver)
        demo1.cell()
        demo1.cell_sort1()
        demo1.cell_sort2()
        demo1.cell_sort3()
        demo1.cell_sort4()
        demo1.cell_sort5()
        demo1.cell_display1()
        demo1.cell_display2()
        demo1.cell_display3()
        demo1.cell_view()
        demo1.cell_view2()
        demo1.cell_des()
        demo1.cell_addto()

