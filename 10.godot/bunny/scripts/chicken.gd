extends CharacterBody2D

@export var target: Node2D = null
@export var max_speed = 50
@onready var navigation: NavigationAgent2D = $NavigationAgent2D


func setup():
	await get_tree().physics_frame
	if target:
		navigation.target_position = target.global_position

func _ready() -> void:
	call_deferred("setup")
	print(navigation.get_current_navigation_path())
	
func nearest_egg():
	var eggs = get_parent().get_parent().eggs 
	if !eggs: 
		eggs=[]
	var near_egg = null
	var min_distance 
	for egg in eggs.get_children():
		var distance = global_position.distance_squared_to(egg.global_position)
		if near_egg == null || min_distance > distance:
			near_egg = egg
			min_distance = distance
	return near_egg

func _physics_process(delta: float) -> void:
	
	var near_egg = nearest_egg()
	if near_egg:
		navigation.target_position = near_egg.global_position
	if navigation.is_navigation_finished():
		return
	
	var nex_path_position = navigation.get_next_path_position()
	
	velocity = global_position.direction_to(nex_path_position) * max_speed
	
	move_and_slide()
