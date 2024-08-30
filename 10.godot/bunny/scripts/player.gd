extends CharacterBody2D

@onready var anim_tree = $AnimationTree
@onready var state_machine = $AnimationTree.get("parameters/playback")

var input_vector

func set_blend_position(vector):
	anim_tree.set("parameters/Idle/blend_position", vector)
	anim_tree.set("parameters/Run/blend_position", vector)
	anim_tree.set("parameters/Axe/blend_position", vector)
	anim_tree.set("parameters/Pick/blend_position", vector)

func _on_player_control_do_move(incoming_input_vector: Vector2) -> void:
	input_vector = incoming_input_vector
	set_blend_position(input_vector)
	state_machine.travel("Run")


func _on_player_control_do_attack() -> void:
	print(input_vector)
	set_blend_position(input_vector)
	state_machine.travel("Axe")
