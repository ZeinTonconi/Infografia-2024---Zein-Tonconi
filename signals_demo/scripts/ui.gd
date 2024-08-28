extends Control

var board = []
var player = false
@onready var title = $Title
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	board = [
		[$Button_0_0, $Button_0_1, $Button_0_2],
		[$Button_1_0, $Button_1_1, $Button_1_2],
		[$Button_2_0, $Button_2_1, $Button_2_2],	
	]
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func checkEndGame():
	
	for i in range(3):
		var count = 0
		for j in range(3):
			if board[i][j].text == "X":
				count += 1
			if board[i][j].text == "O":
				count -= 1
		if abs(count) == 3:
			return true	
	for i in range(3):
		var count = 0
		for j in range(3):
			if board[j][i].text == "X":
				count += 1
			if board[i][j].text == "O":
				count -= 1
		if abs(count) ==3:
			return true
	
	if(board[0][0].text == board[1][1].text and board[1][1].text==board[2][2].text) and board[0][0].text != "_":
		return true
	return false

func changeTurn():
	player = !player
	for row in board:
		for column in row:
			column.player = player
	
	var endGameString
	if player:
		endGameString = "Gano X"
	else:
		endGameString = "Gano O"
	
	if(checkEndGame()):
		title.text = endGameString 
	

func _on_button_0_0_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_0_1_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_0_2_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_1_0_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_1_1_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_1_2_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_2_0_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_2_1_button_down() -> void:
	changeTurn()
	pass # Replace with function body.


func _on_button_2_2_button_down() -> void:
	changeTurn()
	pass # Replace with function body.
