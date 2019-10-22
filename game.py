import functions
import minimax

if __name__ == '__main__':
    b = functions.Board()
    gamer = -1 if input('Human first? [Y/n] ').upper() == 'N' else 1
    print('Human: X, Tree: O\n')

    while True:
        if gamer == 1:
            b.draw()
            go = input('  -> ')
        else:
            # go = minimax.british_museum(b, gamer, True)
            # go = minimax.alpha_beta(b, None, gamer, True)
            go = minimax.alpha_beta_symmetry(b, None, gamer, True)
            print(f'     {go} <-')

        b.go(gamer, go)
        state = b.win_state()
        if state:
            b.draw()
            print(state, 'wins.')
            break
        else:
            gamer *= -1
