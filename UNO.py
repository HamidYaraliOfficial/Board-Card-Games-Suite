import sys
import random
import math
from enum import Enum
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ─── Translations ───────────────────────────────────────────────────────────
TR = {
    'en': {
        'title': 'Board & Card Games',
        'chess': 'Chess',
        'uno': 'UNO',
        'theme': 'Theme',
        'light': 'Light',
        'dark': 'Dark',
        'lang': 'Language',
        'new_game': 'New Game',
        'two_player': '2 Players',
        'vs_ai': 'vs AI',
        'mode': 'Mode',
        'status_chess': 'Chess - Your Turn',
        'check': 'Check!',
        'checkmate': 'Checkmate!',
        'stalemate': 'Stalemate!',
        'white_wins': 'White Wins!',
        'black_wins': 'Black Wins!',
        'draw': 'Draw!',
        'white_turn': "White's Turn",
        'black_turn': "Black's Turn",
        'promote': 'Promote Pawn',
        'uno_title': 'UNO Game',
        'your_hand': 'Your Hand',
        'draw_card': 'Draw Card',
        'players': 'Players',
        'uno_win': 'wins the game!',
        'uno_shout': 'UNO!',
        'choose_color': 'Choose Color',
        'red': 'Red',
        'green': 'Green',
        'blue': 'Blue',
        'yellow': 'Yellow',
        'skip': 'Skip',
        'reverse': 'Reverse',
        'draw2': '+2',
        'draw4': '+4',
        'wild': 'Wild',
        'current_color': 'Current Color',
        'ai_thinking': 'AI Thinking...',
        'player': 'Player',
        'score': 'Score',
        'cards': 'cards',
        'direction': 'Direction',
        'cw': '→ Clockwise',
        'ccw': '← Counter-CW',
    },
    'zh': {
        'title': '桌游与纸牌游戏',
        'chess': '国际象棋',
        'uno': 'UNO纸牌',
        'theme': '主题',
        'light': '浅色',
        'dark': '深色',
        'lang': '语言',
        'new_game': '新游戏',
        'two_player': '双人',
        'vs_ai': '对战AI',
        'mode': '模式',
        'status_chess': '象棋 - 轮到你了',
        'check': '将军！',
        'checkmate': '将死！',
        'stalemate': '和棋！',
        'white_wins': '白方胜！',
        'black_wins': '黑方胜！',
        'draw': '平局！',
        'white_turn': '白方回合',
        'black_turn': '黑方回合',
        'promote': '兵的升变',
        'uno_title': 'UNO游戏',
        'your_hand': '你的手牌',
        'draw_card': '摸牌',
        'players': '玩家',
        'uno_win': '赢得了游戏！',
        'uno_shout': 'UNO！',
        'choose_color': '选择颜色',
        'red': '红',
        'green': '绿',
        'blue': '蓝',
        'yellow': '黄',
        'skip': '跳过',
        'reverse': '反转',
        'draw2': '+2',
        'draw4': '+4',
        'wild': '万能',
        'current_color': '当前颜色',
        'ai_thinking': 'AI思考中...',
        'player': '玩家',
        'score': '分数',
        'cards': '张牌',
        'direction': '方向',
        'cw': '→ 顺时针',
        'ccw': '← 逆时针',
    },
    'fa': {
        'title': 'بازی‌های رومیزی و کارتی',
        'chess': 'شطرنج',
        'uno': 'اونو',
        'theme': 'تم',
        'light': 'روشن',
        'dark': 'تاریک',
        'lang': 'زبان',
        'new_game': 'بازی جدید',
        'two_player': '۲ بازیکن',
        'vs_ai': 'برابر AI',
        'mode': 'حالت',
        'status_chess': 'شطرنج - نوبت شما',
        'check': 'کیش!',
        'checkmate': 'کیش و مات!',
        'stalemate': 'پات!',
        'white_wins': 'سفید برنده شد!',
        'black_wins': 'سیاه برنده شد!',
        'draw': 'مساوی!',
        'white_turn': 'نوبت سفید',
        'black_turn': 'نوبت سیاه',
        'promote': 'ارتقای پیاده',
        'uno_title': 'بازی اونو',
        'your_hand': 'دست شما',
        'draw_card': 'کارت بگیر',
        'players': 'بازیکنان',
        'uno_win': 'برنده شد!',
        'uno_shout': 'اونو!',
        'choose_color': 'رنگ انتخاب کن',
        'red': 'قرمز',
        'green': 'سبز',
        'blue': 'آبی',
        'yellow': 'زرد',
        'skip': 'رد کن',
        'reverse': 'برعکس',
        'draw2': '+۲',
        'draw4': '+۴',
        'wild': 'آزاد',
        'current_color': 'رنگ جاری',
        'ai_thinking': 'AI فکر می‌کند...',
        'player': 'بازیکن',
        'score': 'امتیاز',
        'cards': 'کارت',
        'direction': 'جهت',
        'cw': '← ساعتگرد',
        'ccw': '→ پادساعتگرد',
    }
}

THEMES = {
    'light': {
        'bg': '#F0F0F0',
        'panel': '#FFFFFF',
        'border': '#CCCCCC',
        'text': '#1A1A1A',
        'text2': '#555555',
        'btn': '#4A90D9',
        'btn_text': '#FFFFFF',
        'btn_hover': '#357ABD',
        'btn_active': '#2B6299',
        'accent': '#E8F0FE',
        'chess_light': '#F0D9B5',
        'chess_dark': '#B58863',
        'chess_sel': '#7FC97F',
        'chess_move': '#AAD794',
        'chess_check': '#FF6B6B',
        'highlight': '#3498DB',
        'card_bg': '#FFFFFF',
        'card_shadow': '#AAAAAA',
        'table_bg': '#1B6B3A',
        'table_border': '#145A30',
    },
    'dark': {
        'bg': '#1A1A2E',
        'panel': '#16213E',
        'border': '#0F3460',
        'text': '#E0E0E0',
        'text2': '#AAAAAA',
        'btn': '#0F3460',
        'btn_text': '#E0E0E0',
        'btn_hover': '#1A4A7A',
        'btn_active': '#0A2845',
        'accent': '#0F3460',
        'chess_light': '#4A6741',
        'chess_dark': '#2D4A2A',
        'chess_sel': '#6B9F5E',
        'chess_move': '#5A8A4E',
        'chess_check': '#CC3333',
        'highlight': '#4ECDC4',
        'card_bg': '#1E2D5A',
        'card_shadow': '#0A1020',
        'table_bg': '#0D3320',
        'table_border': '#0A2418',
    }
}

# ─── Chess Engine ────────────────────────────────────────────────────────────
PIECE_SYMBOLS = {
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
}

PIECE_VALUES = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
                'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0}

class ChessEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.',],
            ['.','.','.','.','.','.','.','.',],
            ['.','.','.','.','.','.','.','.',],
            ['.','.','.','.','.','.','.','.',],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R'],
        ]
        self.turn = 'w'
        self.castling = {'wK': True, 'wQ': True, 'bK': True, 'bQ': True}
        self.en_passant = None
        self.halfmove = 0
        self.fullmove = 1
        self.history = []
        self.game_over = False
        self.result = None
        self.in_check = False
        self.promoting = None

    def is_white(self, p): return p.isupper() and p != '.'
    def is_black(self, p): return p.islower() and p != '.'
    def is_enemy(self, p, turn):
        return (self.is_black(p) if turn == 'w' else self.is_white(p))
    def is_friend(self, p, turn):
        return (self.is_white(p) if turn == 'w' else self.is_black(p))
    def in_bounds(self, r, c): return 0 <= r < 8 and 0 <= c < 8

    def raw_moves(self, r, c, board=None, turn=None):
        if board is None: board = self.board
        if turn is None: turn = self.turn
        p = board[r][c]
        if p == '.': return []
        moves = []
        pt = p.upper()

        def add(nr, nc):
            if self.in_bounds(nr, nc):
                tgt = board[nr][nc]
                if tgt == '.' or self.is_enemy(tgt, turn):
                    moves.append((nr, nc))
                    return tgt == '.'
            return False

        def slide(dr, dc):
            nr, nc = r+dr, c+dc
            while self.in_bounds(nr, nc):
                tgt = board[nr][nc]
                if tgt == '.':
                    moves.append((nr, nc))
                elif self.is_enemy(tgt, turn):
                    moves.append((nr, nc)); break
                else: break
                nr += dr; nc += dc

        if pt == 'P':
            d = -1 if turn == 'w' else 1
            start = 6 if turn == 'w' else 1
            if self.in_bounds(r+d, c) and board[r+d][c] == '.':
                moves.append((r+d, c))
                if r == start and board[r+2*d][c] == '.':
                    moves.append((r+2*d, c))
            for dc in [-1, 1]:
                nr, nc = r+d, c+dc
                if self.in_bounds(nr, nc):
                    if self.is_enemy(board[nr][nc], turn):
                        moves.append((nr, nc))
                    elif (nr, nc) == self.en_passant:
                        moves.append((nr, nc))
        elif pt == 'N':
            for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
                add(r+dr, c+dc)
        elif pt == 'B':
            for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]: slide(dr, dc)
        elif pt == 'R':
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: slide(dr, dc)
        elif pt == 'Q':
            for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]:
                slide(dr, dc)
        elif pt == 'K':
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr == 0 and dc == 0: continue
                    add(r+dr, c+dc)
            row = 7 if turn == 'w' else 0
            if r == row and c == 4:
                if self.castling[turn+'K'] and board[row][5]=='.' and board[row][6]=='.' and board[row][7] in ('R','r'):
                    moves.append((row, 6))
                if self.castling[turn+'Q'] and board[row][3]=='.' and board[row][2]=='.' and board[row][1]=='.' and board[row][0] in ('R','r'):
                    moves.append((row, 2))
        return moves

    def find_king(self, turn, board=None):
        if board is None: board = self.board
        k = 'K' if turn == 'w' else 'k'
        for r in range(8):
            for c in range(8):
                if board[r][c] == k: return (r, c)
        return None

    def is_attacked(self, r, c, by_turn, board=None):
        if board is None: board = self.board
        for rr in range(8):
            for cc in range(8):
                p = board[rr][cc]
                if p == '.': continue
                if (by_turn == 'w' and not self.is_white(p)): continue
                if (by_turn == 'b' and not self.is_black(p)): continue
                raw = self.raw_moves(rr, cc, board, by_turn)
                if (r, c) in raw: return True
        return False

    def legal_moves(self, r, c):
        raw = self.raw_moves(r, c)
        legal = []
        p = self.board[r][c]
        for (nr, nc) in raw:
            b2 = [row[:] for row in self.board]
            b2[nr][nc] = b2[r][c]
            b2[r][c] = '.'
            if (nr, nc) == self.en_passant and p.upper() == 'P':
                d = 1 if self.turn == 'w' else -1
                b2[nr+d][nc] = '.'
            king_pos = self.find_king(self.turn, b2)
            if king_pos and not self.is_attacked(king_pos[0], king_pos[1], 'b' if self.turn == 'w' else 'w', b2):
                legal.append((nr, nc))
        return legal

    def apply_move(self, r, c, nr, nc, promote='Q'):
        p = self.board[r][c]
        captured = self.board[nr][nc]
        prev_ep = self.en_passant
        prev_cast = dict(self.castling)

        self.board[nr][nc] = p
        self.board[r][c] = '.'

        if p.upper() == 'P' and (nr, nc) == prev_ep:
            d = 1 if self.turn == 'w' else -1
            self.board[nr+d][nc] = '.'

        if p.upper() == 'P' and abs(nr - r) == 2:
            self.en_passant = ((r + nr) // 2, c)
        else:
            self.en_passant = None

        if p == 'K':
            self.castling['wK'] = False; self.castling['wQ'] = False
            if nc == 6 and c == 4:
                self.board[7][5] = 'R'; self.board[7][7] = '.'
            elif nc == 2 and c == 4:
                self.board[7][3] = 'R'; self.board[7][0] = '.'
        elif p == 'k':
            self.castling['bK'] = False; self.castling['bQ'] = False
            if nc == 6 and c == 4:
                self.board[0][5] = 'r'; self.board[0][7] = '.'
            elif nc == 2 and c == 4:
                self.board[0][3] = 'r'; self.board[0][0] = '.'
        if r == 7 and c == 0: self.castling['wQ'] = False
        if r == 7 and c == 7: self.castling['wK'] = False
        if r == 0 and c == 0: self.castling['bQ'] = False
        if r == 0 and c == 7: self.castling['bK'] = False

        if p == 'P' and nr == 0:
            self.promoting = (nr, nc)
            self.board[nr][nc] = promote.upper()
        elif p == 'p' and nr == 7:
            self.promoting = (nr, nc)
            self.board[nr][nc] = promote.lower()
        else:
            self.promoting = None

        self.turn = 'b' if self.turn == 'w' else 'w'
        king = self.find_king(self.turn)
        opp = 'b' if self.turn == 'w' else 'w'
        self.in_check = self.is_attacked(king[0], king[1], opp) if king else False
        self.check_game_over()

    def check_game_over(self):
        all_legal = []
        for r in range(8):
            for c in range(8):
                p = self.board[r][c]
                if p == '.': continue
                if self.turn == 'w' and not self.is_white(p): continue
                if self.turn == 'b' and not self.is_black(p): continue
                all_legal.extend(self.legal_moves(r, c))
        if not all_legal:
            self.game_over = True
            if self.in_check:
                self.result = 'b' if self.turn == 'w' else 'w'
            else:
                self.result = 'draw'

    def ai_move(self):
        moves = []
        for r in range(8):
            for c in range(8):
                p = self.board[r][c]
                if p == '.': continue
                if self.turn == 'w' and not self.is_white(p): continue
                if self.turn == 'b' and not self.is_black(p): continue
                for (nr, nc) in self.legal_moves(r, c):
                    moves.append((r, c, nr, nc))
        if not moves: return
        best = None; best_score = float('-inf') if self.turn == 'w' else float('inf')
        for mv in moves:
            b2 = [row[:] for row in self.board]
            ep2 = self.en_passant
            turn2 = self.turn
            self.board = [row[:] for row in b2]
            self.apply_move(mv[0], mv[1], mv[2], mv[3])
            score = sum(PIECE_VALUES.get(self.board[r][c], 0)
                        for r in range(8) for c in range(8) if self.board[r][c] != '.')
            if (turn2 == 'w' and score > best_score) or (turn2 == 'b' and score < best_score):
                best_score = score; best = mv
            self.board = [row[:] for row in b2]
            self.en_passant = ep2
            self.turn = turn2
            self.game_over = False; self.result = None; self.in_check = False
        if best:
            self.apply_move(best[0], best[1], best[2], best[3])

# ─── Chess Board Widget ──────────────────────────────────────────────────────
class ChessBoard(QWidget):
    status_changed = pyqtSignal(str)

    def __init__(self, theme_name='light', lang='en', mode='2p'):
        super().__init__()
        self.theme_name = theme_name
        self.lang = lang
        self.mode = mode
        self.engine = ChessEngine()
        self.selected = None
        self.legal = []
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self._do_ai_move)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(300, 300)

    def t(self, key): return TR[self.lang].get(key, key)
    def th(self): return THEMES[self.theme_name]

    def new_game(self, mode=None):
        if mode: self.mode = mode
        self.engine.reset()
        self.selected = None
        self.legal = []
        self.update()
        self._emit_status()

    def _emit_status(self):
        e = self.engine
        t = self.t
        if e.game_over:
            if e.result == 'draw': msg = t('stalemate')
            elif e.result == 'w': msg = t('white_wins')
            else: msg = t('black_wins')
        elif e.in_check:
            msg = t('check') + ' ' + (t('white_turn') if e.turn == 'w' else t('black_turn'))
        else:
            msg = t('white_turn') if e.turn == 'w' else t('black_turn')
        self.status_changed.emit(msg)

    def cell_size(self):
        return min(self.width(), self.height()) // 8

    def board_offset(self):
        cs = self.cell_size()
        bw = cs * 8
        ox = (self.width() - bw) // 2
        oy = (self.height() - bw) // 2
        return ox, oy

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = self.th()
        cs = self.cell_size()
        ox, oy = self.board_offset()
        e = self.engine

        p.fillRect(self.rect(), QColor(th['bg']))

        for r in range(8):
            for c in range(8):
                x = ox + c * cs
                y = oy + r * cs
                light = (r + c) % 2 == 0
                col = QColor(th['chess_light'] if light else th['chess_dark'])

                if self.selected and (r, c) == self.selected:
                    col = QColor(th['chess_sel'])
                elif (r, c) in self.legal:
                    col = QColor(th['chess_move'])
                elif e.in_check and e.board[r][c] in ('K','k'):
                    king_turn = 'K' if e.turn == 'w' else 'k'
                    if e.board[r][c] == king_turn:
                        col = QColor(th['chess_check'])

                p.fillRect(x, y, cs, cs, col)

                piece = e.board[r][c]
                if piece != '.':
                    sym = PIECE_SYMBOLS.get(piece, piece)
                    font_size = max(12, int(cs * 0.72))
                    f = QFont('Segoe UI Symbol', font_size)
                    f.setBold(False)
                    p.setFont(f)
                    is_white_piece = piece.isupper()
                    text_col = QColor('#FFFFFF') if not is_white_piece else QColor('#1A1A1A')
                    shadow_col = QColor('#333333') if is_white_piece else QColor('#AAAAAA')
                    p.setPen(shadow_col)
                    p.drawText(QRect(x+2, y+2, cs, cs), Qt.AlignmentFlag.AlignCenter, sym)
                    p.setPen(text_col)
                    p.drawText(QRect(x, y, cs, cs), Qt.AlignmentFlag.AlignCenter, sym)

        if (r, c) in self.legal:
            pass
        for (r, c) in self.legal:
            x = ox + c * cs; y = oy + r * cs
            if e.board[r][c] != '.':
                pen = QPen(QColor(th['chess_sel']), 3)
                p.setPen(pen)
                p.setBrush(Qt.BrushStyle.NoBrush)
                p.drawRect(x+1, y+1, cs-2, cs-2)
            else:
                dot_c = QColor(th['chess_sel'])
                dot_c.setAlpha(180)
                p.setBrush(dot_c)
                p.setPen(Qt.PenStyle.NoPen)
                r2 = cs // 5
                p.drawEllipse(x + cs//2 - r2, y + cs//2 - r2, r2*2, r2*2)

        border_col = QColor(th['border'])
        p.setPen(QPen(border_col, 2))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRect(ox, oy, cs * 8, cs * 8)

        label_font = QFont('Arial', max(8, cs // 6))
        p.setFont(label_font)
        p.setPen(QColor(th['text2']))
        for i in range(8):
            p.drawText(QRect(ox - cs//2, oy + i*cs, cs//2, cs),
                       Qt.AlignmentFlag.AlignCenter, str(8 - i))
            p.drawText(QRect(ox + i*cs, oy + cs*8, cs, cs//2),
                       Qt.AlignmentFlag.AlignCenter, 'abcdefgh'[i])

    def mousePressEvent(self, event):
        e = self.engine
        if e.game_over: return
        if e.promoting: return
        if self.mode == 'ai' and e.turn == 'b': return

        cs = self.cell_size()
        ox, oy = self.board_offset()
        x = event.position().x() - ox
        y = event.position().y() - oy
        c = int(x // cs); r = int(y // cs)
        if not (0 <= r < 8 and 0 <= c < 8): return

        if self.selected:
            if (r, c) in self.legal:
                p = e.board[self.selected[0]][self.selected[1]]
                if (p == 'P' and r == 0) or (p == 'p' and r == 7):
                    self._do_promote(self.selected[0], self.selected[1], r, c)
                    return
                e.apply_move(self.selected[0], self.selected[1], r, c)
                self.selected = None; self.legal = []
                self.update()
                self._emit_status()
                if self.mode == 'ai' and not e.game_over:
                    self.animation_timer.start(400)
                return
            self.selected = None; self.legal = []

        p = e.board[r][c]
        if p == '.': self.update(); return
        if e.turn == 'w' and not e.is_white(p): self.update(); return
        if e.turn == 'b' and not e.is_black(p): self.update(); return
        self.selected = (r, c)
        self.legal = e.legal_moves(r, c)
        self.update()

    def _do_promote(self, r, c, nr, nc):
        th = self.th()
        d = QDialog(self)
        d.setWindowTitle(self.t('promote'))
        d.setStyleSheet(f"background:{th['panel']}; color:{th['text']};")
        lay = QHBoxLayout(d)
        turn = self.engine.turn
        pieces = ['Q','R','B','N'] if turn == 'w' else ['q','r','b','n']
        for piece in pieces:
            sym = PIECE_SYMBOLS[piece]
            btn = QPushButton(sym)
            btn.setFont(QFont('Segoe UI Symbol', 28))
            btn.setFixedSize(60, 60)
            btn.clicked.connect(lambda _, p2=piece, d2=d: (
                self.engine.apply_move(r, c, nr, nc, p2.upper()),
                self.update(), self._emit_status(), d2.accept(),
                self.selected.__class__ and setattr(self, 'selected', None),
                setattr(self, 'legal', []),
            ))
            lay.addWidget(btn)
        d.exec()
        self.selected = None; self.legal = []
        if self.mode == 'ai' and not self.engine.game_over:
            self.animation_timer.start(400)

    def _do_ai_move(self):
        self.animation_timer.stop()
        self.engine.ai_move()
        self.update()
        self._emit_status()

    def apply_theme(self, theme_name, lang=None):
        self.theme_name = theme_name
        if lang: self.lang = lang
        self.update()

# ─── UNO Engine ──────────────────────────────────────────────────────────────
UNO_COLORS = ['red', 'green', 'blue', 'yellow']
UNO_VALUES = ['0','1','2','3','4','5','6','7','8','9','skip','reverse','draw2']
UNO_WILDS  = ['wild', 'draw4']

class UnoCard:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def is_wild(self): return self.color == 'wild'

    def can_play_on(self, top, current_color):
        if self.is_wild(): return True
        if self.color == current_color: return True
        if self.value == top.value: return True
        return False

    def __repr__(self): return f'{self.color}:{self.value}'

class UnoEngine:
    def __init__(self, num_players=4):
        self.num_players = num_players
        self.reset()

    def reset(self):
        self.deck = self._build_deck()
        random.shuffle(self.deck)
        self.hands = [[] for _ in range(self.num_players)]
        for _ in range(7):
            for i in range(self.num_players):
                self.hands[i].append(self.deck.pop())
        while True:
            top = self.deck.pop()
            if not top.is_wild(): break
            self.deck.insert(0, top)
        self.discard = [top]
        self.current_color = top.color
        self.current_player = 0
        self.direction = 1
        self.game_over = False
        self.winner = None
        self.pending_draw = 0
        self.message = ''
        self.must_draw = False

    def _build_deck(self):
        cards = []
        for color in UNO_COLORS:
            cards.append(UnoCard(color, '0'))
            for val in UNO_VALUES[1:]:
                cards.append(UnoCard(color, val))
                cards.append(UnoCard(color, val))
        for _ in range(4):
            cards.append(UnoCard('wild', 'wild'))
            cards.append(UnoCard('wild', 'draw4'))
        return cards

    def top_card(self): return self.discard[-1]

    def can_play(self, card):
        if self.pending_draw > 0:
            if card.value == 'draw2': return True
            if card.value == 'draw4': return True
            return False
        return card.can_play_on(self.top_card(), self.current_color)

    def playable_cards(self, hand):
        return [c for c in hand if self.can_play(c)]

    def play_card(self, card_idx, chosen_color=None):
        hand = self.hands[self.current_player]
        card = hand[card_idx]
        if not self.can_play(card): return False
        hand.pop(card_idx)
        self.discard.append(card)

        if card.is_wild():
            self.current_color = chosen_color or 'red'
        else:
            self.current_color = card.color

        if len(hand) == 0:
            self.game_over = True
            self.winner = self.current_player
            return True

        if card.value == 'reverse':
            self.direction *= -1
            if self.num_players == 2:
                self._advance()
        elif card.value == 'skip':
            self._advance()
        elif card.value == 'draw2':
            self.pending_draw += 2
        elif card.value == 'draw4':
            self.pending_draw += 4

        self._advance()
        self.must_draw = (self.pending_draw > 0 and not self.playable_cards(self.hands[self.current_player]))
        return True

    def draw_card(self):
        if self.pending_draw > 0:
            for _ in range(self.pending_draw):
                self._draw_one(self.current_player)
            self.pending_draw = 0
            self._advance()
        else:
            self._draw_one(self.current_player)
            hand = self.hands[self.current_player]
            card = hand[-1]
            if self.can_play(card):
                pass
            else:
                self._advance()
        self.must_draw = False

    def _draw_one(self, player):
        if not self.deck:
            top = self.discard.pop()
            self.deck = self.discard[:]
            random.shuffle(self.deck)
            self.discard = [top]
        if self.deck:
            self.hands[player].append(self.deck.pop())

    def _advance(self):
        self.current_player = (self.current_player + self.direction) % self.num_players

    def ai_play(self, player_idx):
        hand = self.hands[player_idx]
        playable = [(i, c) for i, c in enumerate(hand) if self.can_play(c)]
        if not playable:
            self.draw_card()
            return None, None
        idx, card = max(playable, key=lambda x: (
            x[1].value in ['draw4', 'draw2', 'skip', 'reverse'],
        ))
        chosen = None
        if card.is_wild():
            color_counts = {col: sum(1 for c in hand if c.color == col) for col in UNO_COLORS}
            chosen = max(color_counts, key=color_counts.get)
        self.play_card(idx, chosen)
        return card, chosen

# ─── UNO Card Widget ─────────────────────────────────────────────────────────
COLOR_MAP = {
    'red':    ('#E74C3C', '#C0392B'),
    'green':  ('#27AE60', '#1E8449'),
    'blue':   ('#2980B9', '#1F618D'),
    'yellow': ('#F1C40F', '#D4AC0D'),
    'wild':   ('#8E44AD', '#6C3483'),
}

def draw_uno_card(painter, x, y, w, h, card, theme, facedown=False, small=False):
    th = THEMES[theme]
    radius = max(6, w // 6)

    if facedown:
        grad = QLinearGradient(x, y, x+w, y+h)
        grad.setColorAt(0, QColor('#1A237E'))
        grad.setColorAt(1, QColor('#283593'))
        painter.setBrush(grad)
        painter.setPen(QPen(QColor('#3F51B5'), 2))
        painter.drawRoundedRect(x, y, w, h, radius, radius)
        painter.setPen(QColor('#7986CB'))
        painter.setFont(QFont('Arial', max(8, w//4), QFont.Weight.Bold))
        painter.drawText(QRect(x, y, w, h), Qt.AlignmentFlag.AlignCenter, 'UNO')
        return

    color = card.color if card else 'wild'
    main_c, dark_c = COLOR_MAP.get(color, ('#888', '#666'))

    grad = QLinearGradient(x, y, x+w, y+h)
    grad.setColorAt(0, QColor(main_c))
    grad.setColorAt(1, QColor(dark_c))
    painter.setBrush(grad)
    painter.setPen(QPen(QColor('#FFFFFF'), 2))
    painter.drawRoundedRect(x, y, w, h, radius, radius)

    inner_margin = max(3, w // 8)
    painter.setBrush(QColor(255, 255, 255, 40))
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawEllipse(x + w//2 - w//3, y + h//2 - h//3, w*2//3, h*2//3)

    if card:
        val = card.value
        display = {
            'skip': '⊘', 'reverse': '⇄', 'draw2': '+2',
            'draw4': '+4', 'wild': '★'
        }.get(val, val)
        font_size = max(8, int(h * 0.35)) if not small else max(7, int(h * 0.4))
        painter.setFont(QFont('Arial', font_size, QFont.Weight.Bold))
        painter.setPen(QColor('#FFFFFF'))
        shadow_offset = 1
        painter.setPen(QColor(0, 0, 0, 80))
        painter.drawText(QRect(x+shadow_offset, y+shadow_offset, w, h),
                         Qt.AlignmentFlag.AlignCenter, display)
        painter.setPen(QColor('#FFFFFF'))
        painter.drawText(QRect(x, y, w, h), Qt.AlignmentFlag.AlignCenter, display)

        if not small:
            small_font = QFont('Arial', max(6, int(h * 0.15)), QFont.Weight.Bold)
            painter.setFont(small_font)
            painter.setPen(QColor('#FFFFFF'))
            painter.drawText(QRect(x+3, y+2, w-6, h//4), Qt.AlignmentFlag.AlignLeft, display)
            painter.drawText(QRect(x+3, y + h - h//4 - 2, w-6, h//4),
                             Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom, display)

class UnoBoard(QWidget):
    status_changed = pyqtSignal(str)
    need_color = pyqtSignal()

    def __init__(self, theme_name='light', lang='en', num_players=4):
        super().__init__()
        self.theme_name = theme_name
        self.lang = lang
        self.num_players = num_players
        self.engine = UnoEngine(num_players)
        self.selected_card = -1
        self.hover_card = -1
        self.ai_timer = QTimer()
        self.ai_timer.timeout.connect(self._ai_step)
        self.choosing_color = False
        self.color_rects = {}
        self.card_rects = []
        self.draw_btn_rect = QRect()
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(400, 400)
        self.setMouseTracking(True)

    def t(self, key): return TR[self.lang].get(key, key)
    def th(self): return THEMES[self.theme_name]

    def new_game(self, num_players=None):
        if num_players: self.num_players = num_players
        self.engine = UnoEngine(self.num_players)
        self.selected_card = -1
        self.hover_card = -1
        self.choosing_color = False
        self.ai_timer.stop()
        self.update()
        self._emit_status()
        if self.engine.current_player != 0:
            self.ai_timer.start(600)

    def _emit_status(self):
        e = self.engine
        if e.game_over:
            winner = e.winner
            name = f"{self.t('player')} {winner+1}"
            msg = f"{name} {self.t('uno_win')}"
        else:
            cp = e.current_player
            name = f"{self.t('player')} {cp+1}"
            cards = len(e.hands[cp])
            msg = f"{name} | {cards} {self.t('cards')}"
        self.status_changed.emit(msg)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        th = self.th()
        W, H = self.width(), self.height()
        e = self.engine

        p.fillRect(self.rect(), QColor(th['table_bg']))

        grid_pen = QPen(QColor(th['table_border']), 1)
        p.setPen(grid_pen)
        cell = 40
        for x in range(0, W, cell):
            p.drawLine(x, 0, x, H)
        for y in range(0, H, cell):
            p.drawLine(0, y, W, y)

        card_w = max(50, min(80, W // 10))
        card_h = int(card_w * 1.5)

        center_x, center_y = W // 2, H // 2

        deck_x = center_x - card_w - 10
        deck_y = center_y - card_h // 2
        draw_uno_card(p, deck_x, deck_y, card_w, card_h, None, self.theme_name, facedown=True)
        p.setPen(QColor('#FFFFFF'))
        p.setFont(QFont('Arial', max(7, card_w//6)))
        p.drawText(QRect(deck_x, deck_y - 20, card_w, 18),
                   Qt.AlignmentFlag.AlignCenter, self.t('draw_card'))
        self.draw_btn_rect = QRect(deck_x, deck_y, card_w, card_h)

        top = e.top_card()
        top_x = center_x + 10
        top_y = center_y - card_h // 2
        draw_uno_card(p, top_x, top_y, card_w, card_h, top, self.theme_name)

        color_indicator_size = max(16, card_w // 3)
        ci_x = top_x + card_w + 10
        ci_y = top_y + (card_h - color_indicator_size) // 2
        cc = e.current_color
        cc_main = COLOR_MAP.get(cc, ('#888','#666'))[0]
        p.setBrush(QColor(cc_main))
        p.setPen(QPen(QColor('#FFFFFF'), 2))
        p.drawEllipse(ci_x, ci_y, color_indicator_size, color_indicator_size)

        p.setPen(QColor('#FFFFFF'))
        p.setFont(QFont('Arial', max(7, card_w//8)))
        p.drawText(ci_x - 10, ci_y + color_indicator_size + 14, self.t('current_color'))

        dir_sym = '→' if e.direction == 1 else '←'
        p.setFont(QFont('Arial', max(10, card_w//4), QFont.Weight.Bold))
        p.setPen(QColor('#FFD700'))
        p.drawText(QRect(center_x - 15, center_y + card_h//2 + 5, 30, 24),
                   Qt.AlignmentFlag.AlignCenter, dir_sym)

        num_opponents = e.num_players - 1
        self._draw_opponents(p, W, H, card_w, card_h, num_opponents)

        if e.current_player == 0 and not e.game_over:
            hand = e.hands[0]
            self._draw_player_hand(p, W, H, card_w, card_h, hand)
        else:
            self.card_rects = []

        if e.pending_draw > 0:
            msg = f"+{e.pending_draw}"
            p.setFont(QFont('Arial', max(14, card_w//3), QFont.Weight.Bold))
            p.setPen(QColor('#FF4444'))
            p.drawText(QRect(center_x - 30, center_y - card_h//2 - 35, 60, 30),
                       Qt.AlignmentFlag.AlignCenter, msg)

        if self.choosing_color:
            self._draw_color_chooser(p, W, H)

        if e.game_over:
            self._draw_winner(p, W, H)

    def _draw_opponents(self, p, W, H, cw, ch, num_opp):
        e = self.engine
        positions = []
        if num_opp == 1:
            positions = [(W//2, 20, 'top')]
        elif num_opp == 2:
            positions = [(W//2, 20, 'top'), (20, H//2, 'left')]
        elif num_opp == 3:
            positions = [(W//4, 20, 'top'), (3*W//4, 20, 'top'), (20, H//2, 'left')]

        small_cw = max(25, cw // 2)
        small_ch = int(small_cw * 1.5)

        for i, (px, py, side) in enumerate(positions):
            player_idx = i + 1
            hand = e.hands[player_idx]
            num_cards = len(hand)
            is_current = (e.current_player == player_idx)

            max_show = min(num_cards, 10)
            overlap = max(small_cw + 4, (max_show * (small_cw + 4) + small_cw) // max_show if max_show > 1 else small_cw + 4)
            total_w = max_show * overlap + small_cw

            if side == 'top':
                sx = px - total_w // 2
                for j in range(max_show):
                    cx = sx + j * overlap
                    draw_uno_card(p, cx, py, small_cw, small_ch, None, self.theme_name, facedown=True, small=True)
            else:
                sy = py - (max_show * (small_ch // 2) + small_ch) // 2
                for j in range(max_show):
                    cy = sy + j * (small_ch // 2 + 2)
                    draw_uno_card(p, px, cy, small_cw, small_ch, None, self.theme_name, facedown=True, small=True)

            p.setPen(QColor('#FFFF00') if is_current else QColor('#FFFFFF'))
            p.setFont(QFont('Arial', max(8, small_cw//3), QFont.Weight.Bold if is_current else QFont.Weight.Normal))
            label = f"P{player_idx} [{num_cards}]"
            if num_cards == 1:
                label += f" {self.t('uno_shout')}"
            if side == 'top':
                p.drawText(px - 40, py + small_ch + 14, label)
            else:
                p.drawText(px + small_cw + 4, py + small_ch//2, label)

    def _draw_player_hand(self, p, W, H, cw, ch, hand):
        n = len(hand)
        if n == 0:
            self.card_rects = []
            return

        avail_w = int(W * 0.9)
        overlap = min(cw + 8, avail_w // max(n, 1))
        total_w = (n - 1) * overlap + cw
        sx = (W - total_w) // 2
        base_y = H - ch - 16

        self.card_rects = []
        for i, card in enumerate(hand):
            cx = sx + i * overlap
            cy = base_y
            if i == self.hover_card or i == self.selected_card:
                cy -= max(10, ch // 6)
            draw_uno_card(p, cx, cy, cw, ch, card, self.theme_name, small=False)
            self.card_rects.append(QRect(cx, cy, cw, ch))

            can_play = self.engine.can_play(card)
            if can_play:
                pen = QPen(QColor('#FFD700'), 2)
                p.setPen(pen)
                p.setBrush(Qt.BrushStyle.NoBrush)
                p.drawRoundedRect(cx, cy, cw, ch, max(4, cw//8), max(4, cw//8))
            if i == self.selected_card:
                pen = QPen(QColor('#FFFFFF'), 3)
                p.setPen(pen)
                p.setBrush(Qt.BrushStyle.NoBrush)
                p.drawRoundedRect(cx - 1, cy - 1, cw + 2, ch + 2, max(4, cw//8), max(4, cw//8))

        p.setFont(QFont('Arial', max(8, cw//6), QFont.Weight.Bold))
        p.setPen(QColor('#FFFFFF'))
        p.drawText(QRect(0, H - ch - 35, W, 20), Qt.AlignmentFlag.AlignCenter, self.t('your_hand'))

    def _draw_color_chooser(self, p, W, H):
        overlay = QColor(0, 0, 0, 150)
        p.fillRect(self.rect(), overlay)
        btn_size = max(60, min(100, W // 6))
        gap = 16
        total = 4 * btn_size + 3 * gap
        sx = (W - total) // 2
        sy = (H - btn_size) // 2
        self.color_rects = {}
        for i, col in enumerate(UNO_COLORS):
            cx = sx + i * (btn_size + gap)
            main_c = COLOR_MAP[col][0]
            p.setBrush(QColor(main_c))
            p.setPen(QPen(QColor('#FFFFFF'), 3))
            p.drawRoundedRect(cx, sy, btn_size, btn_size, 12, 12)
            p.setPen(QColor('#FFFFFF'))
            p.setFont(QFont('Arial', max(9, btn_size//6), QFont.Weight.Bold))
            p.drawText(QRect(cx, sy, btn_size, btn_size),
                       Qt.AlignmentFlag.AlignCenter, self.t(col))
            self.color_rects[col] = QRect(cx, sy, btn_size, btn_size)

        p.setPen(QColor('#FFFFFF'))
        p.setFont(QFont('Arial', max(11, btn_size//5), QFont.Weight.Bold))
        p.drawText(QRect(0, sy - 40, W, 35), Qt.AlignmentFlag.AlignCenter, self.t('choose_color'))

    def _draw_winner(self, p, W, H):
        overlay = QColor(0, 0, 0, 180)
        p.fillRect(self.rect(), overlay)
        e = self.engine
        winner = e.winner
        name = f"{self.t('player')} {winner+1}"
        msg = f"🎉 {name} {self.t('uno_win')} 🎉"
        p.setFont(QFont('Arial', max(16, W//20), QFont.Weight.Bold))
        p.setPen(QColor('#FFD700'))
        p.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, msg)

    def mousePressEvent(self, event):
        e = self.engine
        if e.game_over: return
        pos = event.position().toPoint()

        if self.choosing_color:
            for col, rect in self.color_rects.items():
                if rect.contains(pos):
                    self._apply_chosen_color(col)
            return

        if e.current_player != 0: return

        if self.draw_btn_rect.contains(pos):
            e.draw_card()
            self.selected_card = -1
            self.update()
            self._emit_status()
            if e.current_player != 0 and not e.game_over:
                self.ai_timer.start(600)
            return

        for i, rect in enumerate(self.card_rects):
            if rect.contains(pos):
                if self.selected_card == i:
                    card = e.hands[0][i]
                    if e.can_play(card):
                        if card.is_wild():
                            self.choosing_color = True
                            self._pending_card_idx = i
                            self.update()
                        else:
                            e.play_card(i)
                            self.selected_card = -1
                            self.update()
                            self._emit_status()
                            if not e.game_over and e.current_player != 0:
                                self.ai_timer.start(600)
                else:
                    self.selected_card = i
                    self.update()
                return
        self.selected_card = -1
        self.update()

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()
        new_hover = -1
        for i, rect in enumerate(self.card_rects):
            if rect.contains(pos):
                new_hover = i; break
        if new_hover != self.hover_card:
            self.hover_card = new_hover
            self.update()

    def _apply_chosen_color(self, color):
        self.choosing_color = False
        e = self.engine
        e.play_card(self._pending_card_idx, color)
        self.selected_card = -1
        self.update()
        self._emit_status()
        if not e.game_over and e.current_player != 0:
            self.ai_timer.start(600)

    def _ai_step(self):
        e = self.engine
        if e.game_over or e.current_player == 0:
            self.ai_timer.stop()
            self.update()
            return
        card, color = e.ai_play(e.current_player)
        self.update()
        self._emit_status()
        if e.game_over:
            self.ai_timer.stop()
        elif e.current_player == 0:
            self.ai_timer.stop()
        else:
            self.ai_timer.start(600)

    def apply_theme(self, theme_name, lang=None):
        self.theme_name = theme_name
        if lang: self.lang = lang
        self.update()

# ─── Main Window ─────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme_name = 'light'
        self.lang = 'en'
        self.current_game = 'chess'
        self.chess_mode = '2p'
        self.setWindowTitle('Board & Card Games')
        self.setMinimumSize(600, 600)
        self.resize(900, 700)
        self._build_ui()
        self._apply_theme()

    def t(self, key): return TR[self.lang].get(key, key)
    def th(self): return THEMES[self.theme_name]

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Top bar
        self.top_bar = QWidget()
        self.top_bar.setFixedHeight(52)
        top_layout = QHBoxLayout(self.top_bar)
        top_layout.setContentsMargins(12, 6, 12, 6)
        top_layout.setSpacing(8)

        self.title_lbl = QLabel(self.t('title'))
        self.title_lbl.setFont(QFont('Arial', 13, QFont.Weight.Bold))
        top_layout.addWidget(self.title_lbl)
        top_layout.addStretch()

        self.game_group = QButtonGroup(self)
        self.chess_btn = QPushButton(self.t('chess'))
        self.chess_btn.setCheckable(True)
        self.chess_btn.setChecked(True)
        self.chess_btn.setFixedHeight(34)
        self.chess_btn.setMinimumWidth(80)
        self.uno_btn = QPushButton(self.t('uno'))
        self.uno_btn.setCheckable(True)
        self.uno_btn.setFixedHeight(34)
        self.uno_btn.setMinimumWidth(80)
        self.game_group.addButton(self.chess_btn, 0)
        self.game_group.addButton(self.uno_btn, 1)
        self.chess_btn.clicked.connect(lambda: self._switch_game('chess'))
        self.uno_btn.clicked.connect(lambda: self._switch_game('uno'))
        top_layout.addWidget(self.chess_btn)
        top_layout.addWidget(self.uno_btn)
        top_layout.addSpacing(16)

        self.lang_combo = QComboBox()
        self.lang_combo.addItems(['English', '中文', 'فارسی'])
        self.lang_combo.setFixedHeight(34)
        self.lang_combo.currentIndexChanged.connect(self._change_lang)
        top_layout.addWidget(QLabel())
        top_layout.addWidget(self.lang_combo)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Light', 'Dark'])
        self.theme_combo.setFixedHeight(34)
        self.theme_combo.currentIndexChanged.connect(self._change_theme)
        top_layout.addWidget(self.theme_combo)

        main_layout.addWidget(self.top_bar)

        # Content
        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Stacked games
        self.stack = QStackedWidget()
        self.chess_board = ChessBoard(self.theme_name, self.lang, self.chess_mode)
        self.uno_board = UnoBoard(self.theme_name, self.lang, 4)
        self.stack.addWidget(self.chess_board)
        self.stack.addWidget(self.uno_board)
        content_layout.addWidget(self.stack, 1)

        # Side panel
        self.side_panel = QWidget()
        self.side_panel.setFixedWidth(160)
        side_layout = QVBoxLayout(self.side_panel)
        side_layout.setContentsMargins(10, 14, 10, 14)
        side_layout.setSpacing(10)

        self.status_lbl = QLabel('...')
        self.status_lbl.setWordWrap(True)
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_lbl.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        side_layout.addWidget(self.status_lbl)
        side_layout.addSpacing(6)

        self.mode_label = QLabel(self.t('mode'))
        self.mode_label.setFont(QFont('Arial', 9))
        side_layout.addWidget(self.mode_label)

        self.mode_2p_btn = QPushButton(self.t('two_player'))
        self.mode_2p_btn.setCheckable(True)
        self.mode_2p_btn.setChecked(True)
        self.mode_2p_btn.setFixedHeight(30)
        self.mode_2p_btn.clicked.connect(lambda: self._set_mode('2p'))
        side_layout.addWidget(self.mode_2p_btn)

        self.mode_ai_btn = QPushButton(self.t('vs_ai'))
        self.mode_ai_btn.setCheckable(True)
        self.mode_ai_btn.setFixedHeight(30)
        self.mode_ai_btn.clicked.connect(lambda: self._set_mode('ai'))
        side_layout.addWidget(self.mode_ai_btn)

        self.mode_group = QButtonGroup(self)
        self.mode_group.addButton(self.mode_2p_btn, 0)
        self.mode_group.addButton(self.mode_ai_btn, 1)

        side_layout.addSpacing(6)
        self.new_game_btn = QPushButton(self.t('new_game'))
        self.new_game_btn.setFixedHeight(36)
        self.new_game_btn.setFont(QFont('Arial', 10))
        self.new_game_btn.clicked.connect(self._new_game)
        side_layout.addWidget(self.new_game_btn)

        side_layout.addStretch()
        content_layout.addWidget(self.side_panel)

        main_layout.addWidget(content)

        # Bottom bar
        self.bot_bar = QWidget()
        self.bot_bar.setFixedHeight(28)
        bot_layout = QHBoxLayout(self.bot_bar)
        bot_layout.setContentsMargins(10, 2, 10, 2)
        self.info_lbl = QLabel('')
        self.info_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bot_layout.addWidget(self.info_lbl)
        main_layout.addWidget(self.bot_bar)

        # Signals
        self.chess_board.status_changed.connect(self.status_lbl.setText)
        self.uno_board.status_changed.connect(self.status_lbl.setText)

        self._switch_game('chess')

    def _switch_game(self, game):
        self.current_game = game
        if game == 'chess':
            self.stack.setCurrentWidget(self.chess_board)
            self.mode_label.show()
            self.mode_2p_btn.show()
            self.mode_ai_btn.show()
            self.status_lbl.setText(self.t('status_chess'))
        else:
            self.stack.setCurrentWidget(self.uno_board)
            self.mode_label.hide()
            self.mode_2p_btn.hide()
            self.mode_ai_btn.hide()
            self.status_lbl.setText(self.t('uno_title'))
        self._apply_theme()

    def _set_mode(self, mode):
        self.chess_mode = mode
        self.chess_board.new_game(mode)

    def _new_game(self):
        if self.current_game == 'chess':
            self.chess_board.new_game(self.chess_mode)
        else:
            self.uno_board.new_game()

    def _change_theme(self, idx):
        self.theme_name = 'light' if idx == 0 else 'dark'
        self._apply_theme()

    def _change_lang(self, idx):
        self.lang = ['en', 'zh', 'fa'][idx]
        self._apply_language()
        self._apply_theme()

    def _apply_language(self):
        self.title_lbl.setText(self.t('title'))
        self.chess_btn.setText(self.t('chess'))
        self.uno_btn.setText(self.t('uno'))
        self.mode_label.setText(self.t('mode'))
        self.mode_2p_btn.setText(self.t('two_player'))
        self.mode_ai_btn.setText(self.t('vs_ai'))
        self.new_game_btn.setText(self.t('new_game'))

    def _apply_theme(self):
        th = self.th()
        qss = f"""
        QMainWindow {{
            background-color: {th['bg']};
            color: {th['text']};
        }}
        QLabel {{
            color: {th['text']};
        }}
        QPushButton {{
            background-color: {th['btn']};
            color: {th['btn_text']};
            border: 1px solid {th['border']};
            border-radius: 6px;
            padding: 4px 8px;
        }}
        QPushButton:hover {{
            background-color: {th['btn_hover']};
        }}
        QPushButton:pressed {{
            background-color: {th['btn_active']};
        }}
        QPushButton:checked {{
            background-color: {th['highlight']};
            color: #ffffff;
        }}
        QComboBox {{
            background-color: {th['panel']};
            color: {th['text']};
            border: 1px solid {th['border']};
            border-radius: 5px;
            padding: 3px 6px;
        }}
        QComboBox QAbstractItemView {{
            background-color: {th['panel']};
            color: {th['text']};
            selection-background-color: {th['highlight']};
        }}
        """
        self.setStyleSheet(qss)

        bar_style = f"background:{th['panel']}; border-bottom:1px solid {th['border']};"
        self.top_bar.setStyleSheet(bar_style)

        bot_style = f"background:{th['panel']}; border-top:1px solid {th['border']};"
        self.bot_bar.setStyleSheet(bot_style)

        side_style = f"background:{th['panel']}; border-left:1px solid {th['border']};"
        self.side_panel.setStyleSheet(side_style)

        self.chess_board.apply_theme(self.theme_name, self.lang)
        self.uno_board.apply_theme(self.theme_name, self.lang)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Board & Card Games')
    app.setStyle('Fusion')

    font = QFont('Arial', 10)
    app.setFont(font)

    win = MainWindow()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
