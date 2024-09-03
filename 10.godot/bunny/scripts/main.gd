extends Node2D

@onready var eggs = $Eggs
@onready var farm = $Chickens

const egg_scene = preload("res://scenes/egg.tscn")
const chicken_scene = preload("res://scenes/chicken.tscn")


func _on_player_do_put_egg(egg_position: Variant) -> void:
	var egg_instance = egg_scene.instantiate()
	egg_instance.global_position = egg_position
	egg_instance.hatch_egg.connect(_on_egg_hatch_egg)
	eggs.add_child(egg_instance)

func _on_egg_hatch_egg(chicken_position: Variant) -> void:
	var chicken_instance = chicken_scene.instantiate()
	chicken_instance.global_position = chicken_position
	farm.add_child(chicken_instance)
