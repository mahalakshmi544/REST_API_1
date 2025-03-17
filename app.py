from flask import Flask, jsonify

todo = Flask(__name__)

students = [
    {
        'id': 1,
        'student_name': 'std1',
        'age': 21,
        'email': 'hello@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'std2',
        'age': 22,
        'email': 'hello@gmail.com'
    },
    {
        'id': 4,
        'student_name': 'std3',
        'age': 23,
        'email': 'hello@gmail.com'
    }
]

# Route to get all students
@todo.route('/students-list')
def student_list():
    return jsonify(students)

# Route to get student by ID using for loop
@todo.route('/students-list/<int:id>', methods=['GET'])
def get_student_by_id(id):
    for student in students:
        if student['id'] == id:
            return jsonify(student)  # ✅ Return full student details
    return jsonify({'message': 'ID not found'}), 404

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )
