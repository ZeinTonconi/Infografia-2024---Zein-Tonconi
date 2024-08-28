extends CharacterBody2D

const MAX_SPEED = 80
const FRICTION = 500

@onready var state_machine = $AnimationTree.get("parameters/playback")

func _physics_process(delta: float) -> void:
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	input_vector.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		state_machine.travel("Run")
	else:
		state_machine.travel("Idle")
		
	velocity = MAX_SPEED * input_vector
	move_and_slide()
	
