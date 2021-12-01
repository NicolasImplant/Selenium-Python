from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner, runner
from assertions import AssertionsTest
from searchtests2 import SearchTests

# Variables para cargar los casos de prueba

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# Construir la Suit de pruebas a través del código

smoke_test = TestSuite([assertions_test, search_test])

# Indicar los parametros para generar el reporte a través de un diccionario

kwargs = {
    "output": 'smoke-report'
}

# Se crea la variable runner en donde se generará el reporte como lo necesitamos

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)