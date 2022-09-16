# This is a sample Python script.do  appium  import  webdriver
# de  apio . webdriver . comum . appiumby  import  AppiumBy
# importar  pytest
#
# maiúsculas  = {}
# caps [ "platformName" ] =  "Android"
# caps [ "appium:platformVersion" ] =  "9.0"
# caps [ "browserName" ] =  ""
# caps [ "appium:appiumVersion" ] =  "1.22.0"
# caps [ "appium:deviceName" ] =  "Samsung Galaxy S9 FHD GoogleAPI Emulator"
# caps [ "appium:deviceOrientation" ] =  "retrato"
# caps [ "appium:app" ] =  "storage:filename=Calculator_v8.2 (453324893)_apkpure.com.apk"
# caps [ "appium:appPackage" ] =  "com.google.android.calculator"
# caps [ "appium:appActivity" ] =  "com.android.calculator2.Calculator"
# caps [ "appium:ensureWebviewsHavePages" ] =  Verdadeiro
# caps [ "appium:nativeWebScreenshot" ] =  Verdadeiro
# caps [ "appium:newCommandTimeout" ] =  0
# caps [ "appium:connectHardwareKeyboard" ] =  Verdadeiro
#
# if  __name__  ==  '__main__' :   # aciona o script
#
#     # def testar_somar_dois_numeros():
#
#     # conexao com o saucelabs, aponta para datacenter, meu usuario e chave (ocultos)
#     driver  =  webdriver . Remoto ( "segredo" , caps )
#
#     # o roteiro gerado automaticamente pelo appium não funcionou como demonstrado no vídeo pelo professor.
#     # revirei na internet e descobri que a sintaxe mudou um pouco
#     # antes se usava driver.find_element_by_accessibility_etc) e agora é como colocado abaixo
#
#     resultado_esperado  =  '13'
#
#     # script que faz um soma
#     botao_8  =  motorista . find_element ( AppiumBy . ACCESSIBILITY_ID , '8' )
#     botao_8 . clique ()
#     botao_soma  =  motorista . find_element ( AppiumBy . ACCESSIBILITY_ID , 'mais' )
#     botao_soma . clique ()
#     botao_5  =  motorista . find_element ( AppiumBy . ACCESSIBILITY_ID , '5' )
#     botao_5 . clique ()
#     botao_igual  =  motorista . find_element ( AppiumBy . ACCESSIBILITY_ID , 'igual' )
#     botao_igual . clique ()
#     resultado_final  =  driver . find_element ( AppiumBy . ID , 'com.google.android.calculator:id/result_final' )
#
#     print ( f'Resultado final = { resultado_final . text }  \n Resultado esperado = { resultado_esperado } ' )
#
#     assert  resultado_final . texto  ==  resultado_esperado
#
#     motorista . sair ()
