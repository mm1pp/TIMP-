var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БИБ2102",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БИБ2104",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БИБ2103",
        "marks": [5, 5, 5]
    },
    {
        "name": "Владислав",
        "surname": "Лимонов",
        "group": "БИБ2103",
        "marks": [2, 3, 5]
    },
    {
        "name": "Никита",
        "surname": "Сенаторов",
        "group": "БИБ2101",
        "marks": [5, 5, 4]
    }
];

console.log(groupmates);

var rpad = function(str, length) 
{
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет 
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки return str; // когда все пробелы добавлены, возвратить строку
    return str;
};

var printStudent = function (student) {
    console.log(
        rpad(student['name'], 15),
        rpad(student['surname'], 15),
        rpad(student['group'], 8),
        rpad(student['marks'], 20)
    );
}
    
var printStudents = function(students)
{ 
    console.log(
    rpad("Имя", 15),
    rpad("Фамилия", 15),
    rpad("Группа", 8),
    rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++){
    // в цикле выводится каждый экземпляр студента 
        printStudent(students[i]);
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

printStudents(groupmates); 

var print_students_by_groupnames = function (students, Group_Name) 
{
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
        );
    for (var i = 0; i < students.length; i++)
        if (students[i]["group"] == Group_Name)
            printStudent(students[i]);
    console.log("\n");
};

var sr_ball = function(student)
{
    var sum = 0;
    for (var i = 0; i < student.length; i++)
    {
        sum += student[i];
    }
    return (sum/student.length);
};

var print_students_by_average_grade = function(students, average_Grade) 
{
    console.log(average_Grade);
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
        );
    for (var i = 0; i < students.length; i++)
        if (sr_ball(students[i]['marks']) >= average_Grade)
            printStudent(students[i]);
    console.log("\n");
};