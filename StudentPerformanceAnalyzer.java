import java.util.*;
import java.util.stream.*;

import StudentAnalyzer.Student;

public class StudentPerformanceAnalyzer {

    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, List<Integer>> courseScores = new HashMap<>();

        for (Student student : students) {
            for (String course : student.getCourses()) {

                int score = student.getScores().getOrDefault(course, 0);

                courseScores
                        .computeIfAbsent(course, k -> new ArrayList<>())
                        .add(score);
            }
        }

        return courseScores.entrySet()
                .stream()
                .collect(Collectors.toMap(
                        Map.Entry::getKey,
                        entry -> entry.getValue()
                                .stream()
                                .mapToInt(Integer::intValue)
                                .average()
                                .orElse(0.0)
                ));
    }

    public static Set<String> getAllUniqueCourses(List<Student> students) {

        Set<String> uniqueCourses = new HashSet<>();

        students.stream()
                .map(Student::getCourses)
                .forEach(uniqueCourses::addAll);

        return uniqueCourses;
    }
}
