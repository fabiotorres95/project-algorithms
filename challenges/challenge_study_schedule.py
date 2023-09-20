def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    result = 0
    for student in permanence_period:
        if (
            type(student) is not tuple
            or type(student[0]) is not int
            or type(student[1]) is not int
        ):
            return None
        if student[0] <= target_time and student[1] >= target_time:
            result += 1

    return result
