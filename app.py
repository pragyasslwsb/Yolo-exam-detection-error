
def detect_behaviors(objects, high_priority, person_count, head_turn):
    object_set = set(objects)
    high_set = set(high_priority)

    phone_detected = any(label in high_set for label in ["cell phone", "phone", "smartphone", "mobile phone"])
    laptop_detected = any(label in high_set for label in ["laptop", "tablet", "computer"])
    smart_watch_detected = any(label in high_set for label in ["smart watch", "watch", "wristwatch"])
    earphones_detected = any(label in high_set for label in ["earphones", "earphone", "headphones", "ear buds"])
    water_bottle_detected = any(label in high_set for label in ["water bottle", "bottle", "drink", "cup"])

    hand_detected = any(label in object_set for label in ["hand", "hands", "arm", "arms"])
    pocket_like = any(label in object_set for label in ["pocket", "coat", "bag", "sleeve"])

    drinking_water = water_bottle_detected
    head_itching = False

    # Eye movement approximation using head direction / sideways glance
    side_glance = head_turn in ["left", "right", "sideways"]
    eye_movement = side_glance and person_count > 0
    repeated_eye_movement = side_glance and person_count > 1

    # Hidden hand movement approximation
    hand_below_desk = hand_detected and not water_bottle_detected
    repeated_hand_movements = hand_detected and person_count > 0 and side_glance

    # Pocket concealment approximation
    hand_in_pocket = hand_detected and pocket_like
    repeated_hand_in_pocket = hand_in_pocket and side_glance and person_count > 0

    return {
        "phone": phone_detected,
        "laptop": laptop_detected,
        "smart_watch": smart_watch_detected,
        "earphones": earphones_detected,
        "water_bottle": water_bottle_detected,
        "drinking_water": drinking_water,
        "head_itching": head_itching,
        "side_glance": side_glance,
        "eye_movement": eye_movement,
        "repeated_eye_movement": repeated_eye_movement,
        "hand_below_desk": hand_below_desk,
        "repeated_hand_movements": repeated_hand_movements,
        "hand_in_pocket": hand_in_pocket,
        "repeated_hand_in_pocket": repeated_hand_in_pocket,
        "multiple_people": person_count > 1,
    }
    

   


    

        
       


   
               
    