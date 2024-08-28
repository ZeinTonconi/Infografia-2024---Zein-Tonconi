extends CharacterBody2D

var SPEED = 150			
var GRAVITY = ProjectSettings.get_setting("physics/2d/default_gravity")
var JUMP_SPEED = -600

func _physics_process(delta: float) -> void:
	var right = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	velocity.x = right * SPEED
	velocity.y += GRAVITY * delta
	
	#var upDown = Input.get_action_raw_strength("ui_down")-Input.get_action_strength("ui_up")
	#velocity.y = upDown * SPEED
	if Input.is_action_just_pressed("ui_up") and is_on_floor():
		velocity.y = JUMP_SPEED 
	
	
	# tiene su constante delta
	move_and_slide()
	
	for i in get_slide_collision_count():
		var collision = get_slide_collision(i)
		print("hit by: ", collision.get_collider().name)
