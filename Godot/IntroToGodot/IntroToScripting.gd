extends Node2D

# Called when the node enters the scene tree for the first time.
func _ready():
	_welcome_message()
	_add(10,25)

func _add(a, b):
	return a + b

func _welcome_message():
	print("Welcome Message")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
