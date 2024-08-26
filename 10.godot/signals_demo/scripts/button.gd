extends Button

@export var label: Label

func _on_button_down() -> void:
	print("boton ha sido presionado!")
	# cambiar etiqueta
	label.text = "HOLA!"
