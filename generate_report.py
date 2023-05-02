from junitparser import JUnitXml, TestCase, TestSuite, Properties

if __name__ == '__main__':
    report = JUnitXml()
    testsuite = TestSuite("Scan Details")
    testsuite.add_property('Name', "scan_name")
    testsuite.add_property('ID', "sdfg23456vbj678bn")
    testsuite.add_property('Env', "Prod")
    report.add_testsuite(testsuite)
    report.write("report.xml")