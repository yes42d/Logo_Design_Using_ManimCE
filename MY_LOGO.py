from manim import *
class Mylogo(Scene):
    def construct(self):
        circle = Circle(fill_opacity=5).scale(2)
        circle.set_fill()
        circle.set_color(DARK_BROWN)
        Text=TextMobject("Yes ","42","d")
        Text[0].set_color(GREEN_E)
        Text[1].set_color(YELLOW)
        Text[2].set_color(RED_C)
        Text.next_to(circle,0,buff=0).scale(2)
        Text1=TextMobject("Analytics")
        Text1.set_color(GOLD_A)
        Text1.next_to(circle,DOWN,buff=0.2).scale(1.5)
        picture=Group(*self.mobjects)

        self.play(DrawBorderThenFill(circle,run_time=6),Write(Text,run_time=6),Write(Text1,run_time=6))
        self.wait()

        
       