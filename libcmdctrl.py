import ctypes

STD_OUTPUT_HANDLE = -11 
HANDLE = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cursor_position(x,y):
	position = (x + (y << 16))
	ctypes.windll.kernel32.SetConsoleCursorPosition(HANDLE, position)

def clear_console():
	ctypes.windll.kernel32.SetConsoleCursorPosition(HANDLE, 0)

def clear():
	set_cursor_position(0 ,0)
	empty_line = ''
	for i in range(79):
		empty_line += ' '

	for i in  range(24):
		print(empty_line)
	set_cursor_position(0, 0)