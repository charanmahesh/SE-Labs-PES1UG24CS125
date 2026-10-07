import math
import pygame


class Rope:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_y = screen_height // 2
        self.marker_x = screen_width // 2

        self.left_win_x = 180
        self.right_win_x = screen_width - 180
        self.pull_step = 12

    def pull_left(self, strength=1.0):
        self.marker_x -= int(self.pull_step * strength)

    def pull_right(self, strength=1.0):
        self.marker_x += int(self.pull_step * strength)

    def check_winner(self):
        if self.marker_x <= self.left_win_x:
            return "PLAYER"
        if self.marker_x >= self.right_win_x:
            return "COMPUTER"
        return None

    def reset(self):
        self.marker_x = float(self.screen_width // 2)
        self.velocity = 0.0

    def render(self, surface):
        # Visual-only tension: the farther the marker moves from center,
        # the more the rope sags and vibrates. Game mechanics are unchanged.
        center_x = self.screen_width / 2
        displacement = self.marker_x - center_x
        tension = min(abs(displacement) / max(center_x - self.left_win_x, 1), 1.0)
        time = pygame.time.get_ticks() / 1000.0

        points = []
        start_x = 60
        end_x = self.screen_width - 60
        segments = 24
        sag = 5 + 14 * tension
        vibration = 1.5 + 3.5 * tension

        for i in range(segments + 1):
            ratio = i / segments
            x = start_x + (end_x - start_x) * ratio
            # Sag is strongest near the middle; vibration increases with tension.
            sag_offset = sag * math.sin(math.pi * ratio)
            wave = vibration * math.sin(time * 18.0 + ratio * 30.0)
            y = self.center_y + sag_offset + wave
            points.append((int(x), int(y)))

        pygame.draw.lines(surface, (180, 140, 90), False, points, 10)

        pygame.draw.line(
            surface,
            (50, 200, 50),
            (self.left_win_x, self.center_y - 40),
            (self.left_win_x, self.center_y + 40),
            4
        )
        pygame.draw.line(
            surface,
            (200, 50, 50),
            (self.right_win_x, self.center_y - 40),
            (self.right_win_x, self.center_y + 40),
            4
        )

        pygame.draw.line(
            surface,
            (120, 120, 120),
            (self.screen_width // 2, self.center_y - 20),
            (self.screen_width // 2, self.center_y + 20),
            2
        )

        flag_rect = pygame.Rect(int(self.marker_x) - 12, self.center_y - 24, 24, 48)
        pygame.draw.rect(surface, (230, 40, 40), flag_rect, border_radius=4)
        pygame.draw.rect(surface, (255, 255, 255), flag_rect, width=2, border_radius=4)