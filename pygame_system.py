import pygame
import sys

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)

# メイン処理をする関数
def main():
    # pygameモジュールの初期化
    pygame.init()
    pygame.display.set_caption("初めてのpygame")
    # スクリーンの初期化
    screen = pygame.display.set_mode((800, 600))
    # クロックオブジェクトの作成
    clock = pygame.time.Clock()
    # フォントオブジェクトの作成
    font = pygame.font.Font(None, 80)

    # タイマー変数の初期化
    tmr = 0

    # ずっと
    while True:
        tmr = tmr + 1
        # pygameのイベントを繰り返しで処理する
        for event in pygame.event.get():
            # もしバツボタンがクリックされたら
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        txt = font.render(str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt, [300, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()


