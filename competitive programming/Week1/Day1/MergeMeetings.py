def merge_meets(meetings_list):
    if len(meetings_list) < 2:
        raise IndexError('Error Less than two numbers')

    sorted_meetings = sorted(meetings_list)
    new_meetings_list = [sorted_meetings[0]]

    for meeting_start, meeting_end in sorted_meetings[1:]:
        merged_start, merged_end = new_meetings_list[-1]

        if (meeting_start <= merged_end):
            new_meetings_list[-1] = (merged_start,max(merged_end,meeting_end))
        else:
            new_meetings_list.append((meeting_start, meeting_end))

    return new_meetings_list

if __name__ == '__main__':
    input = eval(input())

    try:
        print(str(merge_meets(input)))
    except IndexError:
        print("Error Less than two numbers")