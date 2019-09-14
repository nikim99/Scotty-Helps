var departments = new Array('Architecture', 'Art', 
'BXA Intercollege Degree Programs', 'Biological Sciences', 
'Biomedical Engineering', 'Business Administration', 'CFA Interdisciplinary', 
'CIT Interdisciplinary', 'Carnegie Mellon University-Wide Studies', 
'Chemical Engineering', 'Chemistry', 'Civil & Environmental Engineering', 
'Creative Enterprise:Sch of Pub Pol & Mgt', 'Design', 
'Dietrich College Information Systems', 
'Drama', 'Economics', 'Electrical & Computer Engineering', 
'Engineering & Public Policy', 'English', 
'General Dietrich College', 'History', 
'Information & Communication Technology', 'Information Networking Institute', 
'Information Systems:Sch of IS & Mgt', 'Institute for Politics and Strategy', 
'MCS Interdisciplinary', 
'Materials Science & Engineering', 'Mathematical Sciences', 
'Mechanical Engineering',
'Modern Languages', 'Music', 'Philosophy', 
'Physical Education', 'Physics', 'Psychology', 
'SCS: Computational Biology', 'SCS Interdisciplinary', 
'SCS: Computer Science', 'SCS: Human-Computer Interaction', 
'SCS: Institute for Software Research', 'SCS: Language Technologies Institute', 
'SCS: Machine Learning', 'SCS: Robotics', 'Social & Decision Sciences', 
'Statistics and Data Science', 'StuCo (Student Led Courses)', 
'Tepper School of Business');

var units = new Array('0-5', '6-10', '11-15', '16-20', '21+');
var level = new Array("Freshman", "Sophomore", "Junior", "Senior", 
"Undergraduate", "Graduate");
var sems = new Array("Fall", "Spring", "Summer 1", "Summer 2");
var type = new Array("Core", "Science", "Humanities", "Math", "Computer Science");

var departmentDD = document.getElementById("department");
var unitsDD = document.getElementById("units");
var levelDD = document.getElementById("level");
var semsDD = document.getElementById("semester");
var typeDD = document.getElementById("type");

for (var i = 0; i < departments.length; ++i) {
    departmentDD[departmentDD.length] = new Option(departments[i],departments[i]);
}

for (var i = 0; i < units.length; ++i) {
    unitsDD[unitsDD.length] = new Option(units[i], units[i]);
}

for (var i = 0; i < level.length; ++i) {
    levelDD[levelDD.length] = new Option(level[i], level[i]);
}

for (var i = 0; i < sems.length; ++i) {
    semsDD[semsDD.length] = new Option(sems[i], sems[i]);
}

for (var i = 0; i < type.length; ++i) {
    typeDD[typeDD.length] = new Option(type[i], type[i]);
}

var departUser = null;
var unitsUser = null;
var levelUser = null;
var semsUser = null;
var typeUser = null;


function goToTable() {
    departUser = departmentDD.options[departmentDD.selectedIndex].text;
    unitsUser = unitsDD.options[unitsDD.selectedIndex].text;
    levelUser = levelDD.options[levelDD.selectedIndex].text;
    semsUser = semsDD.options[semsDD.selectedIndex].text;
    typeUser = typeDD.options[typeDD.selectedIndex].text;
    window.location.href='courses?department='+departUser + '&units='+unitsUser+
        '&year='+levelUser+'&sems='+semsUser+'&type='+typeUser;

}

function getUserInput() {
    var departUser = departmentDD.options[departmentDD.selectedIndex].text;
    var unitsUser = unitsDD.options[unitsDD.selectedIndex].text;
    var levelUser = levelDD.options[levelDD.selectedIndex].text;
    var semsUser = semsDD.options[semsDD.selectedIndex].text;
    var typeUser = typeDD.options[typeDD.selectedIndex].text;
}

