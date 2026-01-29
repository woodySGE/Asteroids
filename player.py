from circleshape import *
from constants import *
from shot import shot

class Player(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
    rotation = 0
    rapid_fire = False
    Timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.PLAYER_SHOOT_COOLDOWN_SECONDS += dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.rapid_fire == True:
            bullet = shot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.math.Vector2(0,1)
            direction = direction.rotate(self.rotation)

            bullet.velocity = direction * PLAYER_SHOOT_SPEED
        else:
            if self.PLAYER_SHOOT_COOLDOWN_SECONDS >= 0.3:
                bullet = shot(self.position.x, self.position.y, SHOT_RADIUS)
                direction = pygame.math.Vector2(0,1)
                direction = direction.rotate(self.rotation)

                bullet.velocity = direction * PLAYER_SHOOT_SPEED
                self.PLAYER_SHOOT_COOLDOWN_SECONDS = 0
            else:
                self.PLAYER_SHOOT_COOLDOWN_SECONDS = self.PLAYER_SHOOT_COOLDOWN_SECONDS



        


        