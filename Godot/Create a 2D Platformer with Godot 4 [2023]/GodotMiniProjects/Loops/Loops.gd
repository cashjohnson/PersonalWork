extends Node2D

@export var spawn_count : int = 300
var star_scene = preload("res://Loops/star.tscn")
var i : int = 0

# Called when the node enters the scene tree for the first time.
func _process(delta):
	if i < spawn_count:
		var star = star_scene.instantiate()
		add_child(star)
		
		star.position.x = randi_range(-280, 280)
		star.position.y = randi_range(-160, 160)
		
		var star_size = randf_range(0.5, 1)
		star.scale.x = star_size
		star.scale.y = star_size
		i = i + 1
