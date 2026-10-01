class RiskEngine:
    def calculate_risk(
        self,
        phone=False,
        laptop=False,
        multiple_people=False,
        head_turn="forward",
        side_glance=False,
        hand_below_desk=False,
        repeated_hand_movements=False,
        smart_watch=False,
        earphones=False,
        water_bottle=False,
        drinking_water=False,
        peer_look_seconds=0,
        head_itching=False,
        eye_movement=False,
        repeated_eye_movement=False,
        hand_in_pocket=False,
        repeated_hand_in_pocket=False
    ):
        score = 0
        events = []

        if drinking_water:
            pass

        if head_itching:
            pass

        if phone:
            score += 35
            events.append("Phone detected")

        if smart_watch:
            score += 20
            events.append("Smart watch detected")

        if earphones:
            score += 20
            events.append("Earphones detected")

        if laptop:
            score += 25
            events.append("Laptop or tablet detected")

        if multiple_people and side_glance:
            score += 12
            events.append("Student is looking sideways at others")

        if eye_movement or repeated_eye_movement:
            score += 18
            events.append("Repeated eye movement / side eye suspicious activity")

        if hand_below_desk:
            score += 25
            events.append("Hands below desk / hidden movement detected")

        if hand_in_pocket:
            score += 22
            events.append("Hand hidden in pocket / suspicious concealment")

        if repeated_hand_in_pocket:
            score += 30
            events.append("Repeated hand-in-pocket suspicious behavior")

        if repeated_hand_movements:
            score += 20
            events.append("Repeated suspicious hand movement detected")

        if peer_look_seconds >= 30 * 60:
            score += 40
            events.append("Student looking at another student for more than 30 minutes")
            events.append("Human verification required")

        if score >= 75:
            level = "HIGH"
        elif score >= 40:
            level = "MEDIUM"
        elif score > 0:
            level = "LOW"
        else:
            level = "NORMAL"

        return score, level, events

        