import pyautogui as pg

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',1.5)
pg.hotkey('winleft','up')
pg.typewrite('Donald Trump\n',0.5)
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('tab')
pg.hotkey('enter')
pg.moveTo(121, 380,0.5)
pg.click()



