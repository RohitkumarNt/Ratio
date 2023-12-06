from manim import *
class RatioTestingNewFileImplementation(Scene):
    imagesPathDirectory = 'C:/Users/rohit.kumar1/Desktop/TestingImageForRatios/'

    def topBackgroundQuestionText(self):
        some_portion = Rectangle(width=config.frame_width, height=config.frame_height / 4, fill_color=BLUE,
                                 fill_opacity=1, stroke_width=0).to_edge(UP)
        text = Text("RATIOS", color=PURPLE).move_to(some_portion.get_center())  # Set text position to the center
        group = VGroup(some_portion, text)  # Group the rectangle and text
        self.add(group)
        questionDescription=Text("Let's learn Ratios",color=BLACK)
        questionDescription.next_to(some_portion,DOWN)
        self.add(questionDescription)
        questionTextX=Text("3 ",color=RED)
        questionTextColon=Text(": ",color=YELLOW,)
        questionTextY = Text("4", color=DARK_BLUE)
        questionTextX = Text("3 ", color=RED)
        questionTextColon = Text(": ", color=YELLOW, )
        questionTextY = Text("4", color=DARK_BLUE)
        questionTextX.next_to(questionDescription, DOWN)
        questionTextColon.next_to(questionTextX, RIGHT)
        questionTextY.next_to(questionTextColon, RIGHT)

        combine = VGroup(questionTextX, questionTextColon, questionTextY)
        combine.next_to(questionDescription, DOWN)
        self.add(combine)
        value = 0.5
        leftSideImageCopy = Group(*[
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),

        ])


        # Position the images in a single row


        # Play the FadeIn animation for the entire group

        leftSideImageCopy.next_to(questionTextX, DOWN)
        leftSideImageCopy.shift(LEFT*2)
        for i in range(len(leftSideImageCopy)):
            if i != 0:
                leftSideImageCopy[i].next_to(leftSideImageCopy[i - 1], RIGHT, buff=0.2)
            self.play(FadeIn(leftSideImageCopy[i]))

        # secondCopyImage.next_to(leftSideImageCopy,DOWN)
        self.wait(duration=2)
        secondCopyImage = Group(
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
        )
        secondCopyImage.arrange(RIGHT, buff=0.2)
        secondCopyImage.next_to(leftSideImageCopy, DOWN)
        # secondCopyImage.shift(LEFT*2)

        self.play(FadeIn(secondCopyImage))
        self.wait(duration=2)


        #here third one
        thirdCopyImage = Group(
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
        )
        thirdCopyImage.arrange(RIGHT, buff=0.2)
        thirdCopyImage.next_to(secondCopyImage, DOWN)
        # secondCopyImage.shift(LEFT*2)

        self.play(FadeIn(thirdCopyImage))
        self.wait(duration=2)

        #here fourth one
        fourthCopyImage = Group(
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'RedAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
            ImageMobject(self.imagesPathDirectory + 'PurpleAppleImage.jpeg').scale(value),
        )
        fourthCopyImage.arrange(RIGHT, buff=0.2)
        fourthCopyImage.next_to(thirdCopyImage, DOWN)
        # secondCopyImage.shift(LEFT*2)

        self.play(FadeIn(fourthCopyImage))
        self.wait(duration=2)


        # self.play(FadeIn(secondCopyImage))

    def construct(self):
        self.camera.background_color = WHITE
        self.topBackgroundQuestionText()