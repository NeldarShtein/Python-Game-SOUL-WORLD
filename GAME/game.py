import pygame
import random

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("SoulWorld")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

walkRight = [pygame.image.load("character_image/RC1.png"), pygame.image.load("character_image/RO1.png")]
walkLeft = [pygame.image.load("character_image/LC1.png"), pygame.image.load("character_image/LO1.png")]
playerStand = [pygame.image.load("character_image/DMO1.png"), pygame.image.load("character_image/DMC1.png")]
playerStand2 = [pygame.image.load("character_image/DMO1.png"), pygame.image.load("character_image/DMC1.png")]
bg = pygame.image.load("bg2.png")
creation = pygame.image.load("creation.png")
heart_img = pygame.image.load("obj_images/heart.png")
apple_img = pygame.image.load("obj_images/apple2.png")
bullet_img = pygame.image.load("obj_images/bullet.png")
bullet_img2 = pygame.image.load("obj_images/bullet2.png")
enemy1_img = pygame.image.load("enemy_image/AR1.png")
enemy2_img = pygame.image.load("enemy_image/AR2.png")
enemy3_img = pygame.image.load("enemy_image/AR3.png")
enemy4_img = pygame.image.load("enemy_image/AR4.png")
enemy5_img = pygame.image.load("enemy_image/SF.png")

pygame.mixer.music.load("Sound/bg.mp3")
buttom_sound = pygame.mixer.Sound("Sound/b.mp3")
gg_sound = pygame.mixer.Sound("Sound/gg.mp3")
in1 = pygame.mixer.Sound("Sound/intro1.mp3")
in2 = pygame.mixer.Sound("Sound/intro2.mp3")
in3 = pygame.mixer.Sound("Sound/intro3.mp3")
in4 = pygame.mixer.Sound("Sound/intro4.mp3")
in5 = pygame.mixer.Sound("Sound/intro5.mp3")
in6 = pygame.mixer.Sound("Sound/intro6.mp3")
in7 = pygame.mixer.Sound("Sound/intro7.mp3")
in8 = pygame.mixer.Sound("Sound/intro8.mp3")
in9 = pygame.mixer.Sound("Sound/intro_for_choose_difficult.mp3")
lv1 = pygame.mixer.Sound("Sound/level_1_intro.mp3")
lv2 = pygame.mixer.Sound("Sound/level_2_intro.mp3")
lv3 = pygame.mixer.Sound("Sound/level_3_intro.mp3")
lv4 = pygame.mixer.Sound("Sound/level_4_intro.mp3")
lv5 = pygame.mixer.Sound("Sound/level_5_intro.mp3")
lv6 = pygame.mixer.Sound("Sound/level_6_intro.mp3")
lv7 = pygame.mixer.Sound("Sound/level_7_intro.mp3")
lv8 = pygame.mixer.Sound("Sound/level_8_intro.mp3")
lv9 = pygame.mixer.Sound("Sound/level_9_intro.mp3")
lv10 = pygame.mixer.Sound("Sound/level_10_intro.mp3")
lv11 = pygame.mixer.Sound("Sound/level_11_intro.mp3")
lv12 = pygame.mixer.Sound("Sound/level_12_intro.mp3")
lv13 = pygame.mixer.Sound("Sound/level_13_intro.mp3")
lv14 = pygame.mixer.Sound("Sound/level_14_intro.mp3")
lv15 = pygame.mixer.Sound("Sound/level_15_intro.mp3")
bullet_sound = pygame.mixer.Sound("Sound/bullet.mp3")

def stop_sound():
	pygame.mixer.Sound.stop(in1)
	pygame.mixer.Sound.stop(in2)
	pygame.mixer.Sound.stop(in3)
	pygame.mixer.Sound.stop(in4)
	pygame.mixer.Sound.stop(in5)
	pygame.mixer.Sound.stop(in6)
	pygame.mixer.Sound.stop(in7)
	pygame.mixer.Sound.stop(in8)
	pygame.mixer.Sound.stop(in9)
	pygame.mixer.Sound.stop(lv1)
	pygame.mixer.Sound.stop(lv2)
	pygame.mixer.Sound.stop(lv3)
	pygame.mixer.Sound.stop(lv4)
	pygame.mixer.Sound.stop(lv5)
	pygame.mixer.Sound.stop(lv6)
	pygame.mixer.Sound.stop(lv7)
	pygame.mixer.Sound.stop(lv8)
	pygame.mixer.Sound.stop(lv9)
	pygame.mixer.Sound.stop(lv10)
	pygame.mixer.Sound.stop(lv11)
	pygame.mixer.Sound.stop(lv12)
	pygame.mixer.Sound.stop(lv13)
	pygame.mixer.Sound.stop(lv14)
	pygame.mixer.Sound.stop(lv15)

class Button:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.inactive_clr = (255, 255, 255)
		self.active_clr = (122, 122, 122)
	def draw(self, x, y, message, action=None, font_size=30):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))
			if click[0] == 1:
				pygame.mixer.Sound.play(buttom_sound)
				pygame.time.delay(300)
				if action is not None:
					if action == quit:
						pygame.quit()
						quit()
					else:
						action()
		else:
			pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))
		print_Text2(message=message, x=x + 10, y=y + 10, font_size=font_size)
class Button2:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.inactive_clr = (0, 0, 0)
		self.active_clr = (60, 60, 60)
	def draw(self, x, y, message, action=None, font_size=30):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))
			if click[0] == 1:
				pygame.mixer.Sound.play(buttom_sound)
				pygame.time.delay(300)
				if action is not None:
					if action == quit:
						pygame.quit()
						quit()
					else:
						action()
		else:
			pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))
		print_Text(message=message, x=x + 10, y=y + 10, font_size=font_size)
class Bullet:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.bul_width = 30
		self.bul_height = 20
		self.speed = 8

	def move(self):
		self.x += self.speed
		if self.x <= display_width:
			display.blit(bullet_img, (self.x, self.y))
			return True
		else:
			return False
class Bullet2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 8

	def move(self):
		self.x -= self.speed
		if self.x <= display_width:
			display.blit(bullet_img2, (self.x, self.y))
			return True
		else:
			return False

global_luck = random.randint(0, 0)
global_luck2 = random.randint(0, 0)
global_luck3 = random.randint(0, 0)

GL = global_luck * 10
GL2 = global_luck2 * 10
GL3 = global_luck3 * 10
TGL = global_luck + global_luck2 + global_luck3
character_colour3 = (GL, GL2, GL3)
saved_TGL = 0
TGL_lvl_8 = 50
p17 = random.randint(4, 10)

display_width = 1080
display_height = 720
display = pygame.display.set_mode((display_width, display_height))

user_width = 81
user_height = 86
user_speed = 5
user_x = 100
user_y = display_height - user_height - 100

level_1_intro_n = 1
level_2_intro_n = 1
level_3_intro_n = 1
level_4_intro_n = 1
level_5_intro_n = 1
level_6_intro_n = 1
level_7_intro_n = 1
level_8_intro_n = 1
level_9_intro_n = 1
level_10_intro_n = 1
level_11_intro_n = 1
level_12_intro_n = 1
level_13_intro_n = 1
level_14_intro_n = 1
level_15_intro_n = 1

user_width1 = 81
user_height1 = 86
user_speed1 = 5
user_x1 = display_width - 100
user_y1 = display_height - user_height - 100

make_jump = False
jump_counter = 30

go_right_count = 30
go_left_count = 30
go_left = False
go_right = False
left = False
right = False
aimCount = 0

p = 0
a = [True, False, False, False, False]
b = [True, True, False, False, False, False]
c = [True, True, True, False, False, False]
d = [True, True, True, True, False, False]
e = [True, True, True, True, False]

waiting_time_lvl_10 = 600
level_number = 1
left_level_quantity = 1
first_start_recognizer = 1
paused = False
pause_lim = random.randint(1, 20)
level_lives = 1
difficult_multiplier = 1
cooldown_bullet = 0
all_btn_bullets = []
quant_of_bul = 0
attack_amount_lvl = 10
jump_amount = 5

obstacle_height = 90
obstacle_width = 20
obstacle_x = display_width - 50
obstacle_y = display_height - obstacle_height - 100

def OVSC1_draw():
	global obstacle_height, obstacle_y, obstacle_width, obstacle_x
	if obstacle_x >= -obstacle_width:
		pygame.draw.rect(display, (255, 255, 255), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
		obstacle_x -= 3
	else:
		obstacle_x = display_width

obstacle2_height = 87
obstacle2_width = 2000
obstacle2_x = -2000
obstacle2_y = display_height - obstacle2_height - 100

def OVSC2_draw():
	global obstacle2_height, obstacle2_y, obstacle2_width, obstacle2_x
	pygame.draw.rect(display, (255, 20, 20), (obstacle2_x, obstacle2_y, obstacle2_width, obstacle2_height))
	if difficult_multiplier == 1:
		obstacle2_x += 1
	if difficult_multiplier == 2:
		obstacle2_x += 0.75
	if difficult_multiplier == 3:
		obstacle2_x += 0.3

obstacle3_height = 87
obstacle3_width = 4
obstacle3_x = display_width - 80
obstacle3_y = display_height - obstacle3_height - 100

def OVSC3_draw():
	global obstacle3_height, obstacle3_y, obstacle3_width, obstacle3_x
	pygame.draw.rect(display, (20, 255, 20), (obstacle3_x, obstacle3_y, obstacle3_width, obstacle3_height))

obstacle4_height = 70
obstacle4_width = 20
obstacle4_x = display_width - 50
obstacle4_y = display_height - obstacle4_height - 100

def OVSC4_draw():
	global obstacle4_height, obstacle4_y, obstacle4_width, obstacle4_x
	if obstacle4_x >= -obstacle4_width:
		pygame.draw.rect(display, (255, 255, 255), (obstacle4_x, obstacle4_y, obstacle4_width, obstacle4_height))
		obstacle4_x -= 3
	else:
		obstacle4_x = display_width

obstacle5_height = 50
obstacle5_width = 20
obstacle5_x = display_width - 50
obstacle5_y = display_height - obstacle5_height - 100

def OVSC5_draw():
	global obstacle5_height, obstacle5_y, obstacle5_width, obstacle5_x
	if obstacle5_x >= -obstacle5_width:
		pygame.draw.rect(display, (255, 255, 255), (obstacle5_x, obstacle5_y, obstacle5_width, obstacle5_height))
		obstacle5_x -= 3
	else:
		obstacle5_x = display_width

obstacle6_height = 30
obstacle6_width = 30
obstacle6_x = display_width / 2
obstacle6_y = display_height - obstacle6_height - 130

def OVSC6_draw():
	global obstacle6_height, obstacle6_y, obstacle6_width, obstacle6_x
	display.blit(apple_img, (obstacle6_x, obstacle6_y))

obstacle7_height = 30
obstacle7_width = 230
obstacle7_x = 465 - 115
obstacle7_y = 0

def OVSC7_draw():
	global obstacle7_height, obstacle7_y, obstacle7_width, obstacle7_x
	if obstacle7_y < display_height + 100:
		pygame.draw.rect(display, (255, 255, 255), (obstacle7_x, obstacle7_y, obstacle7_width, obstacle7_height))
		obstacle7_y += 5
	else:
		obstacle7_y = -150

obstacle8_height = 40
obstacle8_width = 400
obstacle8_x = display_width - obstacle8_width
obstacle8_y = -600

def OVSC8_draw():
	global obstacle8_height, obstacle8_y, obstacle8_width, obstacle8_x
	if obstacle8_y < display_height + 100:
		pygame.draw.rect(display, (255, 255, 255), (obstacle8_x, obstacle8_y, obstacle8_width, obstacle8_height))
		obstacle8_y += 2.4
	else:
		obstacle8_y = -150

obstacle9_height = 20
obstacle9_width = 250
obstacle9_x = 0
obstacle9_y = 0

def OVSC9_draw():
	global obstacle9_height, obstacle9_y, obstacle9_width, obstacle9_x
	if obstacle9_y < display_height + 100:
		pygame.draw.rect(display, (255, 255, 255), (obstacle9_x, obstacle9_y, obstacle9_width, obstacle9_height))
		obstacle9_y += 2.6
	else:
		obstacle9_y = -100

obstacle10_height = 96
obstacle10_width = 65
obstacle10_x = display_width + 100
obstacle10_y = display_height - obstacle10_height - 100

def OVSC10_draw():
	global obstacle10_y, obstacle10_width, obstacle10_x
	if obstacle10_x > - 100:
		display.blit(enemy1_img, (obstacle10_x, obstacle10_y))
		if difficult_multiplier == 1:
			obstacle10_x -= 2.5
		if difficult_multiplier == 2:
			obstacle10_x -= 4.5
		if difficult_multiplier == 3:
			obstacle10_x -= 5.5
	else:
		obstacle10_x = display_width + obstacle10_width

obstacle11_height = 100
obstacle11_width = 38
obstacle11_x = display_width + 200
obstacle11_y = display_height - obstacle11_height - 100

def OVSC11_draw():
	global obstacle11_height, obstacle11_y, obstacle11_width, obstacle11_x
	if obstacle11_x > - 100:
		display.blit(enemy2_img, (obstacle11_x, obstacle11_y))
		if difficult_multiplier == 1:
			obstacle11_x -= 1.5
		if difficult_multiplier == 2:
			obstacle11_x -= 2.5
		if difficult_multiplier == 3:
			obstacle11_x -= 5
	else:
		obstacle11_x = display_width + obstacle11_width

obstacle12_height = 100
obstacle12_width = 38
obstacle12_x = - 650
obstacle12_y = display_height - obstacle12_height - 100

def OVSC12_draw():
	global obstacle12_height, obstacle12_y, obstacle12_width, obstacle12_x
	if obstacle12_x > - 100:
		display.blit(enemy3_img, (obstacle12_x, obstacle12_y))
		if difficult_multiplier == 1:
			obstacle12_x += 1.5
		if difficult_multiplier == 2:
			obstacle12_x += 2.5
		if difficult_multiplier == 3:
			obstacle12_x += 5
	else:
		obstacle12_x = 0 - obstacle12_width

obstacle13_height = 96
obstacle13_width = 65
obstacle13_x = - 400
obstacle13_y = display_height - obstacle13_height - 100

def OVSC13_draw():
	global obstacle13_height, obstacle13_y, obstacle13_width, obstacle13_x
	if obstacle13_x < display_width + 120:
		display.blit(enemy4_img, (obstacle13_x, obstacle13_y))
		if difficult_multiplier == 1:
			obstacle13_x += 1.5
		if difficult_multiplier == 2:
			obstacle13_x += 2.5
		if difficult_multiplier == 3:
			obstacle13_x += 3
	else:
		obstacle13_x = 0 - obstacle13_width

obstacle14_height = 500
obstacle14_width = 3
obstacle14_x = display_width - 500
obstacle14_y = display_height - obstacle14_height - 100

def OVSC14_draw():
	global obstacle14_y, obstacle14_width, obstacle14_x, obstacle14_height
	if obstacle14_x > - 100:
		pygame.draw.rect(display, (255, 20, 255), (obstacle14_x, obstacle14_y, obstacle14_width, obstacle14_height))
		if difficult_multiplier == 1:
			obstacle14_x -= 2.5
		if difficult_multiplier == 2:
			obstacle14_x -= 4.5
		if difficult_multiplier == 3:
			obstacle14_x -= 5.5
	else:
		obstacle14_x = display_width + obstacle14_width

def show_menu():
	menu_bg = pygame.image.load("Mbg2.png")
	stop_sound()
	pygame.mixer.music.play(-1)
	start_btn = Button(345, 70)
	cont_btn = Button(330, 70)
	quit_btn = Button(165, 70)
	quit_btn = Button(165, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		start_btn.draw(365, 155, "NEW GAME", intro1, 50)
		cont_btn.draw(370, 285, "CONTINUE", check1, 50)
		quit_btn.draw(450, 535, "QUIT", quit, 50)
		#quit_btn.draw(450, 410, "WIN", level_15, 50)
		pygame.display.update()
		clock.tick(60)
def show_menu2():
	menu_bg = pygame.image.load("Mbg2.png")
	stop_sound()
	start_btn = Button(345, 70)
	quit_btn = Button(165, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		start_btn.draw(365, 155, "NEW GAME", intro1, 50)
		quit_btn.draw(450, 535, "QUIT", quit, 50)
		pygame.display.update()
		clock.tick(60)
def check1():
	if TGL < 1:
		show_menu2()
	elif level_lives == 0:
		gg()
	else:
		level_checker()
def check2():
	if TGL < 1:
		Tgg()
	elif level_lives == 0:
		gg()
	else:
		level_checker()
def choose_difficult():
	menu_bg = pygame.image.load("Mbg.png")
	stop_sound()
	pygame.mixer.music.unpause()
	easy_btn = Button(170, 70)
	normal_btn = Button(280, 70)
	hard_btn = Button(190, 70)
	back_btn = Button(175, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		x = 250
		y = 25
		print_Text("DIFFICULTY", x, y, font_size=85)
		easy_btn.draw(450, 150, "EASY", dif_easy, 50)
		normal_btn.draw(400, 275, "NORMAL", dif_normal, 50)
		hard_btn.draw(445, 400, "HARD", dif_hard, 50)
		back_btn.draw(450, 525, "BACK", show_menu, 50)
		pygame.display.update()
		clock.tick(60)
def choose_difficult1():
	menu_bg = pygame.image.load("Mbg.png")
	stop_sound()
	pygame.mixer.music.unpause()
	easy_btn = Button(170, 70)
	normal_btn = Button(280, 70)
	hard_btn = Button(190, 70)
	back_btn = Button(175, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		x = 250
		y = 25
		print_Text("DIFFICULTY", x, y, font_size=85)
		easy_btn.draw(450, 150, "EASY", dif_easy1, 50)
		normal_btn.draw(400, 275, "NORMAL", dif_normal1, 50)
		hard_btn.draw(445, 400, "HARD", dif_hard1, 50)
		back_btn.draw(450, 525, "BACK", show_menu, 50)
		pygame.display.update()
		clock.tick(60)
def choose_difficult2():
	menu_bg = pygame.image.load("Mbg.png")
	stop_sound()
	pygame.mixer.music.unpause()
	normal_btn = Button(280, 70)
	hard_btn = Button(190, 70)
	back_btn = Button(175, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		x = 250
		y = 25
		print_Text("DIFFICULTY", x, y, font_size=85)
		normal_btn.draw(400, 275, "NORMAL", dif_normal1, 50)
		hard_btn.draw(445, 400, "HARD", dif_hard1, 50)
		back_btn.draw(450, 525, "BACK", show_menu, 50)
		pygame.display.update()
		clock.tick(60)
def choose_difficult3():
	menu_bg = pygame.image.load("Mbg.png")
	stop_sound()
	pygame.mixer.music.unpause()
	hard_btn = Button(190, 70)
	back_btn = Button(175, 70)
	show = True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.blit(menu_bg, (0, 0))
		x = 250
		y = 25
		print_Text("DIFFICULTY", x, y, font_size=85)
		hard_btn.draw(445, 400, "HARD", dif_hard1, 50)
		back_btn.draw(450, 525, "BACK", show_menu, 50)
		pygame.display.update()
		clock.tick(60)
def start_New_game():
	cho_rand_char()
	GL_reset()
	stop_sound()
	level_checker()
def start_New_game2():
	cho_rand_char()
	stop_sound()
	level_checker()
def game_continue():
	while game_cycle():
		pass
def game_continue2():
	global paused
	paused = False
def game_cycle():
	game = True
	cho_cha()
	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.blit(bg, (0, 0))
			pygame.draw.rect(display, character_colour3, (user_x1, user_y1, user_width1, user_height1))
			TGL_DISP()
			show_health()
			KeyP()
			left = False
			right = False
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def drawWin():
	global aimCount
	aimCount += 1
def jump():
	global user_y, jump_counter, make_jump, jump_amount
	if jump_counter >= -30:
		user_y -= jump_counter / 2.5
		jump_counter -= 1
	else:
		jump_amount +=1
		jump_counter = 30
		make_jump = False
def KL1T():
	global user_x, go_left, go_left_count
	if go_left_count >= -30:
		user_x -= go_left_count / 2.5
		go_left_count -= 1
	else:
		go_left_count = 30
		go_left = False
def KR1T():
	global user_x, go_right, go_right_count
	if go_right_count >= -30:
		user_x += go_right_count / 2.5
		go_right_count -= 1
	else:
		go_right_count = 30
		go_right = False
def KL2():
	global user_x, aimCount
	user_x -= TGL / 10
	display.blit(walkLeft[aimCount // 30], (user_x, user_y))
	drawWin()
	left = True
	right = False
	if aimCount + 1 >= 60:
		aimCount = 0
def KR2():
	global user_x, aimCount
	user_x += TGL / 10
	display.blit(walkRight[aimCount // 30], (user_x, user_y))
	drawWin()
	left = False
	right = True
	if aimCount + 1 >= 60:
		aimCount = 0
def KDM():
	global aimCount
	display.blit(playerStand[aimCount // 30], (user_x, user_y))
	drawWin()
	if aimCount + 1 >= 60:
		aimCount = 0
def KDM2():
	global aimCount
	display.blit(playerStand2[aimCount // 30], (880, 534))
	drawWin()
	if aimCount + 1 >= 60:
		aimCount = 0
def KeyP():
	global make_jump
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (user_x > 5):
		KL2()
	elif keys[pygame.K_RIGHT] and user_x < display_width - user_width - 5:
		KR2()
	elif (False == left) and (right == False):
		KDM()
	if keys[pygame.K_SPACE]:
		make_jump = True
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
	if make_jump:
		jump()
def KeyP2():
	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
def KeyP3():
	global make_jump
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (user_x > 5):
		if difficult_multiplier == 1:
			k = random.choice(e)
			if k == True:
				KL2()
			else:
				KDM()
		if difficult_multiplier == 2:
			k = random.choice(c)
			if k == True:
				KL2()
			else:
				KDM()
		if difficult_multiplier == 3:
			k = random.choice(a)
			if k == True:
				KL2()
			else:
				KDM()
	elif keys[pygame.K_RIGHT] and user_x < display_width - user_width - 5:
		if difficult_multiplier == 1:
			k = random.choice(e)
			if k == True:
				KR2()
			else:
				KDM()
		if difficult_multiplier == 2:
			k = random.choice(c)
			if k == True:
				KR2()
			else:
				KDM()
		if difficult_multiplier == 3:
			k = random.choice(a)
			if k == True:
				KR2()
			else:
				KDM()
	elif (False == left) and (right == False):
		KDM()
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
def KeyP4():
	global make_jump, go_left, go_right
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (user_x > 5):
		gg2()
	elif keys[pygame.K_RIGHT] and user_x < display_width - user_width - 5:
		gg2()
	elif (False == left) and (right == False):
		KDM()
	if keys[pygame.K_SPACE]:
		gg2()
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
def KeyP5():
	global make_jump, cooldown_bullet, quant_of_bul
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (user_x > 5):
		KL2()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet2(user_x, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	elif keys[pygame.K_RIGHT] and user_x < display_width - user_width - 5:
		KR2()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet(user_x + user_width - 20, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	elif (False == left) and (right == False):
		KDM()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet(user_x + user_width, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	if keys[pygame.K_SPACE]:
		make_jump = True
	for bullet in all_btn_bullets:
		if not bullet.move():
			all_btn_bullets.remove(bullet)
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
	if make_jump:
		jump()
def KeyP6():
	global make_jump, cooldown_bullet, quant_of_bul
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and (user_x > 5):
		KL2()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet2(user_x, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	elif keys[pygame.K_RIGHT] and user_x < display_width - user_width - 515:
		KR2()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet(user_x + user_width - 20, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	elif (False == left) and (right == False):
		KDM()
		if not cooldown_bullet:
			if keys[pygame.K_k]:
				pygame.mixer.Sound.play(bullet_sound)
				all_btn_bullets.append(Bullet(user_x + user_width, user_y + 20))
				cooldown_bullet = 50
				quant_of_bul += 1
		else:
			cooldown_bullet -= 1
	if keys[pygame.K_SPACE]:
		make_jump = True
	for bullet in all_btn_bullets:
		if not bullet.move():
			all_btn_bullets.remove(bullet)
	if keys[pygame.K_ESCAPE]:
		if pause_lim < 20:
			pause()
		else:
			pause_limit()
	if make_jump:
		jump()
def print_Text(message, x, y, font_color=(255, 255, 255), font_type="18959.ttf", font_size=30):
	font_type = pygame.font.Font(font_type, font_size)
	text = font_type.render(message, True, font_color)
	display.blit(text, (x, y))
def print_Text2(message, x, y, font_color=(0, 0, 0), font_type="18959.ttf", font_size=30):
	font_type = pygame.font.Font(font_type, font_size)
	text = font_type.render(message, True, font_color)
	display.blit(text, (x, y))
def pause():
	pygame.mixer.music.pause()
	global paused
	paused = True
	global pause_lim
	pause_lim += 1
	back2_btn = Button(190, 70)
	cont2_btn = Button(330, 70)
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		cont2_btn.draw(370, 285, "CONTINUE", game_continue2, 50)
		x = display_width / 2 - 230
		y = 150
		print_Text("PAUSED", x, y, font_size=100)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def pause_limit():
	pygame.mixer.music.pause()
	global paused
	paused = True
	global level_lives
	level_lives -= 1
	back3_btn = Button(190, 70)
	cont3_btn = Button(330, 70)
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		back3_btn.draw(440, 400, "MENU", show_menu, 50)
		cont3_btn.draw(370, 285, "CONTINUE", game_continue2, 50)
		x = display_width / 2 - 320
		y = 120
		print_Text("TOO MUCH PAUSE", x, y, font_size=60)
		x = display_width / 2 - 380
		y = 200
		print_Text("YOU LOOSE ONE LIVE", x, y, font_size=60)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def show_health2():
	global level_lives
	show = 0
	x = 20
	while show != level_lives:
		display.blit(heart_img, (x, 20))
		x += 90
		show += 1
def show_health():
	global level_lives
	pygame.draw.rect(display, (0, 0, 0), (0, display_height - 100, display_width, 120))
	pygame.draw.rect(display, (255, 255, 255), (0, display_height - 100, 1080, 3))
	display.blit(heart_img, (20, display_height - 90))
	if level_lives == 1:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("I", 160, display_height - 80, font_size=80)
	if level_lives == 2:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("II", 160, display_height - 80, font_size=80)
	if level_lives == 3:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("III", 160, display_height - 80, font_size=80)
	if level_lives == 4:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("IV", 160, display_height - 80, font_size=80)
	if level_lives == 5:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("V", 160, display_height - 80, font_size=80)
	if level_lives == 6:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("VI", 160, display_height - 80, font_size=80)
	if level_lives == 7:
		print_Text("x", 100, display_height - 80, font_size=80)
		print_Text("VII", 160, display_height - 80, font_size=80)
def gg():
	pygame.mixer.music.pause()
	pygame.mixer.Sound.play(gg_sound)
	stopped = True
	tryAgain_btn = Button(350, 70)
	back2_btn = Button(190, 70)
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 350
		y = 150
		print_Text("GAME OVER", x, y, font_size=100)
		tryAgain_btn.draw(370, 285, "TRY AGAIN", Try_level_again, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def gg2():
	global user_x, obstacle2_x, difficult_multiplier
	user_x = 100
	obstacle2_x = -2000
	if difficult_multiplier == 1:
		M1TGL()
		M1live()
	if difficult_multiplier == 2:
		M2TGL()
		M1live()
	if difficult_multiplier == 3:
		M3TGL()
		M1live()
	level_checker()
def win():
	pygame.mixer.music.pause()
	stopped = True
	tryAgain_btn = Button(190, 70)
	back2_btn = Button(190, 70)
	GL_P_change()
	global left_level_quantity, level_number
	left_level_quantity -= 1
	level_number += 1
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 420
		y = 150
		print_Text("LEVEL PASSED", x, y, font_size=100)
		tryAgain_btn.draw(440, 285, "NEXT", level_checker, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def win3():
	pygame.mixer.music.pause()
	stopped = True
	tryAgain_btn = Button(190, 70)
	back2_btn = Button(190, 70)
	M3TGL()
	global left_level_quantity, level_number
	left_level_quantity -= 1
	level_number += 1
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 420
		y = 150
		print_Text("LEVEL PASSED", x, y, font_size=100)
		tryAgain_btn.draw(440, 285, "NEXT", level_checker, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def win2():
	pygame.mixer.music.pause()
	stopped = True
	tryAgain_btn = Button(190, 70)
	back2_btn = Button(190, 70)
	M3TGL()
	M3TGL()
	global left_level_quantity, level_number
	left_level_quantity -= 1
	level_number += 1
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 350
		y = 150
		print_Text("DISRESPECT", x, y, font_size=100)
		tryAgain_btn.draw(440, 285, "NEXT", level_checker, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def lvl_skip():
	pygame.mixer.music.pause()
	stopped = True
	tryAgain_btn = Button(190, 70)
	back2_btn = Button(190, 70)
	GL_M_change()
	global left_level_quantity, level_number
	left_level_quantity -= 1
	level_number += 1
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 420
		y = 150
		print_Text("LEVEL PASSED", x, y, font_size=100)
		tryAgain_btn.draw(440, 285, "NEXT", level_checker, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def lvl_skip2():
	pygame.mixer.music.pause()
	stopped = True
	tryAgain_btn = Button(190, 70)
	back2_btn = Button(190, 70)
	M3TGL()
	M3TGL()
	GL_M_change()
	global left_level_quantity, level_number
	left_level_quantity -= 1
	level_number += 1
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 420
		y = 150
		print_Text("LEVEL PASSED", x, y, font_size=100)
		tryAgain_btn.draw(440, 285, "NEXT", level_checker, 50)
		back2_btn.draw(440, 400, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
	pygame.mixer.music.unpause()
def Try_level_again():
	pygame.mixer.music.play(-1)
	global difficult_multiplier, level_lives, pause_lim
	if difficult_multiplier == 1:
		level_lives = random.randint(5, 7)
	elif difficult_multiplier == 2:
		level_lives = random.randint(3, 5)
	else:
		level_lives = random.randint(1, 3)
	GL_M_change()
	check2()
def TGL_DISP():
	p57 = random.randint(1, 57)   #x = display_width - 60    y = 150     print_Text(str(TGL), x, y)
def GL_M_change():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck -= 9
	if global_luck < 1:
		global_luck2 += global_luck
		global_luck = 0
	if global_luck2 < 1:
		global_luck3 += global_luck2
		global_luck2 = 0
	if global_luck3 < 1:
		saved_TGL += global_luck3
		global_luck3 = 0
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def GL_P_change():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck += 7
	if global_luck > 25:
		global_luck2 += (global_luck-25)
		global_luck = 25
	if global_luck2 > 25:
		global_luck3 += (global_luck2-25)
		global_luck2 = 25
	if global_luck3 > 25:
		saved_TGL += (global_luck3-25)
		global_luck3 = 25
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def Tgg():
	pygame.mixer.music.pause()
	stopped = True
	rest_lev_fsr()
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 460
		y = 120
		print_Text("THANKS FOR YOUR LUCK", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 200
		print_Text("NOW WE DON'T NEED YOU", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 290
		print_Text("ANYMORE", x, y, font_size=60)
		x = display_width - 200
		y = display_height - 200
		print_Text("PRESS ESC", x, y)
		pygame.display.update()
		clock.tick(15)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.mixer.music.unpause()
			show_menu()
def rest_lev_fsr():
	global first_start_recognizer, level_1_intro_n, level_2_intro_n, level_3_intro_n, level_4_intro_n, level_5_intro_n, \
		level_6_intro_n, level_7_intro_n, level_8_intro_n, level_9_intro_n, level_10_intro_n, level_11_intro_n, \
		level_12_intro_n, level_13_intro_n, level_14_intro_n, level_15_intro_n, level_number
	first_start_recognizer = 1
	level_1_intro_n = 1
	level_2_intro_n = 1
	level_3_intro_n = 1
	level_4_intro_n = 1
	level_5_intro_n = 1
	level_6_intro_n = 1
	level_7_intro_n = 1
	level_8_intro_n = 1
	level_9_intro_n = 1
	level_10_intro_n = 1
	level_11_intro_n = 1
	level_12_intro_n = 1
	level_13_intro_n = 1
	level_14_intro_n = 1
	level_15_intro_n = 1
	level_number = 1
def Twin():
	pygame.mixer.music.pause()
	stopped = True
	rest_lev_fsr()
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 460
		y = 120
		print_Text("YOU ARE TOO LUCKY. ", x, y,  font_size=60)
		x = display_width / 2 - 460
		y = 200
		print_Text("WE CAN'T USE YOU", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 290
		print_Text("ANYMORE", x, y, font_size=60)
		x = display_width - 200
		y = display_height - 200
		print_Text("PRESS ESC", x, y)
		pygame.display.update()
		clock.tick(15)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.mixer.music.unpause()
			show_menu()
def TTwin():
	pygame.mixer.music.pause()
	stopped = True
	rest_lev_fsr()
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		x = display_width / 2 - 460
		y = 120
		print_Text("YOU ARE GOD OF LUCK ", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 200
		print_Text("NOW YOU ARE MY", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 290
		print_Text("FAVORITE SOUL", x, y, font_size=60)
		x = display_width - 200
		y = display_height - 200
		print_Text("PRESS ESC", x, y)
		pygame.display.update()
		clock.tick(15)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.mixer.music.unpause()
			show_menu()
def cho_rand_char():
	global p
	p = random.randint(1, 3)
	cho_cha()
def cho_cha():
	if p == 1:
		rand_char()
	else:
		rand_char2()
def rand_char():
	global TGL, walkLeft, walkRight, playerStand
	if 0 < TGL <= 20:
		walkLeft = [pygame.image.load("character_image/LC1.png"), pygame.image.load("character_image/LO1.png")]
		walkRight = [pygame.image.load("character_image/RC1.png"), pygame.image.load("character_image/RO1.png")]
		playerStand = [pygame.image.load("character_image/DMO1.png"), pygame.image.load("character_image/DMC1.png")]
	elif 20 < TGL <= 40:
		walkLeft = [pygame.image.load("character_image/LC2.png"), pygame.image.load("character_image/LO2.png")]
		walkRight = [pygame.image.load("character_image/RC2.png"), pygame.image.load("character_image/RO2.png")]
		playerStand = [pygame.image.load("character_image/DMO2.png"), pygame.image.load("character_image/DMC2.png")]
	elif 40 < TGL <= 60:
		walkLeft = [pygame.image.load("character_image/LC3.png"), pygame.image.load("character_image/LO3.png")]
		walkRight = [pygame.image.load("character_image/RC3.png"), pygame.image.load("character_image/RO3.png")]
		playerStand = [pygame.image.load("character_image/DMO3.png"), pygame.image.load("character_image/DMC3.png")]
	elif 60 < TGL <= 80:
		walkLeft = [pygame.image.load("character_image/LC4.png"), pygame.image.load("character_image/LO4.png")]
		walkRight = [pygame.image.load("character_image/RC4.png"), pygame.image.load("character_image/RO4.png")]
		playerStand = [pygame.image.load("character_image/DMO4.png"), pygame.image.load("character_image/DMC4.png")]
	else:
		walkLeft = [pygame.image.load("character_image/LC5.png"), pygame.image.load("character_image/LO5.png")]
		walkRight = [pygame.image.load("character_image/RC5.png"), pygame.image.load("character_image/RO5.png")]
		playerStand = [pygame.image.load("character_image/DMO5.png"), pygame.image.load("character_image/DMC5.png")]
def rand_char_lvl_8():
	global TGL_lvl_8, walkLeft, walkRight, playerStand2
	if 0 < TGL_lvl_8 <= 20:
		playerStand2 = [pygame.image.load("character_image/DMO1.png"), pygame.image.load("character_image/DMC1.png")]
	elif 20 < TGL_lvl_8 <= 40:
		playerStand2 = [pygame.image.load("character_image/DMO2.png"), pygame.image.load("character_image/DMC2.png")]
	elif 40 < TGL_lvl_8 <= 60:
		playerStand2 = [pygame.image.load("character_image/DMO3.png"), pygame.image.load("character_image/DMC3.png")]
	elif 60 < TGL_lvl_8 <= 80:
		playerStand2 = [pygame.image.load("character_image/DMO4.png"), pygame.image.load("character_image/DMC4.png")]
	else:
		playerStand2 = [pygame.image.load("character_image/DMO5.png"), pygame.image.load("character_image/DMC5.png")]
def rand_char2():
	global walkLeft, walkRight, playerStand
	RC = random.randint(1, 5)
	if RC == 1:
		walkLeft = [pygame.image.load("character_image/LC1.png"), pygame.image.load("character_image/LO1.png")]
		walkRight = [pygame.image.load("character_image/RC1.png"), pygame.image.load("character_image/RO1.png")]
		playerStand = [pygame.image.load("character_image/DMO1.png"), pygame.image.load("character_image/DMC1.png")]
	elif RC == 2:
		walkLeft = [pygame.image.load("character_image/LC2.png"), pygame.image.load("character_image/LO2.png")]
		walkRight = [pygame.image.load("character_image/RC2.png"), pygame.image.load("character_image/RO2.png")]
		playerStand = [pygame.image.load("character_image/DMO2.png"), pygame.image.load("character_image/DMC2.png")]
	elif RC == 3:
		walkLeft = [pygame.image.load("character_image/LC3.png"), pygame.image.load("character_image/LO3.png")]
		walkRight = [pygame.image.load("character_image/RC3.png"), pygame.image.load("character_image/RO3.png")]
		playerStand = [pygame.image.load("character_image/DMO3.png"), pygame.image.load("character_image/DMC3.png")]
	elif RC == 4:
		walkLeft = [pygame.image.load("character_image/LC4.png"), pygame.image.load("character_image/LO4.png")]
		walkRight = [pygame.image.load("character_image/RC4.png"), pygame.image.load("character_image/RO4.png")]
		playerStand = [pygame.image.load("character_image/DMO4.png"), pygame.image.load("character_image/DMC4.png")]
	else:
		walkLeft = [pygame.image.load("character_image/LC5.png"), pygame.image.load("character_image/LO5.png")]
		walkRight = [pygame.image.load("character_image/RC5.png"), pygame.image.load("character_image/RO5.png")]
		playerStand = [pygame.image.load("character_image/DMO5.png"), pygame.image.load("character_image/DMC5.png")]
def level_quantity():
	global difficult_multiplier, left_level_quantity
	if difficult_multiplier == 1:
		left_level_quantity = random.randint(6, 10)
	elif difficult_multiplier == 2:
		left_level_quantity = random.randint(8, 12)
	else:
		left_level_quantity = random.randint(11, 15)
def dif_easy():
	global difficult_multiplier, level_number
	level_number = 1
	difficult_multiplier = 1
	level_quantity()
	start_New_game2()
def dif_easy1():
	global difficult_multiplier, level_lives, pause_lim, first_start_recognizer, level_number
	first_start_recognizer += 1
	level_lives = random.randint(5, 7)
	pause_lim = random.randint(10, 15)
	difficult_multiplier = 1
	level_number = 1
	level_quantity()
	start_New_game()
def dif_normal():
	global difficult_multiplier, level_number
	level_number = 1
	difficult_multiplier = 2
	level_quantity()
	start_New_game2()
def dif_normal1():
	global difficult_multiplier, level_lives, first_start_recognizer, level_number, pause_lim
	level_number = 1
	pause_lim = random.randint(7, 15)
	first_start_recognizer += 1
	level_lives = random.randint(3, 5)
	pause_lim = random.randint(13, 18)
	difficult_multiplier = 2
	level_quantity()
	start_New_game()
def dif_hard():
	global difficult_multiplier, level_number
	level_number = 1
	difficult_multiplier = 3
	level_quantity()
	start_New_game2()
def dif_hard1():
	global difficult_multiplier, level_lives, first_start_recognizer, level_number, pause_lim
	level_number = 1
	first_start_recognizer += 1
	level_lives = random.randint(1, 3)
	pause_lim = random.randint(17, 19)
	difficult_multiplier = 3
	level_quantity()
	start_New_game()
def GL_reset():
	global global_luck, global_luck2, global_luck3, character_colour3, TGL, GL, GL2, GL3
	global_luck = random.randint(0, 24)
	global_luck2 = random.randint(0, 24)
	global_luck3 = random.randint(0, 24)
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	saved_TGL = 0
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
	character_colour3 = (GL, GL2, GL3)
def skip_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	first_start_recognizer = 5
	choose_difficult1()
def intro1():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 1:
		first_start_recognizer += 1
		stopped = True
		pygame.mixer.Sound.play(in1)
		skip_introstart_btn = Button(190, 70)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("GREETINGS, YOUR SOUL", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("HAS BEEN SUMMONED TO", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("THIS WORLD FOR", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("ENLIGHTENMENT", x, y, font_size=60)
			skip_introstart_btn.draw(660, 435, "SKIP", skip_intro, 50)
			back2_btn.draw(660, 525, "NEXT", intro1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro2()
def intro2():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 2:
		first_start_recognizer += 1
		stopped = True
		pygame.mixer.Sound.play(in2)
		skip_introstart_btn = Button(190, 70)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("OUR CREATOR WAS SO", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("GENEROUS TO YOU THAT", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("HE CREATED THE WHOLE", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("WORLD JUST FOR YOU", x, y, font_size=60)
			skip_introstart_btn.draw(660, 435, "SKIP", skip_intro, 50)
			back2_btn.draw(660, 525, "NEXT", intro1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro3()
def intro3():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 3:
		first_start_recognizer += 1
		stopped = True
		pygame.mixer.Sound.play(in3)
		skip_introstart_btn = Button(190, 70)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("I AM ITS CREATION, I AM", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("APPOINTED TO GUIDE YOU", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("AND HELP YOU COPE WITH", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("ALL TROUBLES", x, y, font_size=60)
			skip_introstart_btn.draw(660, 435, "SKIP", skip_intro, 50)
			back2_btn.draw(660, 525, "NEXT", intro1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro4()
def intro4():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 4:
		first_start_recognizer += 1
		stopped = True
		pygame.mixer.Sound.play(in4)
		skip_introstart_btn = Button(190, 70)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("AND YES, DON'T WORRY,", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOUR VISION IS OKAY,", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("IT'S JUST THAT YOUR", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("SOUL ISN'T STRONG", x, y, font_size=60)
			skip_introstart_btn.draw(660, 435, "SKIP", skip_intro, 50)
			back2_btn.draw(660, 525, "NEXT", intro1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro5()
def intro5():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 5:
		stopped = True
		pygame.mixer.Sound.play(in5)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("THE FIRST STEP FOR", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOU IS TO CHOOSE THE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("DIFFICULTY OF YOUR SOUL", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("TRAINING", x, y, font_size=60)
			back2_btn.draw(660, 525, "NEXT", choose_difficult1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro6()
def intro6():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 6:
		stopped = True
		pygame.mixer.Sound.play(in6)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("I HAVE ALREADY TOLD", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOU WHAT YOU NEED TO", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("KNOW, YOU CAN START", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("TRAINING", x, y, font_size=60)
			back2_btn.draw(660, 525, "NEXT", choose_difficult1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro7()
def intro7():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 7:
		stopped = True
		pygame.mixer.Sound.play(in7)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("I DON'T LIKE THE FACT", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOU HAVEN'T COMPLETED", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("YOUR ENLIGHTENMENT", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("FEEL CONSEQUENCES", x, y, font_size=60)
			back2_btn.draw(660, 525, "NEXT", choose_difficult2, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		intro8()
def intro8():
	pygame.mixer.music.pause()
	stop_sound()
	global first_start_recognizer
	if first_start_recognizer == 8:
		stopped = True
		pygame.mixer.Sound.play(in8)
		back2_btn = Button(190, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("I DON'T LIKE THE FACT", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOU HAVEN'T COMPLETED", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("YOUR ENLIGHTENMENT", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("LAST WARNING", x, y, font_size=60)
			back2_btn.draw(660, 525, "NEXT", choose_difficult3, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		quit()
def level_finished_check_for_Tgg():
	if TGL < 1:
		Tgg()
	elif TGL > 99:
		Twin()
	else:
		intro_for_choose_difficult()
def intro_for_choose_difficult():
	pygame.mixer.music.pause()
	stop_sound()
	pygame.mixer.Sound.play(in9)
	stopped = True
	back2_btn = Button(190, 70)
	menu3_btn = Button(190, 70)
	while stopped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		display.fill((0, 0, 0))
		display.blit(creation, (-120, 320))
		x = display_width / 2 - 460
		y = 120
		print_Text("YOU COMPLETE LEVELS,", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 200
		print_Text("BUT YOUR SOUL IS STILL", x, y, font_size=60)
		x = display_width / 2 - 460
		y = 280
		print_Text("WEAK, YOU NEED TO HAVE", x, y, font_size=60)
		x = display_width / 2 - 280
		y = 360
		print_Text("ONE MORE TRAINING", x, y, font_size=60)
		back2_btn.draw(660, 525, "NEXT", choose_difficult, 50)
		menu3_btn.draw(660, 615, "MENU", show_menu, 50)
		pygame.display.update()
		clock.tick(15)
def level_checker():
	pygame.mixer.music.play(-1)
	stop_sound()
	global left_level_quantity, level_number
	if left_level_quantity > 0:
		if level_number == 1:
			level_1_intro()
		elif level_number == 2:
			level_2_intro()
		elif level_number == 3:
			level_3_intro()
		elif level_number == 4:
			level_4_intro()
		elif level_number == 5:
			level_5_intro()
		elif level_number == 6:
			level_6_intro()
		elif level_number == 7:
			level_7_intro()
		elif level_number == 8:
			level_8_intro()
		elif level_number == 9:
			level_9_intro()
		elif level_number == 10:
			level_10_intro()
		elif level_number == 11:
			level_11_intro()
		elif level_number == 12:
			level_12_intro()
		elif level_number == 13:
			level_13_intro()
		elif level_number == 14:
			level_14_intro()
		elif level_number == 15:
			level_15_intro()
	else:
		level_finished_check_for_Tgg()
def M1TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck -= 1
	if global_luck < 1:
		global_luck2 += global_luck
		global_luck = 0
	if global_luck2 < 1:
		global_luck3 += global_luck2
		global_luck2 = 0
	if global_luck3 < 1:
		saved_TGL += global_luck3
		global_luck3 = 0
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def M2TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck -= 2
	if global_luck < 1:
		global_luck2 += global_luck
		global_luck = 0
	if global_luck2 < 1:
		global_luck3 += global_luck2
		global_luck2 = 0
	if global_luck3 < 1:
		saved_TGL += global_luck3
		global_luck3 = 0
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def M3TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck -= 3
	if global_luck < 1:
		global_luck2 += global_luck
		global_luck = 0
	if global_luck2 < 1:
		global_luck3 += global_luck2
		global_luck2 = 0
	if global_luck3 < 1:
		saved_TGL += global_luck3
		global_luck3 = 0
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def P1TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck += 1
	if global_luck > 25:
		global_luck2 += (global_luck - 25)
		global_luck = 25
	if global_luck2 > 25:
		global_luck3 += (global_luck2 - 25)
		global_luck2 = 25
	if global_luck3 > 25:
		saved_TGL += (global_luck3 - 25)
		global_luck3 = 25
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def P2TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck += 2
	if global_luck > 25:
		global_luck2 += (global_luck - 25)
		global_luck = 25
	if global_luck2 > 25:
		global_luck3 += (global_luck2 - 25)
		global_luck2 = 25
	if global_luck3 > 25:
		saved_TGL += (global_luck3 - 25)
		global_luck3 = 25
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def P3TGL():
	global TGL, global_luck, global_luck2, global_luck3, GL, GL2, GL3, character_colour3, saved_TGL
	global_luck += 3
	if global_luck > 25:
		global_luck2 += (global_luck - 25)
		global_luck = 25
	if global_luck2 > 25:
		global_luck3 += (global_luck2 - 25)
		global_luck2 = 25
	if global_luck3 > 25:
		saved_TGL += (global_luck3 - 25)
		global_luck3 = 25
	GL = global_luck * 10
	GL2 = global_luck2 * 10
	GL3 = global_luck3 * 10
	character_colour3 = (GL, GL2, GL3)
	TGL = global_luck + global_luck2 + global_luck3 + saved_TGL
def level_1():
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_2_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			x = display_width / 2 - 230
			y = 20
			print_Text("I LEVEL", x, y, font_size=100)
			TGL_DISP()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, " ", lvl1, 50)
			LVL_1_2_btn.draw(670, 140, " ", lvl1, 50)
			LVL_1_3_btn.draw(260, 430, " ", lvl1, 50)
			LVL_1_4_btn.draw(670, 430, " ", lvl1, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def nothing():
	pass
def M1live():
	global level_lives
	level_lives -= 1
def lvl1():
	if difficult_multiplier == 1:
		t = random.randint(1, 4)
		if t == 1:
			M1TGL()
		elif t == 2:
			M1TGL()
		elif t == 3:
			M1live()
		else:
			win()
	elif difficult_multiplier == 2:
		t = random.randint(1, 5)
		if t == 1:
			M2TGL()
		elif t == 2:
			M2TGL()
		elif t == 3:
			M1live()
		elif t == 4:
			nothing()
		else:
			win()
	else:
		t = random.randint(1, 6)
		if t == 1:
			M3TGL()
		elif t == 2:
			M3TGL()
		elif t == 3:
			M1live()
		elif t == 4:
			nothing()
		elif t == 5:
			M1live()
		else:
			win()
def level_2():
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			TGL_DISP()
			OVSC2_draw()
			OVSC3_draw()
			x = display_width / 2 - 230
			y = 20
			print_Text("II LEVEL", x, y, font_size=100)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			check_collision_lvl_2()
			KeyP3()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def check_collision_lvl_2():
	if user_y + user_height >= obstacle2_y:
		if obstacle2_x + 2000 >= user_x:
			gg2()
		else:
			pass
	if user_y + user_height >= obstacle3_y:
		if obstacle3_x <= user_x + user_width:
			win()
		else:
			pass
def set_default_position():
	global user_x, obstacle5_x, obstacle4_x, obstacle_x, user_y, make_jump, jump_counter, obstacle2_x, obstacle9_x, \
		obstacle9_y, obstacle8_x, obstacle8_y, obstacle7_x, obstacle6_x, obstacle7_y, obstacle6_y, cooldown_bullet, \
		obstacle10_x, obstacle10_y, obstacle11_x, obstacle11_y, obstacle12_x, obstacle12_y, obstacle13_x, obstacle13_y,\
		quant_of_bul
	pygame.mixer.music.unpause()
	stop_sound()
	cooldown_bullet = 0
	quant_of_bul = 0
	obstacle2_x = -2000
	obstacle_x = display_width - 230
	user_y = display_height - user_height - 100
	user_x = 100
	all_btn_bullets = []
	obstacle4_x = display_width - 530
	obstacle5_x = 70
	obstacle6_x = display_width / 2
	obstacle6_y = display_height - obstacle6_height - 130
	obstacle7_x = (display_width - 150) / 2 - 115
	obstacle7_y = 0
	obstacle8_x = display_width - obstacle8_width
	obstacle8_y = -600
	obstacle9_x = 0
	obstacle9_y = 0
	obstacle10_x = display_width + 100
	obstacle10_y = display_height - obstacle10_height - 100
	obstacle11_x = display_width + 200
	obstacle11_y = display_height - obstacle11_height - 100
	obstacle12_x = - 650
	obstacle12_y = display_height - obstacle12_height - 100
	obstacle13_x = - 800
	obstacle13_y = display_height - obstacle13_height - 100
	obstacle14_x = display_width - 500
	obstacle14_y = display_height - obstacle14_height - 100
	make_jump = False
	jump_counter = 30
def level_3():
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			TGL_DISP()
			OVSC1_draw()
			if difficult_multiplier == 2:
				OVSC4_draw()
			if difficult_multiplier == 3:
				OVSC4_draw()
				OVSC5_draw()
			OVSC3_draw()
			x = display_width / 2 - 230
			y = 20
			print_Text("III LEVEL", x, y, font_size=100)
			KeyP()
			check_collision_lvl_3()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def check_collision_lvl_3():
	if user_y + user_height >= obstacle_y:
		if obstacle_x <= user_x <= obstacle_x + obstacle_width:
			gg2()
		elif obstacle_x <= user_x + user_width <= obstacle_x + obstacle_width:
			gg2()
	if difficult_multiplier >= 2:
		if user_y + user_height >= obstacle4_y:
			if obstacle4_x <= user_x <= obstacle4_x + obstacle4_width:
				gg2()
			elif obstacle4_x <= user_x + user_width <= obstacle4_x + obstacle4_width:
				gg2()
	if difficult_multiplier == 3:
		if user_y + user_height >= obstacle5_y:
			if obstacle5_x <= user_x <= obstacle5_x + obstacle5_width:
				gg2()
			elif obstacle5_x <= user_x + user_width <= obstacle5_x + obstacle5_width:
				gg2()
	if user_y + user_height >= obstacle3_y:
		if obstacle3_x <= user_x + user_width:
			win()
		else:
			pass
def level_4():
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			display.blit(enemy5_img, (930, 494))
			if user_x + user_width > 930:
				if difficult_multiplier == 1:
					P23 = random.randint(1, 3)
					if P23 == 1:
						win()
					else:
						M1TGL()
						level_4()
				if difficult_multiplier == 2:
					P23 = random.randint(1, 5)
					if P23 == 1:
						win()
					else:
						M1TGL()
						level_4()
				if difficult_multiplier == 3:
					P23 = random.randint(1, 7)
					if P23 == 1:
						win()
					else:
						M1TGL()
						level_4()
			KeyP()
			x = display_width / 2 - 230
			y = 20
			print_Text("IV LEVEL", x, y, font_size=100)
			TGL_DISP()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def check_collision_lvl_12():
	if obstacle14_x < user_x + user_width:
		win3()
def level_5():
	set_default_position()
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_2_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			LVL_1_1_btn.draw(260, 140, " ", level_5_1, 50)
			LVL_1_2_btn.draw(670, 140, " ", level_5_2, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_5_3, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_5_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			KeyP2()
			show_health()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_T5_1():
	set_default_position()
	LVL_1_1_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 2)
		if p15 == 1:
			win()
		elif p15 == 2:
			gg2()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 3)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 4)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			TGL_DISP()
			LVL_1_1_btn.draw(260, 140, " ", win, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_T5_2():
	set_default_position()
	LVL_1_2_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 2)
		if p15 == 1:
			win()
		elif p15 == 2:
			gg2()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 3)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 4)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_2_btn.draw(670, 140, " ", win, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_T5_3():
	set_default_position()
	LVL_1_3_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 2)
		if p15 == 1:
			win()
		elif p15 == 2:
			gg2()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 3)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 4)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_3_btn.draw(260, 430, " ", win, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_T5_4():
	set_default_position()
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 2)
		if p15 == 1:
			win()
		elif p15 == 2:
			gg2()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 3)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 4)
		if p15 == 1:
			win()
		elif p15 > 2:
			gg2()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_4_btn.draw(670, 430, " ", win, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_1():
	set_default_position()
	LVL_1_2_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(2, 8)
		if p15 == 2:
			win()
		elif p15 == 3:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(2, 12)
		if p15 == 2:
			win()
		elif p15 > 9:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(2, 16)
		if p15 == 2:
			win()
		elif p15 > 12:
			M1live()
		else:
			M1TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_2_btn.draw(670, 140, " ", level_5_1_1, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_5_1_2, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_5_1_3, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_1_1():
	set_default_position()
	LVL_1_3_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_3_btn.draw(260, 430, " ", level_T5_3, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_T5_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_1_2():
	set_default_position()
	LVL_1_2_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_2_btn.draw(670, 140, " ", level_T5_2, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_T5_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_1_3():
	set_default_position()
	LVL_1_2_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_2_btn.draw(670, 140, " ", level_T5_2, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_T5_3, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_2_3():
	set_default_position()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, " ", level_T5_1, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_T5_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_3_4():
	set_default_position()
	LVL_1_2_btn = Button(150, 150)
	LVL_1_1_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_2_btn.draw(670, 140, " ", level_T5_2, 50)
			LVL_1_1_btn.draw(260, 140, " ", level_T5_1, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_2_4():
	set_default_position()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(1, 6)
		if p15 == 1:
			win()
		elif p15 == 2:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(1, 9)
		if p15 == 1:
			win()
		elif p15 > 7:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(1, 12)
		if p15 == 1:
			win()
		elif p15 > 8:
			M1live()
		else:
			M2TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, " ", level_T5_1, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_T5_3, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_2():
	set_default_position()
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(2, 8)
		if p15 == 2:
			win()
		elif p15 == 3:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(2, 12)
		if p15 == 2:
			win()
		elif p15 > 9:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(2, 16)
		if p15 == 2:
			win()
		elif p15 > 12:
			M1live()
		else:
			M1TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, " ", level_5_1_1, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_5_2_3, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_5_2_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_3():
	set_default_position()
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_2_btn = Button(150, 150)
	LVL_1_4_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(2, 8)
		if p15 == 2:
			win()
		elif p15 == 3:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(2, 12)
		if p15 == 2:
			win()
		elif p15 > 9:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(2, 16)
		if p15 == 2:
			win()
		elif p15 > 12:
			M1live()
		else:
			M1TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, " ", level_5_1_2, 50)
			LVL_1_2_btn.draw(670, 140, " ", level_5_2_3, 50)
			LVL_1_4_btn.draw(670, 430, " ", level_5_3_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_5_4():
	set_default_position()
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 150)
	LVL_1_2_btn = Button(150, 150)
	LVL_1_3_btn = Button(150, 150)
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p15 = random.randint(2, 8)
		if p15 == 2:
			win()
		elif p15 == 3:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 2:
		p15 = random.randint(2, 12)
		if p15 == 2:
			win()
		elif p15 > 9:
			M1live()
		else:
			M1TGL()
	if difficult_multiplier == 3:
		p15 = random.randint(2, 16)
		if p15 == 2:
			win()
		elif p15 > 12:
			M1live()
		else:
			M1TGL()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			LVL_1_1_btn.draw(260, 140, " ", level_5_1_3, 50)
			LVL_1_2_btn.draw(670, 140, " ", level_5_2_4, 50)
			LVL_1_3_btn.draw(260, 430, " ", level_5_3_4, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			KeyP2()
			show_health()
			y = 20
			print_Text("V LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_6():
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			TGL_DISP()
			OVSC6_draw()
			if difficult_multiplier > 1:
				OVSC7_draw()
			OVSC8_draw()
			OVSC9_draw()
			show_health()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("VI LEVEL", x, y, font_size=100)
			KeyP()
			check_collision_lvl_6()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def check_collision_lvl_6():
	if user_x < obstacle9_x + obstacle9_width:
		if obstacle9_y + obstacle9_height > user_y > obstacle9_y:
			gg2()
		elif obstacle9_y < user_y + user_height < obstacle9_y + obstacle9_height:
			gg2()
		elif user_y < obstacle9_y < user_y + user_height:
			gg2()
	if user_x > display_width - obstacle8_width:
		if obstacle8_y + obstacle8_height > user_y > obstacle8_y:
			gg2()
		elif obstacle8_y < user_y + user_height < obstacle8_y + obstacle8_height:
			gg2()
		elif user_y < obstacle8_y < user_y + user_height:
			gg2()
	if (obstacle7_x < user_x < obstacle7_x + obstacle7_width) or (obstacle7_x < user_x + user_width < obstacle7_x + obstacle7_width):
		if obstacle7_y + obstacle7_height > user_y > obstacle7_y:
			gg2()
		elif obstacle7_y < user_y + user_height < obstacle7_y + obstacle7_height:
			gg2()
		elif user_y < obstacle7_y < user_y + user_height:
			gg2()
	if (obstacle6_x < user_x < obstacle6_x + obstacle6_width) or \
			(obstacle6_x < user_x + user_width < obstacle6_x + obstacle6_width) or \
			(user_x > obstacle6_x > user_x + user_width):
		if obstacle6_y + obstacle6_height > user_y > obstacle6_y:
			lvl_6_apple()
		elif obstacle6_y < user_y + user_height < obstacle6_y + obstacle6_height:
			lvl_6_apple()
		elif user_y < obstacle6_y < user_y + user_height:
			lvl_6_apple()
		elif user_y < obstacle6_y + obstacle6_height < user_y + user_height:
			lvl_6_apple()
def lvl_6_apple():
	global obstacle6_y, obstacle6_x
	p1 = display_height - 100 - obstacle6_height
	p2 = p1 - 100
	p6 = p2 - 100
	k1 = random.randint(p2, p1)
	k2 = random.randint(p6, p2)
	c1 = 0
	c2 = 360 - obstacle6_width
	c3 = c2 * 2 + obstacle6_width
	c4 = display_width - obstacle6_width
	l1 = random.randint(c1, c2)
	l2 = random.randint(c2, c3)
	l3 = random.randint(c3, c4)
	p3 = random.randint(1, 2)
	p5 = random.randint(1, 3)
	if difficult_multiplier == 1:
		p4 = random.randint(1, 15)
		if p4 == 1:
			win()
		else:
			if p3 == 1:
				obstacle6_y = k1
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
			if p3 == 2:
				obstacle6_y = k2
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
	if difficult_multiplier == 2:
		p4 = random.randint(1, 30)
		if p4 == 1:
			win()
		else:
			if p3 == 1:
				obstacle6_y = k1
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
			if p3 == 2:
				obstacle6_y = k2
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
	if difficult_multiplier == 3:
		p4 = random.randint(1, 45)
		if p4 == 1:
			win()
		else:
			if p3 == 1:
				obstacle6_y = k1
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
			if p3 == 2:
				obstacle6_y = k2
				if p5 == 1:
					obstacle6_x = l1
				if p5 == 2:
					obstacle6_x = l2
				if p5 == 3:
					obstacle6_x = l3
def level_7():
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_1_1_btn = Button(150, 60)
	LVL_1_2_btn = Button(200, 60)
	LVL_1_3_btn = Button(225, 60)
	LVL_1_4_btn = Button(250, 60)
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			x = display_width / 2 - 230
			y = 20
			print_Text("VII LEVEL", x, y, font_size=100)
			TGL_DISP()
			KeyP2()
			LVL_1_1_btn.draw(260, 140, "KILL", KILL, 50)
			LVL_1_2_btn.draw(670, 140, "SAVE", SAVE, 50)
			LVL_1_3_btn.draw(260, 430, "AGREE", AGREE, 50)
			LVL_1_4_btn.draw(670, 430, "ESCAPE", lvl_skip, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def KILL():
	p20 = random.randint(1, 9)
	if p20 == 1:
		win()
	elif p20 == 2:
		M1TGL()
		M1live()
	elif p20 > 5:
		M1TGL()
def SAVE():
	p20 = random.randint(1, 10)
	if p20 == 1:
		win()
	elif p20 == 2:
		win()
	elif p20 > 5:
		M1TGL()
		M1live()
def AGREE():
	p20 = random.randint(1, 10)
	if p20 == 1:
		win()
	elif p20 == 2:
		win()
	elif p20 == 3:
		win()
	elif p20 > 3:
		M3TGL()
		M1live()
def level_8():
	set_default_position()
	global TGL_lvl_8
	if difficult_multiplier == 1:
		TGL_lvl_8 = random.randint(1, 75)
	if difficult_multiplier == 2:
		TGL_lvl_8 = random.randint(1, 100)
	if difficult_multiplier == 3:
		TGL_lvl_8 = random.randint(20, 100)
	rand_char_lvl_8()
	LVL_skip_btn = Button(325, 65)
	LVL_1_1_btn = Button(200, 65)
	LVL_1_2_btn = Button(150, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			TGL_DISP()
			KDM2()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("VIII LEVEL", x, y, font_size=100)
			KeyP()
			LVL_1_1_btn.draw(260, 140, "FIGHT", fight_lvl_8, 50)
			LVL_1_2_btn.draw(670, 140, "RUN", run_lvl_8, 50)
			show_health()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def fight_lvl_8():
	if TGL > TGL_lvl_8:
		if difficult_multiplier == 1:
			p10 = random.randint(1, 7)
			if p10 == 1:
				win()
			else:
				level_8()
		if difficult_multiplier == 2:
			p10 = random.randint(1, 12)
			if p10 == 1:
				win()
			else:
				level_8()
		if difficult_multiplier == 3:
			p10 = random.randint(1, 15)
			if p10 == 1:
				win()
			else:
				level_8()
	else:
		M1live()
		if difficult_multiplier == 1:
			level_8()
		if difficult_multiplier == 2:
			M1TGL()
			level_8()
		if difficult_multiplier == 3:
			M2TGL()
			level_8()
def run_lvl_8():
	if TGL <= TGL_lvl_8:
		if difficult_multiplier == 1:
			p10 = random.randint(1, 9)
			if p10 == 1:
				win()
			elif p10 > 5:
				M1TGL()
				level_8()
			else:
				level_8()
		if difficult_multiplier == 2:
			p10 = random.randint(1, 13)
			if p10 == 1:
				win()
			elif p10 > 8:
				M1TGL()
				level_8()
			else:
				level_8()
		if difficult_multiplier == 3:
			p10 = random.randint(1, 17)
			if p10 == 1:
				win()
			elif p10 > 10:
				M1TGL()
				level_8()
			else:
				level_8()
	else:
		M1live()
		if difficult_multiplier == 1:
			level_8()
		if difficult_multiplier == 2:
			M1TGL()
			level_8()
		if difficult_multiplier == 3:
			M2TGL()
			level_8()
def level_9():
	global p17
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p17 = random.randint(4, 10)
	if difficult_multiplier == 1:
		p17 = random.randint(8, 14)
	if difficult_multiplier == 1:
		p17 = random.randint(12, 18)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			TGL_DISP()
			OVSC10_draw()
			if difficult_multiplier > 1:
				OVSC11_draw()
			OVSC12_draw()
			if difficult_multiplier > 1:
				OVSC13_draw()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("IX LEVEL", x, y, font_size=100)
			KeyP5()
			show_health()
			check_collision_lvl_9()
			if quant_of_bul == p17:
				win()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def check_collision_lvl_9():
	if (obstacle10_x < user_x < obstacle10_x + obstacle10_width) or \
			(obstacle10_x < user_x + user_width < obstacle10_x + obstacle10_width) or \
			(user_x > obstacle10_x > user_x + user_width):
		if obstacle10_y + obstacle10_height > user_y > obstacle10_y:
			gg2()
		elif obstacle10_y < user_y + user_height < obstacle10_y + obstacle10_height:
			gg2()
		elif user_y < obstacle10_y < user_y + user_height:
			gg2()
		elif user_y < obstacle10_y + obstacle10_height < user_y + user_height:
			gg2()
	if (obstacle11_x < user_x < obstacle11_x + obstacle11_width) or \
			(obstacle11_x < user_x + user_width < obstacle11_x + obstacle11_width) or \
			(user_x > obstacle11_x > user_x + user_width):
		if obstacle11_y + obstacle11_height > user_y > obstacle11_y:
			gg2()
		elif obstacle11_y < user_y + user_height < obstacle11_y + obstacle11_height:
			gg2()
		elif user_y < obstacle11_y < user_y + user_height:
			gg2()
		elif user_y < obstacle11_y + obstacle11_height < user_y + user_height:
			gg2()
	if (obstacle12_x < user_x < obstacle12_x + obstacle6_width) or \
			(obstacle12_x < user_x + user_width < obstacle12_x + obstacle12_width) or \
			(user_x > obstacle12_x > user_x + user_width):
		if obstacle12_y + obstacle12_height > user_y > obstacle12_y:
			gg2()
		elif obstacle12_y < user_y + user_height < obstacle12_y + obstacle12_height:
			gg2()
		elif user_y < obstacle12_y < user_y + user_height:
			gg2()
		elif user_y < obstacle12_y + obstacle12_height < user_y + user_height:
			gg2()
	if (obstacle13_x < user_x < obstacle13_x + obstacle13_width) or \
			(obstacle13_x < user_x + user_width < obstacle13_x + obstacle13_width) or \
			(user_x > obstacle13_x > user_x + user_width):
		if obstacle13_y + obstacle13_height > user_y > obstacle13_y:
			gg2()
		elif obstacle13_y < user_y + user_height < obstacle13_y + obstacle13_height:
			gg2()
		elif user_y < obstacle13_y < user_y + user_height:
			gg2()
		elif user_y < obstacle13_y + obstacle13_height < user_y + user_height:
			gg2()
def level_10():
	global user_x, user_y
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	LVL_10_4_btn = Button(450, 55)
	user_y = display_height - user_height - 100
	user_x = 100
	levelt = True
	set_waiting_time_lvl_10()
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			LVL_10_4_btn.draw(display_width / 2 - 225, display_height / 2 - 43, "REDUCE TIME", time_reduce, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip2, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			decriase_time()
			if waiting_time_lvl_10 < 1:
				win()
			show_health()
			#show_waiting_time_lvl_10()
			y = 20
			print_Text("X LEVEL", x, y, font_size=100)
			KeyP4()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def show_waiting_time_lvl_10():
	x = display_width - 80
	y = 250
	print_Text(str(waiting_time_lvl_10), x, y)
	x = display_width - 80
	y = 300
	print_Text(str(waiting_time_lvl_10/60), x, y)
def decriase_time():
	global waiting_time_lvl_10
	waiting_time_lvl_10 -= 1
def set_waiting_time_lvl_10():
	global waiting_time_lvl_10
	if difficult_multiplier == 1:
		waiting_time_lvl_10 = random.randint(300, 1500)
	if difficult_multiplier == 2:
		waiting_time_lvl_10 = random.randint(600, 3000)
	if difficult_multiplier == 3:
		waiting_time_lvl_10 = random.randint(1200, 4500)
def time_reduce():
	global waiting_time_lvl_10
	if difficult_multiplier == 1:
		M3TGL()
		waiting_time_lvl_10 -= random.randint(0, 300)
		M1live()
	if difficult_multiplier == 2:
		M3TGL()
		waiting_time_lvl_10 -= random.randint(0, 400)
		M1live()
	if difficult_multiplier == 3:
		M2TGL()
		waiting_time_lvl_10 -= random.randint(0, 500)
		M1live()
def level_11():
	set_default_position()
	global TGL_lvl_8, attack_amount_lvl, jump_amount
	jump_amount = random.randint(1, 6)
	if difficult_multiplier == 1:
		TGL_lvl_8 = random.randint(1, 75)
	if difficult_multiplier == 2:
		TGL_lvl_8 = random.randint(1, 100)
	if difficult_multiplier == 3:
		TGL_lvl_8 = random.randint(20, 100)
	rand_char_lvl_8()
	LVL_skip_btn = Button(325, 65)
	LVL_1_1_btn = Button(275, 65)
	attack_amount_lvl = random.randint(1, 30)
	set_waiting_time_lvl_10()
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			TGL_DISP()
			KDM2()
			OVSC10_draw()
			OVSC11_draw()
			OVSC12_draw()
			if difficult_multiplier > 2:
				OVSC13_draw()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip2, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("XI LEVEL", x, y, font_size=100)
			KeyP()
			LVL_1_1_btn.draw(260, 140, "ATTACK", attack_amount, 50)
			show_health()
			check_collision_lvl_9()
			if waiting_time_lvl_10 < 1:
				gg2()
			decriase_time()
			if jump_amount < 1:
				gg2()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def attack_amount():
	global attack_amount_lvl, jump_amount
	attack_amount_lvl -= 1
	jump_amount -= 1
	if attack_amount_lvl < 1:
		win()
def level_12():
	global p17
	set_default_position()
	LVL_skip_btn = Button(325, 65)
	if difficult_multiplier == 1:
		p17 = random.randint(12, 20)
	if difficult_multiplier == 1:
		p17 = random.randint(16, 24)
	if difficult_multiplier == 1:
		p17 = random.randint(20, 28)
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			display.blit(creation, (580, 120))
			TGL_DISP()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip2, 60)
			x = display_width / 2 - 230
			y = 20
			print_Text("XII LEVEL", x, y, font_size=100)
			KeyP6()
			show_health()
			check_collision_lvl_9()
			if quant_of_bul == p17:
				ultimate()
			if waiting_time_lvl_10 < 1:
				ultimate()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def ultimate():
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			display.blit(creation, (580, 120))
			TGL_DISP()
			x = display_width / 2 - 230
			y = 20
			print_Text("XV LEVEL", x, y, font_size=100)
			KDM()
			OVSC14_draw()
			show_health()
			check_collision_lvl_12()
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def level_13():
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_skip_btn = Button(325, 65)
	LVL_1_4_btn = Button(540, 60)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			KeyP2()
			LVL_1_4_btn.draw(display_width / 2 - 270, display_height / 2 - 60, "BELIEVE IN LUCK", believe, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip2, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			show_health()
			y = 20
			print_Text("XIII LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def believe():
	p1 = random.randint(1, int(TGL))
	if p1 == TGL:
		win()
	else:
		p2 = random.randint(1, 15)
		if p2 == 1:
			M1live()
		else:
			pass
		M1TGL()
def level_14():
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_skip_btn = Button(325, 65)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			KeyP2()
			y = 20
			print_Text("XIV LEVEL", x, y, font_size=100)
			overcoming()
			pygame.display.update()
			clock.tick(1)
		else:
			return gg()
def overcoming():
	while True:
		if TGL > 7:
			p16 = random.randint(7, TGL)
			if p16 == 7:
				win()
			else:
				M1TGL()
		else:
			M1TGL()
def level_15():
	pygame.mixer.music.unpause()
	stop_sound()
	LVL_skip_btn = Button(325, 65)
	LVL_1_3_btn = Button(280, 60)
	LVL_1_4_btn = Button(450, 60)
	levelt = True
	while levelt:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		global level_lives
		if TGL < 1:
			Tgg()
		elif TGL > 99:
			Twin()
		elif level_lives > 0:
			display.fill((0, 0, 0))
			show_health()
			KeyP2()
			LVL_1_3_btn.draw(display_width / 2 - 140, display_height / 2 + 60, "DONATE", donate, 50)
			LVL_1_4_btn.draw(display_width / 2 - 225, display_height / 2 - 60, "PASS THIS LVL", win2, 50)
			LVL_skip_btn.draw(display_width - 345, display_height - 80, "SKIP LVL", lvl_skip2, 60)
			x = display_width / 2 - 230
			TGL_DISP()
			y = 20
			print_Text("XV LEVEL", x, y, font_size=100)
			pygame.display.update()
			clock.tick(60)
		else:
			return gg()
def donate():
	M1TGL()
	h = random.randint(1, 5)
	if h == 1:
		M1live()
	j = random.randint(1, 10000)
	if j == 666:
		TTwin()
def level_1_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_1_intro_n
	if level_1_intro_n == 1:
		level_1_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv1)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("LET'S START SIMPLE,", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("YOU NEED TO GUESS", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("THE CORRECT BUTTON", x, y, font_size=60)
			level_btn.draw(660, 525, "I LVL", level_1, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_1()
def level_2_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_2_intro_n
	if level_2_intro_n == 1:
		level_2_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv2)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("NOW YOU HAVE TO LEARN", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("TO MOVE. OVERCOME THE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("ROOM IN THE ALLOTTED", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("TIME", x, y, font_size=60)
			level_btn.draw(660, 525, "II LVL", level_2, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_2()
def level_3_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_3_intro_n
	if level_3_intro_n == 1:
		level_3_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv3)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("NOW TRY TO LEARN", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("HOW TO JUMP WELL.", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("GET OVER THE ", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("OBSTACLES", x, y, font_size=60)
			level_btn.draw(660, 525, "III LVL", level_3, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_3()
def level_4_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_4_intro_n
	if level_4_intro_n == 1:
		level_4_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv4)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("LET'S CHECK YOUR MIND.", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("NOW YOU WILL BE TESTED", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("BY THE SPHINX OF ", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("OMNISCIENCE", x, y, font_size=60)
			level_btn.draw(660, 525, "IV LVL", level_4, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_4()
def level_5_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_5_intro_n
	if level_5_intro_n == 1:
		level_5_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv5)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("TEST OF CHOICE. YOU", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("WILL BE SUBJECT TO", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("PRESSURE FROM", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("UNKNOWING", x, y, font_size=60)
			level_btn.draw(660, 525, "V LVL", level_5, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_5()
def level_6_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_6_intro_n
	if level_6_intro_n == 1:
		level_6_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv6)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("AGAIN, THE TEST OF", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("MOTION CONTROL. WATCH", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("OUT FOR THE SKY FALLING", x, y, font_size=60)
			level_btn.draw(660, 525, "VI LVL", level_6, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_6()
def level_7_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_7_intro_n
	if level_7_intro_n == 1:
		level_7_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv7)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("STRENGTHENING MORALITY", x, y, font_size=58)
			x = display_width / 2 - 460
			y = 200
			print_Text("DIFFICULT CHOICES WILL", x, y, font_size=58)
			x = display_width / 2 - 460
			y = 280
			print_Text("HARDEN YOUR NERVES", x, y, font_size=58)
			level_btn.draw(660, 525, "VII LVL", level_7, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_7()
def level_8_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_8_intro_n
	if level_8_intro_n == 1:
		level_8_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv8)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("FIGHT OR RUN. MAKE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("ONLY BALANCED AND", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("CORRECT DECISIONS", x, y, font_size=60)
			level_btn.draw(660, 525, "VIII LVL", level_8, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_8()
def level_9_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_9_intro_n
	if level_9_intro_n == 1:
		level_9_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv9)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("REAL BATTLE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("USE WHAT YOU HAVE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("LEARNED AND K", x, y, font_size=60)
			level_btn.draw(660, 525, "IX LVL", level_9, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_9()
def level_10_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_10_intro_n
	if level_10_intro_n == 1:
		level_10_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv10)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("PATIENCE. JUST DON'T", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("DO ANYTHING, IS THAT", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("EASY? YOU CAN REDUCE", x, y, font_size=60)
			x = display_width / 2 - 280
			y = 360
			print_Text("WAITING TIME BY ***", x, y, font_size=60)
			level_btn.draw(660, 525, "X LVL", level_10, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_10()
def level_11_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_11_intro_n
	if level_11_intro_n == 1:
		level_11_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv11)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("DEFEAT ANOTHER", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("CREATURE CALLED FOR", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 280
			print_Text("INITIATION", x, y, font_size=60)
			level_btn.draw(660, 525, "XI LVL", level_11, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_11()
def level_12_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_12_intro_n
	if level_12_intro_n == 1:
		level_12_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv12)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("KNOW THE HOPELESSNESS", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("FIGHT A PART OF ME", x, y, font_size=60)
			level_btn.draw(660, 525, "XII LVL", level_12, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_12()
def level_13_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_13_intro_n
	if level_13_intro_n == 1:
		level_13_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv13)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("BELIEVE IN LUCK", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("MAKE IT A PART OF YOU", x, y, font_size=60)
			level_btn.draw(660, 525, "XIII LVL", level_13, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_13()
def level_14_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_14_intro_n
	if level_14_intro_n == 1:
		level_14_intro_n += 1
		stopped = True
		pygame.mixer.Sound.play(lv14)
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("OVERCOMING YOURSELF", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("ASCENSION", x, y, font_size=60)
			level_btn.draw(660, 525, "XIV LVL", level_14, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_14()
def level_15_intro():
	pygame.mixer.music.pause()
	stop_sound()
	global level_15_intro_n
	if level_15_intro_n == 1:
		level_15_intro_n += 1
		pygame.mixer.Sound.play(lv15)
		stopped = True
		level_btn = Button2(210, 70)
		menu3_btn = Button(190, 70)
		while stopped:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			display.fill((0, 0, 0))
			display.blit(creation, (-120, 320))
			x = display_width / 2 - 460
			y = 120
			print_Text("HOW DID YOU MANAGE", x, y, font_size=60)
			x = display_width / 2 - 460
			y = 200
			print_Text("TO REACH THIS LEVEL?", x, y, font_size=60)
			level_btn.draw(660, 525, "XV LVL", level_15, 50)
			menu3_btn.draw(660, 615, "MENU", show_menu, 50)
			pygame.display.update()
			clock.tick(15)
	else:
		level_15()

show_menu()
pygame.quit()
quit()