
    print("Test Scenario 1.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"S\" \r")
    result = control.choose_action(lt_ct, gt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "S":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 2.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"W\" \r")
    result = control.choose_action(gt_ct, lt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "W":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 3.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"N\" \r")
    result = control.choose_action(gt_ct, gt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 4.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"E\" \r")
    result = control.choose_action(gt_ct, gt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 5.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"SW\" \r")
    result = control.choose_action(lt_ct, lt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "SW":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 6.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"E or W\" \r")
    result = control.choose_action(lt_ct, gt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E or W":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 7.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"SE\" \r")
    result = control.choose_action(lt_ct, gt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "SE":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 8.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"NW\" \r")
    result = control.choose_action(gt_ct, lt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "NW":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 9.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"N or S\" \r")
    result = control.choose_action(gt_ct, lt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N or S":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 10.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"NE\" \r")
    result = control.choose_action(gt_ct, gt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "NE":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 11.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"S\" \r")
    result = control.choose_action(lt_ct, lt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "S":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 12.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"W\" \r")
    result = control.choose_action(lt_ct, lt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "W":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 13.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"E\" \r")
    result = control.choose_action(lt_ct, gt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 14.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"N\" \r")
    result = control.choose_action(gt_ct, lt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 15.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"Continue\" \r")
    result = control.choose_action(gt_ct, gt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "Continue":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("Test Scenario 16.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"Trapped\" \r")
    result = control.choose_action(lt_ct, lt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "Trapped":
        print("\tFailed!")
    else:
        passed_tests += 1
        print("\tPassed!")

    print("\nYour function has passed in", passed_tests, "test scenarios out of 16.")


if __name__ == "__main__":
    # Executes the main method only if run as a script. Will not
    # execute main() if only parts of this file are imported in
    # to another file.
    main()
