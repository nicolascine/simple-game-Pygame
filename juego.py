import pygame

def main():
	pygame.init()
	pantalla = pygame.display.set_mode([500,500])
	pygame.display.set_caption(" Mi primer juego en python :) ")
	salir = False
	reloj1 = pygame.time.Clock()

	#colores ~
	blanco = (255,255,255)
	rojo = (200,20,50)
	azul = (10,20,244)
	verde = (127,255,0)

	#superficies
	s1 = pygame.Surface((100,150))
	s2 = pygame.Surface([50,50])
	

	#Formas -> rectangulos
	r1 = pygame.Rect(390,150,10,45)
	
	#coloreado de superficies y formas
	s1.fill(rojo)
	s2.fill(azul)

	while salir != True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir = True


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					r1 = r1.move(-10,0)
				if event.key == pygame.K_RIGHT:
					r1 = r1.move(10,0)
				if event.key == pygame.K_DOWN:
					r1 = r1.move(0,10)
				if event.key == pygame.K_UP:
					r1 = r1.move(0,-10)

		
		reloj1.tick(20) #fijo a 20fps
		
		pantalla.fill(blanco)

		#display de superficies y formas
		pantalla.blit(s1, [50, 70])
		pantalla.blit(s2, [50, 60])

		#draw~
		pygame.draw.rect(pantalla, verde, r1)

		pygame.display.update()

	pygame.quit()



main()