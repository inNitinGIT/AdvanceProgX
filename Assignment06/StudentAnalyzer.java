package AdvanceProgX.Assignment06;

import java.util.*;
import java.util.stream.*;

public class StudentAnalyzer {

    // Get Top N Students (sorted by average descending)
    public static List<Student> getTopNStudents(List<Student> students, int n) {

        return students.stream()
                .sorted(
                        Comparator.comparingDouble(Student::getAverageScore)
                                .reversed()
                )
                .limit(n)
                .collect(Collectors.toList());
    }

    // Average Score Per Course
    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .distinct()
                .collect(Collectors.toMap(
                        course -> course,
                        course -> students.stream()
                                .mapToInt(s ->
                                        s.getScores().getOrDefault(course, 0)
                                )
                                .average()
                                .orElse(0.0)
                ));
    }

    // Get All Unique Courses
    public static Set<String> getAllUniqueCourses(List<Student> students) {

        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .collect(Collectors.toCollection(HashSet::new));
    }
}