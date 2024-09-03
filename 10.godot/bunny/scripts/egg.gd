extends StaticBody2D

signal hatch_egg(chicken_position)

func _on_area_2d_area_entered(area: Area2D) -> void:
	hatch_egg.emit(global_position)
	queue_free()
