import MetaTrader5

# Function to start MetaTrader
def start_mt5(project_settings):
    """
    Function to start mt5

    Args:
        project_settings (json): json object with basic info about mt5 server, username, etc.
    """
    # Ensure that all variables are set/formatted to the correct type
    username = project_settings['mt5']['username']
    username = int(username)
    password = project_settings['mt5']['password']
    server = project_settings['mt5']['server']
    location = project_settings['mt5']['mt5_pathway']

    # Attempt to initialize MT5
    mt5_init = False
    try:
        mt5_init = MetaTrader5.initialize(
            login=username
            password=password
            server=server
            path=mt5_pathway
        )
    # Handling erros
    except Exception as e:
        print(f"Error initializing MetaTrader5: {e}")
        mt5_init = False
    
    # If MT5 initialized, attemp to login
    mt5_login = False
    if mt5_init:
        # Attempt to login
        try:
            mt5_login = MetaTrader5.login(
                login=username
                password=password,
                server=server
            )
        # Handle exception
        except Exception as e:
                print(f"Error logging into MT%: {e}")
                mt5_login = False
    # Return true if user was able of login to MT5
    if mt5_login:
        return True
    # Default outcome
    return False
