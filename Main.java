import java.util.*;

import StudentAnalyzer.Student;

public class Main {
    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        Map<String, Integer> scores1 = new HashMap<>();
        scores1.put("Math", 90);
        scores1.put("Physics", 85);

        Map<String, Integer> scores2 = new HashMap<>();
        scores2.put("Math", 95);
        scores2.put("Chemistry", 80);

        Map<String, Integer> scores3 = new HashMap<>();
        scores3.put("Physics", 88);
        scores3.put("Chemistry", 92);

        students.add(new Student(1, "Alice",
                Arrays.asList("Math", "Physics"), scores1));

        students.add(new Student(2, "Bob",
                Arrays.asList("Math", "Chemistry"), scores2));

        students.add(new Student(3, "Charlie",
                Arrays.asList("Physics", "Chemistry"), scores3));

        System.out.println("Top 2 Students:");
        System.out.println(StudentPerformanceAnalyzer.getTopNStudents(students, 2));

        System.out.println("\nAverage Per Course:");
        System.out.println(StudentPerformanceAnalyzer.getAverageScorePerCourse(students));

        System.out.println("\nUnique Courses:");
        System.out.println(StudentPerformanceAnalyzer.getAllUniqueCourses(students));
    }
}
