package AdvanceProgX.Assignment06;

import java.util.*;

public class Main {
    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        students.add(new Student(
                1,
                "Alice",
                Arrays.asList("Math", "Physics"),
                new HashMap<String, Integer>() {{
                    put("Math", 85);
                    put("Physics", 90);
                }}
        ));

        students.add(new Student(
                2,
                "Bob",
                Arrays.asList("Math", "Chemistry"),
                new HashMap<String, Integer>() {{
                    put("Math", 75);
                    put("Chemistry", 80);
                }}
        ));

        students.add(new Student(
                3,
                "Charlie",
                Arrays.asList("Physics", "Chemistry"),
                new HashMap<String, Integer>() {{
                    put("Physics", 95);
                    put("Chemistry", 85);
                }}
        ));

        System.out.println("Top 2 Students:");
        System.out.println(StudentAnalyzer.getTopNStudents(students, 2));

        System.out.println("\nAverage Score Per Course:");
        System.out.println(StudentAnalyzer.getAverageScorePerCourse(students));

        System.out.println("\nAll Unique Courses:");
        System.out.println(StudentAnalyzer.getAllUniqueCourses(students));
    }
}