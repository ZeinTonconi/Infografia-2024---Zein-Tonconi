extends Control

@onready var child_label = $Titulo

@onready var button = $Button

func _on_button_3_button_down() -> void:
	if child_label.text == "HOLA!":
		child_label.text = "SALUDOS"
		button.text = "Cambiado"
