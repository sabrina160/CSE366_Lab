import pygame
import sys
from agent import Agent
from environment import Environment 

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 150)
AGENT_COLOR = (0, 0, 0) 
TEXT_COLOR = (0, 0, 0)
FONT_SIZE = 25

def main():
    pygame.init() 
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Agent Simulation")
    clock = pygame.time.Clock() 
    font = pygame.font.Font(None, FONT_SIZE)
    movement_direction='idle' 

    env = Environment(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    agent = Agent(env, x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT // 2) 
    running = True
    while running:
        clock.tick(60)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Get the keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            agent.move("left")
            movement_direction='Moving Left'
        if keys[pygame.K_RIGHT]:
            agent.move("right")
            movement_direction='Moving Right'
        if keys[pygame.K_UP]:
            agent.move("up")
            movement_direction='Moving Up'
        if keys[pygame.K_DOWN]:
            agent.move("down")
            movement_direction='Moving Down'


        # Fill the screen background
        screen.fill(BACKGROUND_COLOR)

        # Draw the agent
        agent_x, agent_y = agent.get_position()
        #pygame.draw.rect(screen, AGENT_COLOR, (agent_x, agent_y, 30, 30))
        
        pygame.draw.circle(screen, AGENT_COLOR, (agent_x, agent_y),10)

        # Display the agent's position
        position_text = f"Position: {int(agent_x)}, {int(agent_y)}"
        text_surface = font.render(position_text, True, TEXT_COLOR)
        screen.blit(text_surface, (10, 10))
        
        direction_surface = font.render(movement_direction, True, TEXT_COLOR)
        screen.blit(direction_surface, (10, 50))
        # Flip the display. 
        pygame.display.flip()

    # Quit Pygame properly
    pygame.quit()
    sys.exit()

if __name__ == "__main__": 
    main() 
