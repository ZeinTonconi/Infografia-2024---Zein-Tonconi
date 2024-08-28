extends CharacterBody2D

const MAX_SPEED = 80
const FRICTION = 500
const DAMAGE = 10

@export var hp = 100
var is_hit = false

@onready var state_machine = $AnimationTree.get("parameters/playback")

func _physics_process(delta: float) -> void:
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	input_vector.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	input_vector = input_vector.normalized()	
	
	if input_vector != Vector2.ZERO:
		# en movimiento
		state_machine.travel("Run")
	else:
		state_machine.travel("Idle")
	
	velocity = MAX_SPEED * input_vector
	if Input.is_action_just_pressed("attack"):
		state_machine.travel("Attack")
	elif is_hit:
		state_machine.travel("Hit")
		is_hit = false
	
	if hp <= 0:
		state_machine.travel("Dead")
		
	if velocity.x < 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
	elif velocity.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	
	move_and_slide()
		


func _on_hurt_box_area_entered(area: Area2D) -> void:
	print("area entered", area)


func _on_hurt_box_body_entered(body: Node2D) -> void:
	is_hit = true
	hp -= DAMAGE
	print("body entered, remaining HP: ", hp) # Replace with function body.
	
