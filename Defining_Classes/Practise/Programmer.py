class Programmer:
    def __init__(self, name, language, skills):
            self.name = name
            self.language = language
            self.skills = skills

    def watch_course(self,course_name, language, skills_earned):
        if self.language==language:
            self.skills+=skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self,new_language, skills_needed):
        if self.skills>=skills_needed:
            if self.language!=new_language:
                output= f'{self.name} switched from {self.language} to {new_language}'
                self.language = new_language
                return output
            else:
                return f'{self.name} already knows {self.language}'
        else:
            needed_skills=skills_needed-self.skills
            return f'{self.name} needs {needed_skills} more skills'