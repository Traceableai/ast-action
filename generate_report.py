from junitparser import JUnitXml, TestCase, TestSuite

if __name__ == '__main__':
    report = JUnitXml()
    testsuite = TestSuite("Scan Details")
    testsuite.add_property('Name', "scan_name")
    testsuite.add_property('ID', "sdfg23456vbj678bn")
    testsuite.add_property('Env', "Prod")
    testcase = TestCase("my-test")
    testcase.add_property('Severity', "CRITICAL")
    testsuite.add_testcase(testcase)
    report.add_testsuite(testsuite)
    report.write("report.xml")