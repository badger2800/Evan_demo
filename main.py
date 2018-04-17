import sel_code


sel_code.browser_setup()
sel_code.login()

# TODO Change parameter, depending on the file you are pulling in.
sel_code.category_choice("Productos")

# TODO Build file loop here
sel_code.import_files()

sel_code.browser_close()