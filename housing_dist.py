import os
import selenium
from selenium import webdriver as wd
import time

b = wd.Firefox()
b.get('http://dos.cornell.edu/off-campus-living/housing-search-process/search')
b.find_elements_by_partial_link_text('Search Rental Listings')[0].click()
b.close()
b.switch_to_window(b.window_handles[0])
#b.find_elements_by_class_name('p_AFTextOnly')[1].click()
time.sleep(2)
while(1):
    try:
        b.find_elements_by_id('cb1')[0].click()
        break
    except:
        pass
b.find_elements_by_id('qryId2:val00::content')[0].clear()
b.find_elements_by_id('qryId2:val00::content')[0].send_keys('8/15/2016')
b.find_elements_by_id('qryId2:val11::content')[0].clear()
b.find_elements_by_id('qryId2:val11::content')[0].send_keys('650')
b.find_elements_by_id('qryId2::search')[0].click()

time.sleep(3)
address = b.find_elements_by_class_name('x16z')
for i, a in enumerate(address):
    address[i] = a.get_attribute('innerHTML')

b.get('http://www.mapdevelopers.com/distance_from_to.php')
time.sleep(2)
for i in range(0, len(address)):
    f = b.find_elements_by_id('fromInput')[0]
    f.clear()
    f.send_keys(address[i] + ' Ithaca NY')
    t = b.find_elements_by_id('toInput')[0]
    t.clear()
    t.send_keys('242 Carpenter Hall Ithaca NY')
    b.find_elements_by_class_name('link_button')[0].click()
    time.sleep(1)
    
    print address[i], b.find_elements_by_id('driving_status')[0].get_attribute('innerHTML')
    


