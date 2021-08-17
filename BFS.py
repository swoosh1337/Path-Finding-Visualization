from queue import PriorityQueue
from queue import PriorityQueue
import pygame

class BFS:
    


    def reconstruct_path(self,came_from, current, draw):
        
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()


    def algorithm(self,draw,grid, start, end):
        count = 0
        visited = PriorityQueue()
        visited.put((0, count, start))
        came_from = {}
        
        visited_hash ={None: False} 
  
        queue = []

        queue.append(start)
        
        visited_hash = {start:True}

        while queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            

            current = queue.pop(0)
            #visited_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                return True

            

            for neighbor in current.neighbors:
                if neighbor not in visited_hash:
                    queue.append(neighbor)
                    visited_hash[neighbor] = True                

               
                    came_from[neighbor] = current
                    neighbor.make_open()
                    # weight[neighbor] = temp_weight
            
                    # if neighbor not in visited_hash:
                    #     count += 1
                    #     visited.put((True, count, neighbor))
                    #     visited_hash.add(neighbor)
                    #     neighbor.make_open()

            draw()

            if current != start:
                current.make_closed()

        return False
