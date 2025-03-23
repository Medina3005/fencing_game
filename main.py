
import module1_choose_fencing_gear as gear
import module2_warm_up_routine as warmup
import module3_group_stage_matches as group
import module4_first_elimination_match as elim
import module5_face_your_rival as rival
import module6_determine_ending as ending
import module7_train_with_coach as coach
import module8_the_championship_match as final

def start_game():
    print("🏆 Welcome to the Fencing Championship Quest! 🏆")

    selected_gear = gear.choose_gear()
    print(f"You selected: {selected_gear}")

    warmup.warm_up()

    qualified = group.group_stage()
    if not qualified:
        return

    coach.train_with_coach()

    if elim.elimination_match():
        if rival.face_rival():
            won_final = final.championship_match()
            ending.determine_ending(won_final)
        else:
            ending.determine_ending(False)
    else:
        print("Game Over.")

if __name__ == "__main__":
    start_game()
