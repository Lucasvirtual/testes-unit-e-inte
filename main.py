def login():

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


if login():
    from controllers.ProdutoController import ProdutoController

    app = True
    while app:
        app = ProdutoController.exibir_menu()
        if app == False:
            print('\n\n\n\nO programa será finalizado')