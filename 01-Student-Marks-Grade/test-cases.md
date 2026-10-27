# Test Cases: Student Marks and Grade Calculator

| Test | Input | Expected result |
|---|---|---|
| 1 | Subjects: 3; marks: 95, 85, 90 | Total 270, average 90.00, grade A |
| 2 | Subjects: 2; marks: 75, 65 | Total 140, average 70.00, grade C |
| 3 | Subjects: 2; marks: 20, 30 | Total 50, average 25.00, grade F |
| 4 | Subjects: 0 | Error: number of subjects must be positive |
| 5 | Subjects: 2; first mark: 110 | Invalid marks message |

## Sample run

Input:
```text
Enter number of subjects: 3
Enter marks for subject 1 (0-100): 95
Enter marks for subject 2 (0-100): 85
Enter marks for subject 3 (0-100): 90
```

Expected output:
```text
----- Student Result -----
Total Marks: 270
Average: 90.00
Grade: A
```

Run the program in PyCharm and add a screenshot of the actual output to your final report.
