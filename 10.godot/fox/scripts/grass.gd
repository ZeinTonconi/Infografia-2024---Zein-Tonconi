extends Node2D


func _on_hurt_box_area_entered(area: Area2D) -> void:
	queue_free()
