def calculator():
  motd = """

  ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
  ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
  ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
  ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
  ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                      v1.0
                            type "𝐡𝐞𝐥𝐩" to get started
  """

  def mainframe(x):
    return x 


  
  print(mainframe(motd))

  def helpfunc():
    helpcmd = input("")

    if helpcmd == "help":
      print("""
      Supported commands are Exponents, Multiplication, Division, Addition and Subtraction
      In order to Multiply type 'multiply' then 'n1' then 'n2'
      In order to Divide type 'divide' then 'n1' then 'n2'
      In order to Add type 'add' then 'n1' then 'n2'
      In order to Subtract type 'subtract' then 'n1' then 'n2'
      
      """)
    else:
      print("Invalid command! Try again")
      helpfunc()

  helpfunc()

  proccess = input("")
  n1 = input("")
  n2 = input("")

  def calc(a, b, c):
    if a == "add":
      return b + c
    elif a == "subtract":
      return b - c
    elif a == "multiply":
      return b * c
    elif a == "subtract":
      return b / c
    else:
      return "Error, Try again!"
      calc(a, b, c)
    
  print(calc(proccess, n1, n2))
  calculator()

calculator()