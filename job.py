from dataclasses import dataclass

from company import Company


@dataclass
class Job:
    title:str
    company:Company
    description:str
    location:str
    apply:str
    date:str
    

if __name__ == '__main__':
    job = Job(
        title="Random",
        company=Company.GOOGLE,
        description="Hello",
        location="ranodmasd",
        apply="asd",
        date="asda",
    )