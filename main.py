import turtle as t, math as m, random as r, time
s = t.Screen(); s.setup(700,700); 
s.title("Heart Dust"); 
s.bgcolor("black"); s.tracer(0)
p = t.Turtle(); p.hideturtle()

def heart(a, scale) :
    x = 16 * (m.sin(a)**3) * scale
    y = (13 * m.cos(a) - 5 * m.cos(2*a) - 2 * m.cos(3*a) - m.cos(4*a)) * scale
    return x, y

for i in range(10000):
    a = r.uniform(0, 2*m.pi)
    sc = r.uniform(0.5, 15.5)
    x, y = heart(a, sc)

    ang = m.atan2(y,x) + r.uniform(-0.5, 0.5)
    length = r.uniform(4,14)

    p.pencolor(1.0, r.uniform(0.25, 0.55), r.uniform(0.65, 0.85))
    p.width(r.uniform(0.5, 1.2))
    p.penup(); p.goto(x, y)
    p.pendown(); p.goto(x + length * m.cos(ang), y + length * m.sin(ang))

    if i % 200 == 0: s.update(); time.sleep(0.002)
    
for i in range(3500):
    a = r.uniform(0, 2 * m.pi)
    x, y= heart(a, 16.9)

    ang = m.atan2(y, x)+ r.uniform(-0.35, 0.35)
    length= r.uniform(10, 32)

    p.pencolor(1.0, r.uniform(0.45, 0.75), r.uniform(0.75, 0.95))
    p.width(r.uniform(0.4, 0.9))
    p.penup(); p.goto(x + r.uniform(-2, 2), y + r.uniform(-2, 2))
    p.pendown(); p.goto(x + length * m.cos(ang), y + length * m.sin(ang))

    if i % 150 == 0: s.update(); 
    time.sleep(0.002)

s.update()
t.done()