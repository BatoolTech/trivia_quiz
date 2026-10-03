# قائمة الأسئلة والأجوبة للعبة التلفزيونية والبرمجية
questions = [
    {
        "prompt": "ما هي لغة البرمجة التي نستخدمها الآن لبناء هذا المشروع؟",
        "options": ["A) Java", "B) Python", "C) C++", "D) HTML"],
        "answer": "B"
    },
    {
        "prompt": "أي من هذه المكونات يُستخدم لتخزين بيانات على شكل مفتاح وقيمة (Key-Value)؟",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Integer"],
        "answer": "B"
    },
    {
        "prompt": "في أي جامعة تدرسين تخصص علوم الحاسب؟",
        "options": ["A) جامعة الملك سعود", "B) جامعة الملك فهد", "C) جامعة أم القرى", "D) جامعة نورة"],
        "answer": "A"
    }
]

score = 0

# حلقة تكرارية لعرض الأسئلة واستقبال الإجابات
for q in questions:
    print("\n" + q["prompt"])
    for option in q["options"]:
        print(option)

    # استقبال إجابة المستخدم
    user_answer = input("اكتب رمز الإجابة (A, B, C, D): ").strip().upper()

    # التحقق من صحة الإجابة
    if user_answer == q["answer"]:
        print("إجابة صحيحة! 🎉")
        score += 1
    else:
        print(f"إجابة خاطئة. الإجابة الصحيحة هي: {q['answer']}")

# عرض النتيجة النهائية للمستخدم
print("\n" + "=" * 30)
print(f"انتهت اللعبة! نتيجتك النهائية هي: {score} من {len(questions)}")
if score == len(questions):
    print("مذهل! أنتِ عبقرية برمجية حقيقية! 🌟")
else:
    print("بداية ممتازة، استمري في التطور! 💪")