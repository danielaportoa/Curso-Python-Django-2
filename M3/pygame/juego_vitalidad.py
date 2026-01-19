import random
import sys
import pygame

# -----------------------
# Config
# -----------------------
WIDTH, HEIGHT = 800, 600
CELL = 20
FPS = 12

MAX_HEALTH = 30
START_HEALTH = 12
WIN_HEALTH = 30

DANGER_DAMAGE = 4
ENERGY_HEAL = 3

DANGER_COUNT = 6

# -----------------------
# Helpers
# -----------------------
def rand_cell_pos(exclude=set()):
    """Return a random grid position (x, y) that isn't in exclude."""
    cols = WIDTH // CELL
    rows = HEIGHT // CELL
    while True:
        x = random.randint(0, cols - 1) * CELL
        y = random.randint(0, rows - 1) * CELL
        if (x, y) not in exclude:
            return (x, y)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

# -----------------------
# Game
# -----------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Vitalidad Runner (pygame) - Vida 0 = Game Over")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 22)
    big = pygame.font.SysFont("consolas", 44)

    # Player (a short "snake" tail)
    direction = (CELL, 0)  # start moving right
    head = (WIDTH // 2 // CELL * CELL, HEIGHT // 2 // CELL * CELL)
    body = [head, (head[0] - CELL, head[1]), (head[0] - 2 * CELL, head[1])]
    body_len = len(body)

    health = START_HEALTH
    score = 0

    # Spawn energy & dangers
    occupied = set(body)
    energy = rand_cell_pos(occupied)

    dangers = []
    occupied = set(body)
    occupied.add(energy)
    for _ in range(DANGER_COUNT):
        dangers.append(rand_cell_pos(occupied))
        occupied.add(dangers[-1])

    paused = False
    game_over = False
    win = False

    def reset():
        nonlocal direction, head, body, body_len, health, score, energy, dangers, paused, game_over, win
        direction = (CELL, 0)
        head = (WIDTH // 2 // CELL * CELL, HEIGHT // 2 // CELL * CELL)
        body = [head, (head[0] - CELL, head[1]), (head[0] - 2 * CELL, head[1])]
        body_len = len(body)
        health = START_HEALTH
        score = 0

        occupied = set(body)
        energy = rand_cell_pos(occupied)

        dangers = []
        occupied = set(body)
        occupied.add(energy)
        for _ in range(DANGER_COUNT):
            dangers.append(rand_cell_pos(occupied))
            occupied.add(dangers[-1])

        paused = False
        game_over = False
        win = False

    while True:
        # -----------------------
        # Events
        # -----------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_p:
                    paused = not paused

                if event.key == pygame.K_r:
                    reset()

                if not game_over and not win:
                    # Movement: prevent instant reverse into yourself
                    if event.key in (pygame.K_LEFT, pygame.K_a) and direction != (CELL, 0):
                        direction = (-CELL, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-CELL, 0):
                        direction = (CELL, 0)
                    elif event.key in (pygame.K_UP, pygame.K_w) and direction != (0, CELL):
                        direction = (0, -CELL)
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -CELL):
                        direction = (0, CELL)

        if paused:
            clock.tick(10)
            # Draw paused screen
            screen.fill((10, 12, 18))
            txt = big.render("PAUSA (P)", True, (220, 220, 220))
            screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2 - 60))
            tip = font.render("R = reiniciar | ESC = salir", True, (180, 180, 180))
            screen.blit(tip, (WIDTH // 2 - tip.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            continue

        # -----------------------
        # Update
        # -----------------------
        if not game_over and not win:
            # Move
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # Wrap around edges (more forgiving than game over)
            if new_head[0] < 0:
                new_head = (WIDTH - CELL, new_head[1])
            elif new_head[0] >= WIDTH:
                new_head = (0, new_head[1])

            if new_head[1] < 0:
                new_head = (new_head[0], HEIGHT - CELL)
            elif new_head[1] >= HEIGHT:
                new_head = (new_head[0], 0)

            head = new_head
            body.insert(0, head)
            body = body[:body_len]

            # Self-collision costs health
            if head in body[1:]:
                health -= 2
                # knockback: shorten a bit
                body_len = max(3, body_len - 1)

            # Danger collision
            if head in dangers:
                health -= DANGER_DAMAGE
                # Move that danger elsewhere
                occupied = set(body)
                for d in dangers:
                    occupied.add(d)
                occupied.discard(head)
                # relocate the one we hit
                idx = dangers.index(head)
                dangers[idx] = rand_cell_pos(occupied)

            # Energy pickup
            if head == energy:
                score += 1
                health = clamp(health + ENERGY_HEAL, 0, MAX_HEALTH)
                body_len = min(body_len + 1, 40)  # grow a bit for fun

                occupied = set(body)
                for d in dangers:
                    occupied.add(d)
                energy = rand_cell_pos(occupied)

            # Win/Lose checks
            if health <= 0:
                game_over = True
            elif health >= WIN_HEALTH:
                win = True

        # -----------------------
        # Draw
        # -----------------------
        screen.fill((10, 12, 18))

        # grid (subtle)
        for x in range(0, WIDTH, CELL):
            pygame.draw.line(screen, (18, 22, 32), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, CELL):
            pygame.draw.line(screen, (18, 22, 32), (0, y), (WIDTH, y))

        # Energy
        pygame.draw.rect(screen, (70, 220, 150), (*energy, CELL, CELL), border_radius=6)

        # Dangers
        for d in dangers:
            pygame.draw.rect(screen, (240, 80, 90), (*d, CELL, CELL), border_radius=6)

        # Player body
        for i, seg in enumerate(body):
            if i == 0:
                pygame.draw.rect(screen, (90, 160, 255), (*seg, CELL, CELL), border_radius=6)
            else:
                pygame.draw.rect(screen, (60, 110, 200), (*seg, CELL, CELL), border_radius=6)

        # UI bar
        ui_bg = pygame.Rect(0, 0, WIDTH, 44)
        pygame.draw.rect(screen, (6, 8, 12), ui_bg)

        health_text = font.render(f"Vida: {health}/{MAX_HEALTH}", True, (235, 235, 235))
        score_text = font.render(f"Puntos: {score}", True, (200, 200, 200))
        tip_text = font.render("WASD/Flechas | P pausa | R reiniciar", True, (150, 150, 150))

        screen.blit(health_text, (14, 11))
        screen.blit(score_text, (200, 11))
        screen.blit(tip_text, (360, 11))

        # Health bar
        bar_w = 180
        bar_h = 14
        bar_x = WIDTH - bar_w - 18
        bar_y = 15
        pygame.draw.rect(screen, (25, 30, 40), (bar_x, bar_y, bar_w, bar_h), border_radius=10)
        fill = int((health / MAX_HEALTH) * bar_w)
        pygame.draw.rect(screen, (70, 220, 150) if health > 8 else (240, 160, 80) if health > 3 else (240, 80, 90),
                         (bar_x, bar_y, fill, bar_h), border_radius=10)

        if game_over:
            msg = big.render("GAME OVER", True, (240, 80, 90))
            sub = font.render("R para reiniciar | ESC para salir", True, (220, 220, 220))
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 60))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2))

        if win:
            msg = big.render("¡GANASTE!", True, (70, 220, 150))
            sub = font.render("Llegaste a la vitalidad meta. R para reiniciar", True, (220, 220, 220))
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 60))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
