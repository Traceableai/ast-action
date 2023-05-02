from junitparser import JUnitXml, TestCase, TestSuite, Properties

if __name__ == '__main__':
    report = JUnitXml()
    testsuite = TestSuite("Scan Details")
    testsuite.properties = Properties()
    testsuite.properties.add_property('Name', "scan_name")
    testsuite.properties.add_property('ID', "sdfg23456vbj678bn")
    testsuite.properties.add_property('Env', "Prod")
    report.add_testsuite(testsuite)
    with open("report.xml", "w") as f:
        report.write(f)