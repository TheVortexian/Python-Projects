// Perlin Noise testing.

  
float xoff = 0.0;

void setup() {
 size(400, 400);
 background(0);
}

void draw() {
  background(0);
  fill(#FFFFFF);
  stroke(#FFFFFF);
  xoff = xoff + .01;
  float n = noise(xoff) * width;
  line(n, 0, n, height);
}