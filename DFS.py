
from queue import PriorityQueue
from typing import ChainMap
import pygame

class DFS:

    def __init__(self):
        self.came_from = {}
        self.visited = []
        self.where = []
        
    

    def reconstruct_path(self,came_from, current, draw):
        
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()
        return True


    def algorithm(self,draw,grid,start,end):
        
        current = start

        
        while end not in self.visited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            
            #self.where.append(start)
            self.visited.append(current)
            
            #

            if current == end:
                self.visited.append(end)
                print("gavedit damkashi")
                self.reconstruct_path(self.came_from, end, draw)
                end.make_end()
                
                

        
            

            for neighbor in current.neighbors:
                if neighbor not in self.visited and end not in self.visited:
                    
                    self.came_from[neighbor] = current
                    neighbor.make_open()
                    
                    draw()
                    if current != start:
                        current.make_closed()

                    self.algorithm(draw,grid,neighbor,end)               


            
            
            
         
        print("bozebooo")
            
        return False       


   
