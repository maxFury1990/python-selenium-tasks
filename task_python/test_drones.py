import logging


def check_connection(network, first_friend, second_friend):
    """
    Take each value in drones pair and find relations in their network
    """
    checked = {first_friend}
    found_friends = [first_friend]
    while found_friends:
        logging.info(f"select the name of drone and keep it for the forward comparison")
        selected_drone_name = found_friends.pop()
        if selected_drone_name == second_friend:
            return True
        for index in network:
            logging.info(f"find related drone in pair {index} for drone {selected_drone_name} "
                         f"if it doesn't interrupt process")
            if selected_drone_name in index:
                logging.info("if relation was found cut the value and add to found friends")
                index = index.replace(selected_drone_name, '').replace('-', '')
                logging.info("if drone not in checked list skip it otherwise add to this list")
                if index not in checked:
                    found_friends.append(index)
                    checked.add(index)
    return False


def test_drones():
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3"))
    print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout"))