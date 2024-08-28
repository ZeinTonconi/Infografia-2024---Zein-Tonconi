#extends CharacterBody2D
#
#@onready var player = $AnimationPlayer
#var isAttacking = false
#
#func _ready() -> void:
	#player.play("Idle")
#
#func _process(delta: float) -> void:
	#if Input.is_action_just_pressed("ui_accept"):
		#player.play("Attack")
		#isAttacking = true
	#if not isAttacking:
		#player.play("Idle")
#
#
#func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	#if(anim_name == "Attack"):
		#isAttacking = false
	#pass # Replace with function body.
	
extends CharacterBody2D

const MAX_SPEED = 80
const FRICTION = 500
const DAMAGE = 10
@onready var state_machine = $AnimationTree.get("parameters/playback")
var is_hit = false
var hp = 10


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
	
	if velocity.x < 0:
		$Sprite2D.scale.x = -abs($Sprite2D.scale.x)
	elif velocity.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	
	if Input.is_action_just_pressed("attack"):
		state_machine.travel("Attack")
	elif is_hit:
		state_machine.travel("Damage")
		is_hit = false
	
	if hp<=0:
		state_machine.travel("Dead")
	move_and_slide()
	


func _on_hurt_box_area_entered(area: Area2D) -> void:
	print(area)
	pass # Replace with function body.


func _on_hurt_box_body_shape_entered(body_rid: RID, body: Node2D, body_shape_index: int, local_shape_index: int) -> void:
	is_hit = true
	hp -= DAMAGE
