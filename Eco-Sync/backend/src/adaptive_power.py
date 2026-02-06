def decide(predicted_traffic):
    if predicted_traffic is None:
        return 100

    if predicted_traffic < 5:
        return 30
    elif predicted_traffic < 20:
        return 50
    elif predicted_traffic < 50:
        return 75
    else:
        return 100
