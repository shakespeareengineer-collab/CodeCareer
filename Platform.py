import pygame as pg
pg.init()


# Window Dimensions
width, height = 1000, 800


# Window Creation
WIN = pg.display.set_mode((width, height))
pg.display.set_caption("PYTHON _- _ PLATFORMER")


# Player Settings
PLAYER_width, PLAYER_height = 55, 75
Player_X = width // 2 - PLAYER_width // 2
Player_Y = height- PLAYER_height
PlayerVel = 1
player = pg.Rect(Player_X, Player_Y, PLAYER_width, PLAYER_height)
player_x = float(Player_X)
player_y = float(Player_Y)


def movement():
	global player, PlayerVel, player_x, player_y
	key = pg.key.get_pressed()
	if key[pg.K_a] and player.x > 0:
		player_x -= PlayerVel
	if key[pg.K_d] and player.x < width - PLAYER_width:
		player_x += PlayerVel
	if key[pg.K_s] and player.y < height - PLAYER_height:
		player_y += PlayerVel
	if key[pg.K_w] and player.y > 0:
		player_y -= PlayerVel
	if key[pg.K_LSHIFT]:
		PlayerVel = 2
	else:
		PlayerVel = 1
	if key[pg.K_LCTRL]:
		new_height = 55
		PlayerVel = 0.25
	else:
		new_height = 75
	if player.height != new_height:
		player_y = player_y + player.height - new_height
		player.height = new_height
	player.x = int(player_x)
	player.y = int(player_y)

def draw(player):
	WIN.fill((255, 30, 30))
	pg.draw.rect(WIN, (150, 255, 0), player, border_top_left_radius=PLAYER_width//4, border_top_right_radius=PLAYER_width//4)
	pg.display.flip()
clock = pg.time.Clock()
def main():
	global WIN
	global width, height
	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			elif event.type == pg.KEYUP:
				if event.key == pg.K_ESCAPE:
					running = False
				elif event.key == pg.K_EQUALS:
					width += 5
					height += 5
					WIN = pg.display.set_mode((width, height))
				elif event.key == pg.K_MINUS:
					width = max(400, width - 5)
					height = max(300, height - 5)
					WIN = pg.display.set_mode((width, height))

		movement()
		draw(player)
		clock.tick(120)
	pg.quit()
main()