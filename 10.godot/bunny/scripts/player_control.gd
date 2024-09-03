extends Node2D

class_name PlayerControl

# signals
signal do_attack
signal do_move(input_vector)
signal do_put_egg

@export var body: CharacterBody2D

@onready var timer = $Timer

const ACCELERATION = 500
const FRICTION = 500
const MAX_SPEED = 100

enum {
	MOVE,
	ATTACK
}

var state = MOVE

var input_vector
var last_direction

func _physics_process(delta: float) -> void:
	match state:
		MOVE:
			move_state(delta)
		ATTACK:
			attack_state(delta)
			
func move_state(delta):
	input_vector = Vector2.ZERO
	input_vector.x = Input.get_axis("Left", "Right")
	input_vector.y = Input.get_axis("Up", "Down")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		do_move.emit(input_vector)
		body.velocity = body.velocity.move_toward(input_vector * MAX_SPEED, ACCELERATION * delta)
		last_direction = input_vector
	else:
		body.velocity = body.velocity.move_toward(Vector2.ZERO, FRICTION * delta)
	
	body.move_and_slide()
	
	if Input.is_action_just_pressed("Attack"):
		state = ATTACK
		do_attack.emit()
		timer.start()
		print("attack")
	
func attack_state(delta):
	body.velocity = Vector2.ZERO
	
func attack_anim_finished():
	state = MOVE
	do_move.emit(last_direction)

func _on_timer_timeout() -> void:
	attack_anim_finished()

func _input(event: InputEvent) -> void:
	if event is InputEventKey:
		if event.is_action_pressed("PutEgg"):
			do_put_egg.emit()
