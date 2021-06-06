import math
import pygame
import xlrd
book = xlrd.open_workbook("file.xls")
sh = book.sheet_by_index(0)

D_WIDHT = 800
D_HEIGHT = 1500

sc = pygame.display.set_mode((D_WIDHT, D_HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
font1 = pygame.font.SysFont('romand', 12)
font2 = pygame.font.SysFont('romand', 24)

clock = pygame.time.Clock()

def draw_graph(arr, offset_y):
	offset_x = 80

	widht = 1
	x_widht = 60
	element = arr[0]
	y_height_k = 150 / element[1]

	text_offset_x = x_widht // 2
	text_offset_y = 20
	text_offset_y_extra = 10

	last_x = 0
	last_y = 0
	for i in range(0, len(arr)):
		element = arr[i]
		x = element[0] * x_widht
		y = -int(element[1] * y_height_k)

		pygame.draw.line(sc, BLACK, (offset_x + last_x, offset_y + last_y), (offset_x + x, offset_y + y), widht)
		pygame.draw.line(sc, BLACK, (offset_x + x, offset_y + y), (offset_x + x, offset_y), widht)
		
		text = font1.render(str(element[1]), 0, BLACK)
		if y - last_y < 3 and x == last_x and i != 0:
			sc.blit(text, (offset_x + x - text_offset_x, offset_y + y - text_offset_y - text_offset_y_extra))
		else:
			sc.blit(text, (offset_x + x - text_offset_x, offset_y + y - text_offset_y))

		text = font1.render(str(element[0] + 1), 0, BLACK)
		sc.blit(text, (offset_x + x - text_offset_x // 2, offset_y + text_offset_y))
		last_x = x
		last_y = y
		
	pygame.draw.line(sc, BLACK, (offset_x, offset_y), (offset_x + x, offset_y), widht)

sc.fill(WHITE)

j = 1
col = 0
on_input_global = True
while on_input_global:
	i = 0
	txt = font2.render(str(sh.cell_value(rowx=i, colx=col)), 0, BLACK)
	i += 1
	sc.blit(txt, (10, 150 + 250 * (j - 1)))
	array = []
	on_input = True
	while on_input:
		xx = sh.cell_value(rowx=i, colx=col)
		if xx == '.':
			on_input = False
		elif xx == '..':
			on_input = False
			on_input_global = False
		else:
			yy = sh.cell_value(rowx=i, colx=(col+1))
			el = [int(xx)-1, int(yy)]
			array.append(el)
		i += 1
	col += 2

	draw_graph(array, 250 * j)
	array.clear()
	j += 1

pygame.display.update()
pygame.image.save(sc, 'graph.png')
pygame.quit()