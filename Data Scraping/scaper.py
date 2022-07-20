from cgi import test
from lib2to3.pgen2 import driver
from sys import getprofile
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import json


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("window-size=1280,800")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 1}
)
driver=webdriver.Chrome(chrome_options=option,executable_path=r"C:\Users\sangam\AppData\Local\Programs\Python\Python310\chromedriver.exe")
driver.get('https://www.nepalhomes.com/list/&sort=1&page=1&agency_id=&is_project=&find_district_id=&find_area_id=&find_property_category=5d660cb27682d03f547a6c4a')
time.sleep(5)
for i in range(0,328):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        text='Load More'
        load_button=driver.find_element_by_xpath('//button[contains(text(), "' + text + '")]')
        load_button.click()
        time.sleep(2);
text='Property by:'
datas=[]
# blocks=driver.load_button=driver.find_elements_by_xpath('//p[contains(text(), "' + text + '")]')
blocks=driver.find_elements_by_css_selector('div.flex.flex-wrap.py-6.border-b.border-gray-200')
time.sleep(5)

price_count=2100
k=3*price_count
for i in range(price_count,len(blocks)):
    keys=[]
    values=[]
    print('iter',price_count)
   

    try:
        text='Ropani-Aana-Paisa-Daam'
        #land_elem=driver.find_element_by_xpath('//button[contains(text(), "' + text + '")]')
        land_elem=driver.find_elements_by_xpath("//div[@class='flex-1 pl-2']")
        area_elem=land_elem[k].find_element_by_tag_name('p')
        print('this is ares',area_elem.text)
        print("next elem here in land")
        
        keys.append('area')
        values.append(area_elem.text)
    except NoSuchElementException:
        print('Area elem not found')

    price=''
    try:
       price_found=driver.find_elements_by_xpath('//p[contains(text(), "Rs.") or contains(text(), "Price On Call")]')
       price=price_found[price_count].text
       print("this is price ",price)
       keys.append('house_price')
       values.append(price)
    except NoSuchElementException:
       print("couldn't find the house price")

    
    blocks[i].click()
    chwd=driver.window_handles
    driver.switch_to.window(chwd[1])
    time.sleep(3)

    try:
        title_elem=driver.find_element_by_xpath("//h1[@class='text-2xl lg:text-5xl leading-tight']")
        keys.append('title')
        values.append(title_elem.text)
        print('this is title :',title_elem.text)
    except NoSuchElementException:
        print('title elem not found')
    try:
        house_location_elem=driver.find_element_by_css_selector('p.flex-1.pl-3.text-sm.text-gray-500');
        house_location=house_location_elem.text
        keys.append('house_location')
        values.append(house_location_elem.text)
    except NoSuchElementException:
        print('house location not found')
        
    
    

    Amenities=[]
    try:

        
        Amenities_elems=driver.find_elements_by_xpath("//div[@class='w-1/2 lg:w-1/5 text-center px-4 my-4 flex items-center']")
        print("these ammm")
        for i in Amenities_elems:
            elems=i.find_elements_by_xpath(".//*")
            print("next elem")
            Amenity=i.find_element_by_tag_name('p')
            Amenities.append(Amenity.text)
        keys.append('amenities')
        values.append(Amenities)
    except NoSuchElementException:
        print("couldn't find the element")
    

    try:
        middle_elems=driver.find_elements_by_css_selector('div.flex1.pl-6')

        if len(middle_elems)>0:
            try:
                category_elem=middle_elems[0].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[0].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[0].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[0].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[0].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[0].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[0].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[0].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[0].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')



        if len(middle_elems)>1:
            try:
                category_elem=middle_elems[1].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[1].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[1].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[1].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[1].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[1].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[1].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[1].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)
                
                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[1].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')


        if len(middle_elems)>2:
            try:
                category_elem=middle_elems[2].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[2].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[2].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[2].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[2].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[2].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[2].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[2].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[2].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')


        if len(middle_elems)>3:
            try:
                category_elem=middle_elems[3].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[3].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[3].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[3].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[3].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[3].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[3].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[3].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[3].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')

        if len(middle_elems)>4:
            try:
                category_elem=middle_elems[4].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[4].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[4].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[4].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[4].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[4].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[4].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[4].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[4].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')

        if len(middle_elems)>5:
            try:
                category_elem=middle_elems[5].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[5].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[5].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[5].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[5].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[5].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[5].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[5].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[5].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

               


                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')

        if len(middle_elems)>6:
            try:
                category_elem=middle_elems[6].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[6].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[6].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[6].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[6].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[6].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[6].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[6].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[6].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')


        if len(middle_elems)>7:
            try:
                category_elem=middle_elems[7].find_element_by_css_selector('span.text-xs.font-bold.text-gray-400')
                if category_elem.text=="Property Face":
                    print('Property Face Category')
                    property_face_child=middle_elems[7].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    property_face=property_face_child.text
                    keys.append('property_face')
                    values.append(property_face_child.text)
                    print(property_face)
                elif category_elem.text=="Ownership Type":
                    print('Ownership Category')
                    ownership_type_child=middle_elems[7].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    ownership_type=ownership_type_child.text
                    keys.append('ownership_category')
                    values.append(ownership_type_child.text)
                    print(ownership_type)   
                elif category_elem.text=="Road Access":
                    print('Road Category')
                    road_access_child=middle_elems[7].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    road_access=road_access_child.text
                    keys.append('road_access')
                    values.append(road_access_child.text)
                    print(road_access)
                elif category_elem.text=="Parking":
                    print('Parking Category')
                    parking_child=middle_elems[7].find_element_by_css_selector('span.text-sm.font-bold.block.text-gray-600')
                    parking=parking_child.text
                    keys.append('parking')
                    values.append(parking_child.text)
                    print(parking)
                elif category_elem.text=="Floors":
                    print('Floors Category')
                    floors_child=middle_elems[7].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    floors=floors_child.text
                    keys.append('floors')
                    values.append(floors_child.text)
                    print(floors)
                elif category_elem.text=="Bedrooms":
                    print('Bedrooms Category')
                    bedrooms_child=middle_elems[7].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bedrooms=bedrooms_child.text
                    keys.append('bedrooms')
                    values.append(bedrooms_child.text)
                    print(bedrooms)

                elif category_elem.text=="Bathrooms":
                    print('Bathrooms category')
                    bathrooms_child=middle_elems[7].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    bathrooms=bathrooms_child.text
                    keys.append('bathrooms')
                    values.append(bathrooms_child.text)
                    print(bathrooms)

                elif category_elem.text=="Built Up Area":
                    print('builtuparea category')
                    builtuparea_child=middle_elems[7].find_element_by_css_selector('span.font-bold.block.text-gray-600')
                    builtuparea=builtuparea_child.text
                    keys.append('builtuparea')
                    values.append(builtuparea_child.text)
                    print(builtuparea)

                print('Now Moving On')
            
            except NoSuchElementException:
                print('No element found')


    except NoSuchElementException:
        print('Not found')


   
    dict={}
    for i,j in zip(keys,values):
        dict[i]=j
    datas.append(dict)
    driver.close()
    driver.switch_to.window(chwd[0])
    print('Ending this iteration ',str(price_count))
    k=k+3
    price_count=price_count+1
    if price_count==5 or price_count==100 or price_count==200 or price_count==300 or price_count==400 or price_count==500 or price_count==600 or price_count==700 or price_count==800 or price_count==900 or price_count==1000 or price_count==1100 or price_count==1200 or price_count==1300 or price_count==1400 or price_count==1500 or price_count==1600 or price_count==1700 or price_count==1800 or price_count==1900 or price_count==2000 or price_count==2100 or price_count==2200 or price_count==2300 or price_count==2400 or price_count==2500 or price_count==2600:
        with open('data'+str(price_count)+'.json', 'w', encoding='utf-8') as f:
            json.dump(datas, f, ensure_ascii=False, indent=4)
        datas=[]
print(datas)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(datas, f, ensure_ascii=False, indent=4)
print(datas)
time.sleep(5)









