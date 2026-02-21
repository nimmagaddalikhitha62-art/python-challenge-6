playlist = list(map(int, input("Enter song durations separated by space: ").split()))

if any(duration <= 0 for duration in playlist):
    print("Invalid Playlist: Durations must be greater than 0")
else:
    total_duration = sum(playlist)
    number_of_songs = len(playlist)
    repetitive = False
    for duration in playlist:
        if playlist.count(duration) > 1:
            repetitive = True
            break
    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs"
    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Consider shortening the playlist"
    elif repetitive:
        category = "Repetitive Playlist"
        recommendation = "Add variety"
    else:
        variation = max(playlist) - min(playlist)
        if variation > 0:
            category = "Balanced Playlist"
            recommendation = "Good listening session"
        else:
            category = "Irregular Playlist"
            recommendation = "Adjust song selection"
    print("Total Duration:", total_duration, "seconds")
    print("Songs:", number_of_songs)
    print("Category:", category)
    print("Recommendation:", recommendation)