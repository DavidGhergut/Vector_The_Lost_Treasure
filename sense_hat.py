import pygame
import time
import threading
import copy
import queue

class StickEvent:
	def __init__(self):
		self.action = "unknown"
		self.direction = "unknown"

class SenseHatEmu:
	def __init__(self):
		self.lock = threading.Lock()
		self.window = None
		self.draw_th = None
		self.grid = []
		self.active = False
		self.events = queue.Queue(128)
		self.r = 0
		self.cv = threading.Condition()
		self.started = False
		self.clear_color = [50, 50, 50]
		self.rot = [
			self.rotated_grid(0),
			self.rotated_grid(1),
			self.rotated_grid(2),
			self.rotated_grid(3)]
		self.grid = []
		for i in range(64):
			self.grid.append(self.clear_color)
		self.side = 320
		self.active = True
		

	def draw_fn(self):
		print("will start drawing")
		with self.cv:
			pygame.init()
			self.window = pygame.display.set_mode((self.side, self.side))
			self.started = True
			self.cv.notify()
		print("notified start")

		while self.active:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					#self.active = False
				if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
					se_event = StickEvent()
					
					if event.type == pygame.KEYUP:
						se_event.action = "relseased"
					if event.type == pygame.KEYDOWN:
						se_event.action = "pressed"

					if event.key == pygame.K_SPACE:
						se_event.direction = "middle"
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						se_event.direction = "left"
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						se_event.direction = "right"
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						se_event.direction = "up"
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						se_event.direction = "down"

					self.events.put(se_event)

				# push events

			with self.lock:
				for i in range(64):
					x1 = (i % 8) * self.side / 8
					y1 = (i // 8) * self.side / 8
					s = self.side / 9
					color = self.grid[self.rot[self.r][i]]
					if color[0] < 50 and color[1] < 50 and color[2] < 50:
						color = self.clear_color
					pygame.draw.rect(self.window, color, (x1, y1, s, s))
					# pygame.draw.rect(self.window, [255, 255, 255],
					# 		(x1, y1, s, s), 1)
				pygame.display.flip()
			time.sleep(0.01)

	def loop(self):
		print("loop start")
		self.draw_fn()

	def rotated_grid(self, count):
		# 00 01 02 03
		# 10 11 12 13
		# 20 21 22 23
		# 30 31 32 33

		# 30 20 10 00
		# 31 21 11 01
		# 32 22 12 02
		# 33 23 13 03
		rot_grid = []
		grid_ind = []
		aux_grid = []
		for i in range(64):
			rot_grid.append(i)
			grid_ind.append(i)
			aux_grid.append(i)
		for row in range(8):
			for col in range(8):
				rot_grid[row * 8 + col] = (7 - col) * 8 + row
		for k in range(count):
			for i in range(64):
				aux_grid[i] = grid_ind[rot_grid[i]]
			grid_ind = copy.deepcopy(aux_grid)
		return grid_ind

	def init(self):
		with self.lock:
			if self.window:
				return
			with self.cv:
				while not self.started:
					self.cv.wait()

	def set_pixels(self, grid):
		self.init()
		with self.lock:
			self.grid = copy.deepcopy(grid)

	def set_pixel(self, col, row, color):
		self.init()
		with self.lock:
			self.grid[row * 8 + col] = copy.deepcopy(color)

	def set_rotation(self, r):
		self.init()
		with self.lock:
			if r not in [0, 90, 180, 270]:
				raise Exception("Invalid rotation")
			self.r = r // 90

	def get_pixels(self):
		self.init()
		with self.lock:
			return copy.deepcopy(self.grid)

	def clear(self):
		self.init()
		with self.lock:
			self.grid = []
			for i in range(64):
				self.grid.append(self.clear_color)

	def wait_for_event(self, emptybuffer=False):
		self.init()
		if emptybuffer:
			try:
				while True:
					self.events.get(block=False)
			except queue.Empty as e:
				pass

		return self.events.get()

sense_emu = SenseHatEmu()

class Stick:
	def __init__(self):
		pass

	def wait_for_event(self, emptybuffer=False):
		sense_emu.init()
		return sense_emu.wait_for_event(emptybuffer=emptybuffer)

class SenseHat:
	def __init__(self):
		self.stick = Stick()

	def loop(self):
		sense_emu.loop()

	# sets 8x8 pixel grid
	def set_pixels(self, grid):
		sense_emu.set_pixels(grid)

	def set_pixel(self, col, row, color):
		sense_emu.set_pixel(col, row, color)

	def set_rotation(self, r):
		sense_emu.set_rotation(r)

	def clear(self):
		sense_emu.clear()

	def get_pixels(self):
		return sense_emu.get_pixels()

	def show_message(self, msg, text_colour=None, scroll_speed=0.1):
		print("[SENSE_HAT]: " + str(msg))
