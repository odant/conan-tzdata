# The Time Zone Database Conan package
# Dmitriy Vetutnev, ODANT 2018


from conans import ConanFile


class HelloPythonConan(ConanFile):
    name = "tzdata"
    version = "2018e"
    license = "MIT license"
    description = "The Time Zone Database https://www.iana.org/time-zones"
    url = "https://github.com/odant/conan-tzdata"
    exports = "tzdata/*"
    build_policy = "missing"

    def package(self):
        self.copy("*", keep_path=True)

