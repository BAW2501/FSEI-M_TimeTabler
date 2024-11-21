import pandas as pd
import streamlit as st
from Def import (
    Faculty,
    Group,
    Level,
    Module,
    PendingSession,
    Professor,
    Room,
    RoomType,
    Section,
    SessionType,
)
from LoadData import load_data_from_json


class UniversityScheduler:
    def __init__(self):
        fac = load_data_from_json("data.json")
        if "faculties" not in st.session_state:
            st.session_state.faculties = [fac]
        if "current_faculty" not in st.session_state:
            st.session_state.current_faculty = fac

    @property
    def current_faculty(self) -> Faculty | None:
        return st.session_state.current_faculty

    @current_faculty.setter
    def current_faculty(self, value: Faculty | None) -> None:
        st.session_state.current_faculty = value

    def main(self):
        st.title("University Course Scheduler")
        pg = st.navigation(
            [
                st.Page(self.faculty_management, title="Faculties"),
                st.Page(self.promotion_management, title="Promotions"),
                st.Page(self.section_management, title="Sections"),
                st.Page(self.professor_management, title="Professors"),
                st.Page(self.room_management, title="Rooms"),
                st.Page(self.session_management, title="Sessions"),
            ],
        )
        pg.run()

    def faculty_management(self):
        st.header("Faculty Management")

        # Add new faculty
        with st.form("add_faculty"):
            faculty_name = st.text_input("Faculty Name")
            submit = st.form_submit_button("Add Faculty")

            if submit and faculty_name:
                new_faculty = Faculty(name=faculty_name)
                st.session_state.faculties.append(new_faculty)
                st.success(f"Faculty {faculty_name} added successfully!")

        # List existing faculties
        if st.session_state.faculties:
            st.subheader("Existing Faculties")
            for faculty in st.session_state.faculties:
                col1, col2 = st.columns([4, 1])
                with col1:
                    col11, col12, col13, col14 = st.columns(4)

                    col11.write(faculty.name)
                    col12.metric("Students", faculty.number_students)
                    col13.metric("Professors", faculty.number_professors)
                    col14.metric("Rooms", faculty.number_rooms)
                with col2:
                    if st.button("Select", key=f"select_{faculty.name}"):
                        self.current_faculty = faculty
                        st.success(f"Selected faculty: {faculty.name}")

    def promotion_management(self):
        st.header("Promotion Management")

        if not self.current_faculty:
            st.warning("Please select a faculty first!")
            return

        # Create tabs for Promotions and Modules
        promotion_tab, module_tab = st.tabs(["Promotions", "Modules"])

        with promotion_tab:
            # Add new promotion
            with st.form("add_promotion"):
                level = st.text_input("Promotion Level")
                submit = st.form_submit_button("Add Promotion")

                if submit and level:
                    new_promotion = Level(name=level)
                    self.current_faculty.list_promo.append(new_promotion)
                    st.success(f"Promotion {level} added successfully!")

            # List existing promotions
            if self.current_faculty.list_promo:
                st.subheader("Existing Promotions")
                st.table(promo.name for promo in self.current_faculty.list_promo)

        with module_tab:
            # Select promotion for module management
            if self.current_faculty.list_promo:
                selected_promotion = st.selectbox(
                    "Select Promotion",
                    self.current_faculty.list_promo,
                    format_func=lambda x: x.name,
                    key="module_promotion_select",
                )

                if selected_promotion:
                    # Add new module
                    with st.form("add_module"):
                        st.subheader("Add New Module")
                        col1, col2 = st.columns(2)

                        with col1:
                            module_name = st.text_input("Module Name")
                            module_abbr = st.text_input("Module Abbreviation")

                        with col2:
                            nb_lecture = st.number_input(
                                "Number of Lectures",
                                min_value=0,
                                value=0,
                            )
                            nb_td = st.number_input(
                                "Number of Tutorial Sessions",
                                min_value=0,
                                value=0,
                            )
                            nb_tp = st.number_input(
                                "Number of Lab Sessions",
                                min_value=0,
                                value=0,
                            )

                        submit_module = st.form_submit_button("Add Module")

                        if submit_module and module_name and module_abbr:
                            new_module = Module(
                                name=module_name,
                                abbreviation=module_abbr,
                                semester=1,
                                number_of_lectures=nb_lecture,
                                number_of_tutorials=nb_td,
                                number_of_labs=nb_tp,
                            )
                            selected_promotion.curriculum.append(new_module)
                            st.success(f"Module {module_name} added successfully!")

                    # Display existing modules
                    if selected_promotion.curriculum:
                        st.subheader("Existing Modules")

                        df = pd.DataFrame(selected_promotion.curriculum)
                        st.table(df)

                        # Add delete functionality
                        if st.button("Clear All Modules"):
                            selected_promotion.curriculum.clear()
                            st.success("All modules have been removed")
                            st.rerun()
                    else:
                        st.info("No modules added yet for this promotion.")
            else:
                st.warning("Please add a promotion first!")

    def professor_management(self):
        st.header("Professor Management")

        if not self.current_faculty:
            st.warning("Please select a faculty first!")
            return

        # Add new professor
        with st.form("add_professor"):
            prof_name = st.text_input("Professor Name")
            submit = st.form_submit_button("Add Professor")

            if submit and prof_name:
                new_professor = Professor(name=prof_name)
                self.current_faculty.list_profs.append(new_professor)
                st.success(f"Professor {prof_name} added successfully!")

        # List existing professors
        if self.current_faculty.list_profs:
            st.subheader("Existing Professors")
            # for professor in self.current_faculty.list_profs:
            #     st.write(
            #         f"Name: {professor.name}",
            #     )
            st.table(pd.DataFrame(self.current_faculty.list_profs))

    def room_management(self):
        st.header("Room Management")

        if not self.current_faculty:
            st.warning("Please select a faculty first!")
            return

        # Add new room
        with st.form("add_room"):
            room_name = st.text_input("Room Name")
            room_type = st.selectbox("Room Type", [type.name for type in RoomType])
            capacity = st.number_input("Capacity", min_value=1)
            submit = st.form_submit_button("Add Room")

            if submit and room_name:
                new_room = Room(
                    name=room_name,
                    room_type=RoomType[room_type],
                    capacity=capacity,
                )
                self.current_faculty.list_rooms.append(new_room)
                st.success(f"Room {room_name} added successfully!")

        # List existing rooms
        if self.current_faculty.list_rooms:
            st.subheader("Existing Rooms")
            st.table(self.current_faculty.list_rooms)

    def section_management(self):
        st.header("Section Management")

        if not self.current_faculty:
            st.warning("Please select a faculty first!")
            return

        # Select promotion
        if self.current_faculty.list_promo:
            selected_promotion = st.selectbox(
                "Select Promotion",
                self.current_faculty.list_promo,
                format_func=lambda x: x.name,
                key="section_promotion_select",
            )

            if selected_promotion:
                # Create sections and groups tab
                create_tab, view_tab = st.tabs(["Create Sections", "View Sections"])

                with create_tab:
                    with st.form("add_sections"):
                        st.subheader("Create Multiple Sections with Groups")

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            num_sections = st.number_input(
                                "Number of Sections ",
                                min_value=1,
                                value=1,
                                help="Total number of sections to create",
                            )

                        with col2:
                            groups_per_section = st.number_input(
                                "Groups per Section ",
                                min_value=1,
                                value=2,
                                help="Number of groups to create in each section",
                            )

                        with col3:
                            students_per_group = st.number_input(
                                "Students per Group",
                                min_value=1,
                                value=25,
                                help="Number of students in each group",
                            )

                        starting_section_number = st.number_input(
                            "Starting Section Number",
                            min_value=1,
                            value=1,
                            help="The number for the first section",
                        )

                        submit = st.form_submit_button("Create Sections and Groups")

                        if submit:
                            print(
                                f"{num_sections=}{groups_per_section=}{students_per_group=}",
                            )
                            selected_promotion.list_section = []

                            # Create sections and groups
                            for i in range(num_sections):
                                section_num = starting_section_number + i
                                new_section = Section(number=section_num)

                                # Create groups for this section
                                for j in range(groups_per_section):
                                    group_number = j + 1 + (i * groups_per_section)
                                    new_group = Group(
                                        number=group_number,
                                        effective=students_per_group,
                                    )
                                    new_section.list_group.append(new_group)

                                selected_promotion.list_section.append(new_section)

                            st.success(
                                f"Successfully created {num_sections} sections with {groups_per_section} groups each!",
                            )
                            st.rerun()

                with view_tab:
                    if selected_promotion.list_section:
                        st.subheader("Existing Sections and Groups")

                        # Create a structured view of sections and groups
                        for section in selected_promotion.list_section:
                            with st.expander(f"Section {section.number}"):
                                if section.list_group:
                                    # Create a DataFrame for groups in this section

                                    df = pd.DataFrame(section.list_group)
                                    df.set_index("number", inplace=True)

                                    st.table(df)

                                    # Summary statistics
                                    total_students = sum(
                                        group.effective for group in section.list_group
                                    )
                                    st.info(
                                        f"Total students in section: {total_students}",
                                    )
                                else:
                                    st.warning("No groups in this section")

                            # Add delete button for each section
                            if st.button(
                                f"Delete Section {section.number}",
                                key=f"del_section_{section.number}",
                            ):
                                selected_promotion.list_section.remove(section)
                                st.success(
                                    f"Section {section.number} deleted successfully!",
                                )
                                st.rerun()
                    else:
                        st.info("No sections created yet for this promotion.")
        else:
            st.warning("Please add a promotion first!")

    def session_management(self):
        st.header("Session Management")
        professor = None
        promotion = None
        section = None
        module = None

        if not self.current_faculty:
            st.warning("Please select a faculty first!")
            return

        # Add new pending session
        with st.form("add_session"):
            # Select professor

            professor = st.selectbox(
                "Select Professor",
                self.current_faculty.list_profs,
                format_func=lambda x: x.name,
            )

            # Select promotion and section
            promotion = st.selectbox(
                "Select Promotion",
                self.current_faculty.list_promo,
                format_func=lambda x: x.name,
            )

            # Select module from promotion's curriculum
            if promotion:
                module = st.selectbox(
                    "Select Module",
                    promotion.curriculum,
                    format_func=lambda x: x.name,
                )

            session_type = st.selectbox(
                "Session Type",
                [type.name for type in SessionType],
            )

            submit = st.form_submit_button("Add Session")

            if submit and professor and section and module:
                new_session = PendingSession(
                    prof=professor,
                    attendance=section,
                    module=module,
                    session_type=SessionType[session_type],
                )
                promotion.required_sessions.append(new_session)
                st.success("Session added successfully!")


def main():
    scheduler = UniversityScheduler()
    scheduler.main()


if __name__ == "__main__":
    main()
