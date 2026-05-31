# practice_07_quiz_game.py
"""
Quiz Game Project
"""

class QuizGame:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is 2 + 2?": "4",
            "What is the largest ocean on Earth?": "Pacific",
            "Who wrote 'Romeo and Juliet'?": "Shakespeare",
            "What is the chemical symbol for Gold?": "Au"
        }
        self.score = 0
        self.total_questions = len(self.questions)
    
    def run_quiz(self):
        print("=" * 50)
        print("🎯 WELCOME TO THE QUIZ GAME! 🎯")
        print("=" * 50)
        
        for question, correct_answer in self.questions.items():
            print(f"\nQuestion: {question}")
            user_answer = input("Your answer: ").strip()
            
            if user_answer.lower() == correct_answer.lower():
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {correct_answer}")
        
        self.show_results()
    
    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 50)
        print("📊 QUIZ RESULTS 📊")
        print("=" * 50)
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        print(f"Score: {percentage:.1f}%")
        
        if percentage >= 80:
            print("🎉 Excellent! You're a quiz master!")
        elif percentage >= 60:
            print("👍 Good job! Keep practicing!")
        else:
            print("📚 Keep learning! Try again!")

# Run the game
if __name__ == "__main__":
    game = QuizGame()
    game.run_quiz()