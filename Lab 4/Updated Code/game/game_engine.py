import random
import pygame
from game.rope import Rope
from game.player import Puller


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rope = Rope(width, height)
        self.player = Puller(90, height // 2, (50, 120, 220), "PLAYER (A/D)")
        self.computer = Puller(width - 90, height // 2, (220, 80, 50), "COMPUTER")

        # Task 1: robust A/D state tracking.
        self.last_key = None
        self.held_keys = set()

        self.winner = None
        self.game_state = "PLAYING"

        # Task 2: dynamic computer AI.
        self.computer_pull_cooldown = 180
        self.panic_pull_cooldown = 80
        self.panic_threshold = self.rope.left_win_x + 80
        self.panic_pull_strength = 1.5
        self.last_computer_pull = pygame.time.get_ticks()

        # Task 4: 45-second match timer and sudden death.
        self.match_duration = 45_000
        self.match_start_time = pygame.time.get_ticks()
        self.sudden_death = False
        self.sudden_death_multiplier = 2.0

        self.font_big = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 26)

    def handle_event(self, event):
        if self.game_state == "GAME_OVER":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset()
            return

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_a, pygame.K_d):
                # Track physically held keys so overlapping A/D KEYDOWN/KEYUP
                # events cannot leave the input system permanently locked.
                if event.key not in self.held_keys:
                    self.held_keys.add(event.key)

                    # Preserve the original alternating-input behavior, while
                    # doubling player pull power during sudden death.
                    if event.key != self.last_key:
                        strength = (
                            self.sudden_death_multiplier
                            if self.sudden_death
                            else 1.0
                        )
                        self.rope.pull_left(strength)
                        self.last_key = event.key
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                self.held_keys.discard(event.key)

    def update(self):
        if self.game_state == "GAME_OVER":
            return

        now = pygame.time.get_ticks()

        # Task 4: enter sudden death once 45 seconds have elapsed.
        if not self.sudden_death and now - self.match_start_time >= self.match_duration:
            self.sudden_death = True
            self.game_state = "SUDDEN_DEATH"

        # Task 2: the existing AI keeps its normal/panic cooldown structure.
        in_panic = self.rope.marker_x <= self.panic_threshold
        current_cooldown = (
            self.panic_pull_cooldown if in_panic else self.computer_pull_cooldown
        )

        if now - self.last_computer_pull >= current_cooldown:
            computer_variance = random.uniform(0.7, 1.2)
            pull_strength = computer_variance
            if in_panic:
                pull_strength *= self.panic_pull_strength
            if self.sudden_death:
                pull_strength *= self.sudden_death_multiplier

            self.rope.pull_right(pull_strength)
            self.last_computer_pull = now

        result = self.rope.check_winner()
        if result:
            self.winner = result
            self.game_state = "GAME_OVER"

    def reset(self):
        self.rope.reset()
        self.last_key = None
        self.held_keys.clear()
        self.winner = None
        self.game_state = "PLAYING"
        self.last_computer_pull = pygame.time.get_ticks()

        # Reset the timer and sudden-death state for the new match.
        self.match_start_time = pygame.time.get_ticks()
        self.sudden_death = False

    def render(self, screen):
        screen.fill((30, 32, 36))

        mud_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 80, 240, 160)
        pygame.draw.rect(screen, (45, 38, 30), mud_rect, border_radius=12)

        self.rope.render(screen)

        # Task 3: visual struggle feedback based only on current marker position.
        center_x = self.width / 2
        displacement = self.rope.marker_x - center_x
        max_displacement = max(center_x - self.rope.left_win_x, 1)
        struggle = min(abs(displacement) / max_displacement, 1.0)

        if displacement < 0:
            player_lean = -0.18 * struggle
            computer_lean = 0.0
        elif displacement > 0:
            player_lean = 0.0
            computer_lean = 0.18 * struggle
        else:
            player_lean = 0.0
            computer_lean = 0.0

        self.player.render(screen, lean=player_lean)
        self.computer.render(screen, lean=computer_lean)

        # Live timer at the top. Keep it at 45 seconds after sudden death begins.
        elapsed = min(pygame.time.get_ticks() - self.match_start_time, self.match_duration)
        seconds = elapsed / 1000.0
        timer_text = "SUDDEN DEATH" if self.sudden_death else f"TIME: {seconds:04.1f}s"
        timer_surf = self.font_small.render(timer_text, True, (240, 240, 240))
        screen.blit(timer_surf, (self.width // 2 - timer_surf.get_width() // 2, 10))

        inst_surf = self.font_small.render(
            "Alternate [A] and [D] keys rapidly to pull!", True, (210, 210, 210)
        )
        screen.blit(inst_surf, (self.width // 2 - inst_surf.get_width() // 2, 40))

        if self.game_state == "SUDDEN_DEATH":
            sudden_surf = self.font_small.render(
                "PULLING POWER DOUBLED!", True, (255, 220, 100)
            )
            screen.blit(
                sudden_surf,
                (self.width // 2 - sudden_surf.get_width() // 2, 68)
            )

        if self.game_state == "GAME_OVER":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            win_text = f"{self.winner} WINS!"
            color = (80, 220, 80) if self.winner == "PLAYER" else (240, 80, 80)
            text_surf = self.font_big.render(win_text, True, color)
            screen.blit(
                text_surf,
                (self.width // 2 - text_surf.get_width() // 2, self.height // 2 - 50)
            )

            restart_surf = self.font_small.render(
                "Press [R] to Play Again", True, (240, 240, 240)
            )
            screen.blit(
                restart_surf,
                (self.width // 2 - restart_surf.get_width() // 2, self.height // 2 + 10)
            )
