package AdvanceProgX.Assignment06;

import java.util.*;

public class Student {
    private int id;
    private String name;
    private List<String> courses;
    private Map<String, Integer> scores;

    public Student(int id, String name,
                   List<String> courses,
                   Map<String, Integer> scores) {

        this.id = id;
        this.name = name;
        this.courses = new ArrayList<>(courses);
        this.scores = new HashMap<>(scores);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }

    // Compute average score safely
    public double getAverageScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }

        int total = scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .sum();

        return (double) total / scores.size();
    }

    @Override
    public String toString() {
        return name + " (Avg: " + getAverageScore() + ")";
    }
}