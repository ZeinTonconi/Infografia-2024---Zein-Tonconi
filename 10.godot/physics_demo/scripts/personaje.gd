extends CharacterBody2D

var SPEED = 300
var JUMP_SPEED = -600
var GRAVITY = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta: float) -> void:
	var horizontal = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	velocity.y += GRAVITY * delta
	velocity.x = horizontal * SPEED
	
	if Input.is_action_just_pressed("ui_up") and is_on_floor():
		velocity.y = JUMP_SPEED
		
	move_and_slide()
