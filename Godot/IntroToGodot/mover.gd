extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	var vec = Vector2(0,0)
	global_position = vec # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var direction = Vector2(1,1)
	global_position += direction * 30 * delta
