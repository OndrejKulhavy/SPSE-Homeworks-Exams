def recommend_clothes(is_sunny, is_windy, is_visible):
    if is_sunny and not is_windy and not is_visible:
        print("The weather is good and there is no need for an umbrella")
    elif (not is_visible or not is_sunny) and not is_windy:
        print("The weather is not good and I suggest to take an umbrella")
    elif is_windy and not is_sunny:
        if is_visible:
            print("I suggest to take a hat")
        else:
            print("I suggest to take reflective clothing")


