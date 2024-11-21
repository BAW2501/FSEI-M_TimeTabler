import streamlit as st

import json

from Def import (
    Faculty,
    Level,
    Module,
    PendingSession,
    Professor,
    Room,
    RoomType,
    Section,
    SessionType,
    Group,
    DataShow,
)


class AppState:
    def __init__(self):
        self.selected_faculty: Faculty =Faculty(name="FSEI-MOSTA")
        self.selected_faculty.list_promo = [Level(name="L1"), Level(name="L2")]
        self.selected_level: Level = self.selected_faculty.list_promo[0]
        self.faculties: list[Faculty] = [self.selected_faculty]

    def save_state(self):
        # Convert the state to JSON-serializable format
        state_dict = {"faculties": [faculty.__dict__ for faculty in self.faculties]}
        st.session_state["app_state"] = json.dumps(state_dict)

    def load_state(self):
        if "app_state" in st.session_state:
            state_dict = json.loads(st.session_state["app_state"])
            self.faculties = [Faculty(**f) for f in state_dict["faculties"]]

    def select_faculty(self, faculty: Faculty):
        self.selected_faculty = faculty

    def select_level(self, level: Level):
        self.selected_level = level


state = AppState()


def initialize_state():
    if "app_state" not in st.session_state:
        state = AppState()
        state.save_state()
    return AppState()


def faculty_crud():
    st.header("Faculty Management")

    # Create
    with st.expander("Add New Faculty"):
        new_faculty_name = st.text_input("Faculty Name")
        if st.button("Create Faculty"):
            if new_faculty_name:
                new_faculty = Faculty(name=new_faculty_name)
                state.faculties.append(new_faculty)
                state.save_state()
                st.success(f"Created faculty: {new_faculty_name}")

    # Read
    st.subheader("Existing Faculties")

    for fac in state.faculties:

        # Display fac info
        col0, col1, col2, col3, col4 = st.columns(5)
        col0.metric("Name:", fac.name)
        col1.metric("Number of Students:", fac.number_students)
        col2.metric("Number of Professors:", fac.number_professors)
        col3.metric("Number of Rooms:", fac.number_rooms)
        if col4.button(f"Select This Faculty", on_click=lambda: state.select_faculty(fac)):
            st.success(f"Selected faculty: {fac.name}")

        # Update
        with col4.expander("Update Faculty"):
            updated_name = st.text_input("New Name", fac.name)
            if st.button("Update"):
                fac.name = updated_name
                state.save_state()
                st.success("Faculty updated successfully")

        # Delete
        if col4.button("Delete Faculty"):
            state.faculties.remove(fac)
            state.save_state()
            st.success("Faculty deleted successfully")
            st.rerun()


def level_crud():
    if state.selected_faculty == None:
        st.warning("Please select a faculty first")
        return

    st.header("Level Management")

    # Create
    with st.expander("Add New Level"):
        new_level_name = st.text_input("Level Name")
        if st.button("Create Level"):
            if new_level_name:
                new_level = Level(name=new_level_name)
                state.selected_faculty.list_promo.append(new_level)
                state.save_state()
                st.success(f"Created level: {new_level_name}")

    # Read
    st.subheader("Existing Levels")
    level_names = [l.name for l in state.selected_faculty.list_promo]
    selected_level_name = st.selectbox("Select Level", level_names)

    if selected_level_name:
        level = next(
            l
            for l in state.selected_faculty.list_promo
            if l.name == selected_level_name
        )
        state.selected_level = level

        # Update
        with st.expander("Update Level"):
            updated_name = st.text_input("New Name", level.name)
            if st.button("Update"):
                level.name = updated_name
                state.save_state()
                st.success("Level updated successfully")

        # Delete
        if st.button("Delete Level"):
            state.selected_faculty.list_promo.remove(level)
            state.save_state()
            st.success("Level deleted successfully")
            st.rerun()


def section_crud():
    if not state.selected_level:
        st.warning("Please select a level first")
        return

    st.header("Section Management")

    # Create
    with st.expander("Add New Section"):
        new_section_number = st.number_input("Section Number", min_value=1)
        nb_groups = st.number_input("Number of Groups", min_value=1)
        students_per_group = st.number_input("Students per Group", min_value=1)

        if st.button("Create Section"):
            groups = [
                Group(number=i + 1, effective=students_per_group)
                for i in range(nb_groups)
            ]
            new_section = Section(number=new_section_number, list_group=groups)
            state.selected_level.list_section.append(new_section)
            state.save_state()
            st.success("Section created successfully")

    # Read
    st.subheader("Existing Sections")
    for section in state.selected_level.list_section:
        with st.expander(f"Section {section.number}"):
            st.write(f"Number of groups: {len(section.list_group)}")
            st.write(f"Students per group: {section.list_group[0].effective}")

            # Update
            new_number = st.number_input("New Section Number", value=section.number)
            new_groups = st.number_input(
                "New Number of Groups", value=len(section.list_group)
            )
            new_students = st.number_input(
                "New Students per Group", value=section.list_group[0].effective
            )

            if st.button(f"Update Section {section.number}"):
                section.number = new_number
                section.list_group = [
                    Group(number=i + 1, effective=new_students)
                    for i in range(new_groups)
                ]
                state.save_state()
                st.success("Section updated successfully")

            # Delete
            if st.button(f"Delete Section {section.number}"):
                state.selected_level.list_section.remove(section)
                state.save_state()
                st.success("Section deleted successfully")
                st.rerun()


def professor_crud():
    if not state.selected_faculty:
        st.warning("Please select a faculty first")
        return

    st.header("Professor Management")

    # Create
    with st.expander("Add New Professor"):
        new_prof_name = st.text_input("Professor Name")
        if st.button("Create Professor"):
            if new_prof_name:
                new_prof = Professor(name=new_prof_name)
                state.selected_faculty.list_profs.append(new_prof)
                state.save_state()
                st.success(f"Created professor: {new_prof_name}")

    # Read
    st.subheader("Existing Professors")
    filter_name = st.text_input("Filter by name")

    filtered_profs = [
        p
        for p in state.selected_faculty.list_profs
        if filter_name.lower() in p.name.lower()
    ]

    for prof in filtered_profs:
        with st.expander(prof.name):
            # Update
            updated_name = st.text_input("New Name", prof.name)
            if st.button(f"Update {prof.name}"):
                prof.name = updated_name
                state.save_state()
                st.success("Professor updated successfully")

            # Delete
            if st.button(f"Delete {prof.name}"):
                state.selected_faculty.list_profs.remove(prof)
                state.save_state()
                st.success("Professor deleted successfully")
                st.rerun()


def room_crud():
    if not state.selected_faculty:
        st.warning("Please select a faculty first")
        return

    st.header("Room Management")

    # Create
    with st.expander("Add New Room"):
        new_room_name = st.text_input("Room Name")
        room_type = st.selectbox("Room Type", [t.value for t in RoomType])
        capacity = st.number_input("Capacity", min_value=1)

        if st.button("Create Room"):
            if new_room_name:
                new_room = Room(
                    name=new_room_name, room_type=RoomType(room_type), capacity=capacity
                )
                state.selected_faculty.list_rooms.append(new_room)
                state.save_state()
                st.success(f"Created room: {new_room_name}")

    # Read
    st.subheader("Existing Rooms")
    filter_type = st.selectbox("Filter by type", ["All"] + [t.value for t in RoomType])
    min_capacity = st.number_input("Minimum capacity", min_value=0)

    filtered_rooms = state.selected_faculty.list_rooms
    if filter_type != "All":
        filtered_rooms = [
            r for r in filtered_rooms if r.room_type == RoomType(filter_type)
        ]
    filtered_rooms = [r for r in filtered_rooms if r.capacity >= min_capacity]

    for room in filtered_rooms:
        with st.expander(f"{room.name} ({room.room_type.value})"):
            # Update
            updated_name = st.text_input("New Name", room.name)
            updated_type = st.selectbox(
                "New Type",
                [t.value for t in RoomType],
                index=[t.value for t in RoomType].index(room.room_type.value),
            )
            updated_capacity = st.number_input("New Capacity", value=room.capacity)

            if st.button(f"Update {room.name}"):
                room.name = updated_name
                room.room_type = RoomType(updated_type)
                room.capacity = updated_capacity
                state.save_state()
                st.success("Room updated successfully")

            # Delete
            if st.button(f"Delete {room.name}"):
                state.selected_faculty.list_rooms.remove(room)
                state.save_state()
                st.success("Room deleted successfully")
                st.rerun()


def module_crud():
    if not state.selected_level:
        st.warning("Please select a level first")
        return

    st.header("Module Management")

    # Create
    with st.expander("Add New Module"):
        new_module_name = st.text_input("Module Name")
        abbreviation = st.text_input("Abbreviation")
        semester = st.number_input("Semester", min_value=1, max_value=2)
        n_lectures = st.number_input("Number of Lectures", min_value=0)
        n_tutorials = st.number_input("Number of Tutorials", min_value=0)
        n_labs = st.number_input("Number of Labs", min_value=0)

        if st.button("Create Module"):
            if new_module_name and abbreviation:
                new_module = Module(
                    name=new_module_name,
                    abbreviation=abbreviation,
                    semester=semester,
                    number_of_lectures=n_lectures,
                    number_of_tutorials=n_tutorials,
                    number_of_labs=n_labs,
                )
                state.selected_level.curriculum.append(new_module)
                state.save_state()
                st.success(f"Created module: {new_module_name}")

    # Read
    st.subheader("Curriculum")
    semester_filter = st.selectbox("Filter by semester", [0, 1, 2])

    filtered_modules = state.selected_level.curriculum
    if semester_filter > 0:
        filtered_modules = [
            m for m in filtered_modules if m.semester == semester_filter
        ]

    for module in filtered_modules:
        with st.expander(f"{module.name} ({module.abbreviation})"):
            # Display details
            st.write(f"Semester: {module.semester}")
            st.write(f"Lectures: {module.number_of_lectures}")
            st.write(f"Tutorials: {module.number_of_tutorials}")
            st.write(f"Labs: {module.number_of_labs}")

            # Update
            updated_name = st.text_input("New Name", module.name)
            updated_abbr = st.text_input("New Abbreviation", module.abbreviation)
            updated_semester = st.number_input("New Semester", value=module.semester)
            updated_lectures = st.number_input(
                "New Number of Lectures", value=module.number_of_lectures
            )
            updated_tutorials = st.number_input(
                "New Number of Tutorials", value=module.number_of_tutorials
            )
            updated_labs = st.number_input(
                "New Number of Labs", value=module.number_of_labs
            )

            if st.button(f"Update {module.name}"):
                module.name = updated_name
                module.abbreviation = updated_abbr
                module.semester = updated_semester
                module.number_of_lectures = updated_lectures
                module.number_of_tutorials = updated_tutorials
                module.number_of_labs = updated_labs
                state.save_state()
                st.success("Module updated successfully")

            # Delete
            if st.button(f"Delete {module.name}"):
                state.selected_level.curriculum.remove(module)
                state.save_state()
                st.success("Module deleted successfully")
                st.rerun()


# Continuing from the provided code...


def pending_session_crud():
    if not state.selected_level:
        st.warning("Please select a level first")
        return

    st.header("Pending Session Management")

    # Create
    with st.expander("Add New Pending Session"):
        # Professor selection
        selected_prof = st.selectbox(
            "Professor", state.selected_faculty.list_profs, format_func=lambda p: p.name
        )

        # Module selection
        selected_module = st.selectbox(
            "Module", state.selected_level.curriculum, format_func=lambda m: m.name
        )

        # Section/Group selection
        attendance_type = st.selectbox("Attendance Type", ["Section", "Group"])
        if attendance_type == "Section":
            attendance = st.selectbox(
                "Section",
                state.selected_level.list_section,
                format_func=lambda s: f"Section {s.number}",
            )
        else:
            flattened_groups = [
                g for s in state.selected_level.list_section for g in s.list_group
            ]
            attendance = st.selectbox(
                "Group", flattened_groups, format_func=lambda g: f"Group {g.number}"
            )

        session_type = st.selectbox("Session Type", [t.value for t in SessionType])

        if st.button("Create Pending Session"):
            new_pending_session = PendingSession(
                prof=selected_prof,
                module=selected_module,
                attendance=attendance,
                session_type=SessionType(session_type),
            )
            state.selected_level.required_sessions.append(new_pending_session)
            state.save_state()
            st.success("Pending session created successfully")

    # Read & Filter
    st.subheader("Existing Pending Sessions")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_prof = st.selectbox(
            "Filter by Professor",
            ["All"] + [p.name for p in state.selected_faculty.list_profs],
        )
    with col2:
        filter_module = st.selectbox(
            "Filter by Module",
            ["All"] + [m.name for m in state.selected_level.curriculum],
        )
    with col3:
        filter_type = st.selectbox(
            "Filter by Session Type", ["All"] + [t.value for t in SessionType]
        )

    # Apply filters
    filtered_sessions = state.selected_level.required_sessions
    if filter_prof != "All":
        filtered_sessions = [s for s in filtered_sessions if s.prof.name == filter_prof]
    if filter_module != "All":
        filtered_sessions = [
            s for s in filtered_sessions if s.module.name == filter_module
        ]
    if filter_type != "All":
        filtered_sessions = [
            s for s in filtered_sessions if s.session_type.value == filter_type
        ]

    # Display sessions
    for session in filtered_sessions:
        with st.expander(
            f"Session: {session.module.name} - {session.session_type.value}"
        ):
            # Display current details
            st.write(f"Professor: {session.prof.name}")
            st.write(
                f"Attendance: {'Section' if isinstance(session.attendance, Section) else 'Group'} {session.attendance.number}"
            )

            # Update form
            updated_prof = st.selectbox(
                "New Professor",
                state.selected_faculty.list_profs,
                format_func=lambda p: p.name,
                index=state.selected_faculty.list_profs.index(session.prof),
            )

            updated_module = st.selectbox(
                "New Module",
                state.selected_level.curriculum,
                format_func=lambda m: m.name,
                index=state.selected_level.curriculum.index(session.module),
            )

            updated_type = st.selectbox(
                "New Session Type",
                [t.value for t in SessionType],
                index=[t.value for t in SessionType].index(session.session_type.value),
            )

            if st.button(f"Update Session"):
                session.prof = updated_prof
                session.module = updated_module
                session.session_type = SessionType(updated_type)
                state.save_state()
                st.success("Session updated successfully")

            if st.button(f"Delete Session"):
                state.selected_level.required_sessions.remove(session)
                state.save_state()
                st.success("Session deleted successfully")
                st.rerun()


def datashow_crud():
    if not state.selected_faculty:
        st.warning("Please select a faculty first")
        return

    st.header("DataShow Management")

    # Create
    with st.expander("Add New DataShow"):
        if st.button("Add DataShow"):
            new_datashow = DataShow()
            state.selected_faculty.list_datashows.append(new_datashow)
            state.save_state()
            st.success("DataShow added successfully")

    # Read
    st.subheader("Existing DataShows")
    for idx, datashow in enumerate(state.selected_faculty.list_datashows):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"DataShow #{idx + 1}")
        with col2:
            if st.button(f"Delete DataShow #{idx + 1}"):
                state.selected_faculty.list_datashows.remove(datashow)
                state.save_state()
                st.success("DataShow deleted successfully")
                st.rerun()


def main():
    st.set_page_config(page_title="University Course Management", layout="wide")
    st.title("University Course Management System")

    # Initialize state
    global state
    state = initialize_state()
    state.load_state()

    st.title("University Course Scheduler")
    pg = st.navigation(
        [
            st.Page(title="Faculties",page = faculty_crud),
            st.Page(title= "Levels",page = level_crud),
            st.Page(title= "Sections",page = section_crud),
            st.Page(title= "Professors",page = professor_crud),
            st.Page(title= "Rooms",page = room_crud),
            st.Page(title= "Modules",page = module_crud),
            st.Page(title= "Pending Sessions",page = pending_session_crud),
            st.Page(title= "DataShows",page = datashow_crud),
        ],
    )
    pg.run()

if __name__ == "__main__":
    main()
