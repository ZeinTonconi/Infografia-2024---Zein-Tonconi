extends CharacterBody2D

@onready var state_machine = $AnimationTree.get("parameters/playback")


func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_up"):
		state_machine.travel("Attack")
	elif Input.is_action_just_pressed("ui_down"):
		state_machine.travel("Hit")
	elif Input.is_action_just_pressed("ui_accept"):
		state_machine.travel("Dead")
