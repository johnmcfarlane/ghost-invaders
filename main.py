spacePlane = sprites.create(img("""
        . . . . . . . c d . . . . . . .
                     . . . . . . . c d . . . . . . .
                     . . . . . . . c d . . . . . . .
                     . . . . . . . c b . . . . . . .
                     . . . . . . . f f . . . . . . .
                     . . . . . . . c 6 . . . . . . .
                     . . . . . . . f f . . . . . . .
                     . . . . . . . 8 6 . . . . . . .
                     . . . . . . 8 8 9 8 . . . . . .
                     . . . . . . 8 6 9 8 . . . . . .
                     . . . . . c c c 8 8 8 . . . . .
                     . . . . 8 8 6 6 6 9 8 8 . . . .
                     . . 8 f f f c c e e f f 8 8 . .
                     . 8 8 8 8 8 8 6 6 6 6 9 6 8 8 .
                     8 8 8 8 8 8 8 8 6 6 6 9 6 6 8 8
                     8 8 8 8 8 8 8 8 6 6 6 6 9 6 8 8
    """),
    SpriteKind.player)
spacePlane.set_position(80, 120)
spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(5)
controller.move_sprite(spacePlane, 200, 200)

def on_a_pressed():
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . c b a c . . . . . .
                                . . . . c c b c f a c . . . . .
                                . . . . a f b b b a c . . . . .
                                . . . . a f f b a f c c . . . .
                                . . . . c b b a f f c . . . . .
                                . . . . . b b a f a . . . . . .
                                . . . . . . c b b . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
                                . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        0,
        -100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def bogeySpeed():
    return 10 + info.score() / 30
wave_countdown: number = 0

def on_update_interval():
    global wave_countdown
    wave_countdown = wave_countdown - bogeySpeed()
    if wave_countdown > 0:
        return
    wave_countdown = wave_countdown + 1000
    x = randint(20, 30)
    while x < 141:
        bogey = sprites.create(img("""
                ........................
                                        ........................
                                        ........................
                                        ........................
                                        ..........ffff..........
                                        ........ff1111ff........
                                        .......fb111111bf.......
                                        .......f11111111f.......
                                        ......fd11111111df......
                                        ......fd11111111df......
                                        ......fddd1111dddf......
                                        ......fbdbfddfbdbf......
                                        ......fcdcf11fcdcf......
                                        .......fb111111bf.......
                                        ......fffcdb1bdffff.....
                                        ....fc111cbfbfc111cf....
                                        ....f1b1b1ffff1b1b1f....
                                        ....fbfbffffffbfbfbf....
                                        .........ffffff.........
                                        ...........fff..........
                                        ........................
                                        ........................
                                        ........................
                                        ........................
            """),
            SpriteKind.enemy)
        bogey.set_velocity(0, bogeySpeed())
        bogey.set_position(x, -10)
        x += 20
game.on_update_interval(1, on_update_interval)

def on_on_overlap(spacePlane, bogey):
    bogey.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(dart, bogey):
    bogey.destroy()
    dart.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)
