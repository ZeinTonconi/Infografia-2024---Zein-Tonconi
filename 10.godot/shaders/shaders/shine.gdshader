shader_type canvas_item;

void fragment() {
    float wave = sin(UV.x * 10.0); // Sine wave along the x-axis
	float wave_y = sin(UV.y * 10.0);
    COLOR = vec4(wave, wave_y, wave, 0.2); // Grayscale based on sine wave
}