from queue import PriorityQueue
import pygame

class Djikstra:
    

    def h(self,p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self,came_from, current, draw):
        
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()


    def algorithm(self,draw, grid, start, end):
        count = 0
        visited = PriorityQueue()
        visited.put((0, count, start))
        came_from = {}
        weight = {spot: float("inf") for row in grid for spot in row}
        weight[start] = 0
    

        visited_hash = {start}

        while not visited.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = visited.get()[2]
            visited_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                

                if weight[current] < weight[neighbor]:
                    came_from[neighbor] = current
                    # weight[neighbor] = temp_weight
                    weight[neighbor] =  self.h(neighbor.get_pos(), current.get_pos())
                    if neighbor not in visited_hash:
                        count += 1
                        visited.put((weight[neighbor], count, neighbor))
                        visited_hash.add(neighbor)
                        neighbor.make_open()

            draw()

            if current != start:
                current.make_closed()

        return False
