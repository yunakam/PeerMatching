# Subject/Category/Subcategory List
from typing import Dict

lang_categ = {
        # Ranking retrieved from https://blog.duolingo.com/global-language-report-2020/
        1: "English",
        2: "Spanish",
        3: "French",
        4: "German",
        5: "Italian",
        6: "Japanese",
        7: "Korean",
    }

maths_categ = {
        1: "Arithmetic",
        2: "Geometry",
        3: "Algebra",
        4: "Trigonometry",
        5: "Statistics",
    }

comp_categ = {
        1: "Internet",
        2: "Coding",
        3: "Algorithm",
        4: "Digital Literacy",
    }

arthuman_categ = {
        1: "Literature",
        2: "Politics",
        3: "Society",
        4: "History",
        5: "Philosophy",
    }

business_categ = {
        1: "Macroeconomics",
        2: "Microeconomics",
        3: "Finance",
    }

sub1 = lang_categ
sub2 = maths_categ
sub3 = comp_categ
sub4 = arthuman_categ
sub5 = business_categ
sub_list = ["Subject", sub1, sub2, sub3, sub4, sub5]

# Other attributes

language = {
        1: "English",
        2: "Mandarin",
        3: "Hindi",
        4: "Spanish",
        5: "French",
        6: "Arabic",
        7: "Bengali",
        8: "Russian"
    }

profession: Dict[int, str] = {
        1: "Student (in general)",
        2: "Student (primary)",
        3: "Student (secondary)",
        4: "Student (college)",
        5: "Professional (related to subject)",
        6: "Professional (not related to subject)",
        7: "Job seeker",
        8: "Retired"
    }

purpose = {
        1: "To become professional",
        2: "To improve in my career",
        3: "Just for fun",
}

