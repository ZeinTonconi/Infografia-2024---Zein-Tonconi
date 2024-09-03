extends CharacterBody2D

@onready var anim_tree = $AnimationTree
@onready var state_machine = $AnimationTree.get("parameters/playback")

var input_vector
var egg_scene

func _ready() -> void:
	# precargar escena
	egg_scene = preload("res://scenes/egg.tscn")
	

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


func _on_player_control_do_put_egg() -> void:
	# instanciar escena
	var egg_instance = egg_scene.instantiate()
	add_child(egg_instance)
	
	egg_instance.position = Vector2.ZERO
