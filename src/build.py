from cx_Freeze import setup, Executable

files = ["icons", "test"]

target = Executable(
    script="GUI.py",
    base="Win32GUI",
    icon="icons/logo.ico"
)
setup(
    name="FSEI-M TimeTabler",
    version="1.0",
    description="timetable generator built for the faculty of exact sciences and computer science by Belhadj Ahmed "
                "Walid",
    author="Belhadj Ahmed Walid",
    options={"build_exe": {"include_files": files}},
    executables=[target]
)
