import pygame
import sys
from pygame.locals import QUIT

def main():
    # Инициализация Pygame
    pygame.init()
    
    # Установка размеров окна и создание поверхности для отображения
    DISPLAYSURF = pygame.display.set_mode((1600, 900))
    
    # Установка заголовка окна
    pygame.display.set_caption('КРУТАЯ ПРОГРАММА')
    
    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:  # Проверка на событие выхода
                pygame.quit()  # Завершение Pygame
                sys.exit()     # Выход из программы

        # Сюда вставляем код, если хотим отрисовать объект до обновления экрана
        DISPLAYSURF.fill((255, 255, 255))  # Заполнение фона белым цветом
        pygame.draw.circle(DISPLAYSURF, (255, 200, 100), (500, 300), 100)  # Рисуем красный круг
        # Обновление экрана с текущими отрисованными объектами
        pygame.display.update()
        
        # Сюда вставляем код, если хотим отрисовать объект после обновления экрана

# Запуск функции main при выполнении скрипта
if __name__ == "__main__":
    main()