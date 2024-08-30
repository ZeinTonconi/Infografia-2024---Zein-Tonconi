extends CharacterBody2D

const ACCELERATION = 500
const FRICTION = 500
const MAX_SPEED = 100


# estados del player
enum {
	MOVE,
	ROLL,
	ATTACK
}

# variable de estado actual
var state = MOVE
@export var hp = 100

@onready var animation_tree = $AnimationTree
@onready var state_machine = $AnimationTree.get("parameters/playback")


func _physics_process(delta: float) -> void:
	match state:
		MOVE:
			move_state(delta)
		ROLL:
			pass
		ATTACK:
			attack_state(delta)
	
func move_state(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_axis("ui_left", "ui_right")
	input_vector.y = Input.get_axis("ui_up", "ui_down")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		animation_tree.set("parameters/Idle/blend_position", input_vector)
		animation_tree.set("parameters/Run/blend_position", input_vector)
		animation_tree.set("parameters/Attack/blend_position", input_vector)
		state_machine.travel("Run")
		velocity = velocity.move_toward(input_vector * MAX_SPEED, ACCELERATION * delta)
	else:
		state_machine.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
		
	move_and_slide()
	
	if Input.is_action_just_pressed("attack"):
		# transicion a ATTACK
		state = ATTACK

func attack_state(delta):
	velocity = Vector2.ZERO
	state_machine.travel("Attack")

func attack_anim_finished():
	state = MOVE


func _on_hurt_box_area_entered(area: Area2D) -> void:
	print("OUCH")
	hp -= 10
