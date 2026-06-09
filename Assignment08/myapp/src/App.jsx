import { useState } from "react";
import "./App.css";

function App() {
  const [studentsMap, setStudentsMap] = useState(
    new Map([
      [
        1,
        {
          id: 1,
          name: "Alice",
          enrolledCourses: new Set(["Math", "Physics"]),
          gpa: 3.8,
        },
      ],
      [
        2,
        {
          id: 2,
          name: "Bob",
          enrolledCourses: new Set(["Chemistry", "Math"]),
          gpa: 3.5,
        },
      ],
      [
        3,
        {
          id: 3,
          name: "Charlie",
          enrolledCourses: new Set(["Physics"]),
          gpa: 3.9,
        },
      ],
    ])
  );

  const [name, setName] = useState("");
  const [courses, setCourses] = useState("");
  const [gpa, setGpa] = useState("");
  const [filterCourse, setFilterCourse] = useState("");

  const addStudent = () => {
    if (!name || !courses || !gpa) return;

    const newId =
      studentsMap.size > 0
        ? Math.max(...Array.from(studentsMap.keys())) + 1
        : 1;

    const newStudent = {
      id: newId,
      name,
      enrolledCourses: new Set(
        courses.split(",").map((course) => course.trim())
      ),
      gpa: parseFloat(gpa),
    };

    const updatedMap = new Map(studentsMap);
    updatedMap.set(newId, newStudent);

    setStudentsMap(updatedMap);

    setName("");
    setCourses("");
    setGpa("");
  };

  const removeStudent = (id) => {
    const updatedMap = new Map(studentsMap);
    updatedMap.delete(id);
    setStudentsMap(updatedMap);
  };

  const students = Array.from(studentsMap.values());

  const sortedStudents = [...students].sort((a, b) => b.gpa - a.gpa);

  const uniqueCourses = students.reduce((acc, student) => {
    student.enrolledCourses.forEach((course) => acc.add(course));
    return acc;
  }, new Set());

  const filteredStudents = filterCourse
    ? students.filter((student) =>
        student.enrolledCourses.has(filterCourse)
      )
    : sortedStudents;

  return (
    <div className="container">
      <h1>Course Enrollment Dashboard</h1>

      <div className="form">
        <input
          type="text"
          placeholder="Student Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="text"
          placeholder="Courses (comma separated)"
          value={courses}
          onChange={(e) => setCourses(e.target.value)}
        />

        <input
          type="number"
          step="0.1"
          placeholder="GPA"
          value={gpa}
          onChange={(e) => setGpa(e.target.value)}
        />

        <button onClick={addStudent}>Add Student</button>
      </div>

      <div className="filter">
        <input
          type="text"
          placeholder="Filter by Course"
          value={filterCourse}
          onChange={(e) => setFilterCourse(e.target.value)}
        />
      </div>

      <h2>All Unique Courses</h2>
      <ul>
        {Array.from(uniqueCourses).map((course, index) => (
          <li key={index}>{course}</li>
        ))}
      </ul>

      <h2>Students (Sorted by GPA)</h2>
      {filteredStudents.map((student) => (
        <div key={student.id} className="student-card">
          <h3>{student.name}</h3>
          <p>ID: {student.id}</p>
          <p>GPA: {student.gpa}</p>
          <p>
            Courses:{" "}
            {Array.from(student.enrolledCourses).join(", ")}
          </p>
          <button onClick={() => removeStudent(student.id)}>
            Remove
          </button>
        </div>
      ))}

      <div className="complexity">
        <h3>Time Complexity</h3>
        <p>
          Filtering students by course uses the filter() method and checks
          membership in a Set using has().
        </p>
        <p>
          Complexity: O(n), where n is the number of students.
        </p>
      </div>
    </div>
  );
}

export default App;