from stegano import lsb

def hide_message(filename, message, output="hidden.png"):
    secret = lsb.hide(str(filename), message)
    secret.save(output)
    return output

def show_message(filename):
    return lsb.reveal(filename)
