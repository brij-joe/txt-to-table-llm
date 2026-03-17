from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, HttpUrl


class DatesOfEmployment(BaseModel):
    startDate: Optional[str] = Field(None, description="Employment start date (YYYY-MM-DD).")
    endDate: Optional[str] = Field(None, description="Employment end date (YYYY-MM-DD).")


class WorkExperience(BaseModel):
    jobTitle: str = Field(..., description="Specific roles held (e.g., 'Senior Software Engineer, Vice President etc.').")
    companyName: str = Field(..., description="Organizations where the candidate was employed.")
    datesOfEmployment: DatesOfEmployment = Field(..., description="Start and end dates of employment.")
    keyResponsibilities: Optional[List[str]] = Field(None, description="Bullet points outlining accomplishments.")
    quantifiedMetrics: Optional[List[str]] = Field(None, description="Percentages, dollar amounts, or numbers showing impact.")


class Education(BaseModel):
    degreeType: str = Field(..., description="Bachelor’s, Master’s, PhD.")
    majorFieldOfStudy: Optional[str] = Field(None, description="Areas of academic specialization.")
    universityName: str = Field(..., description="Institution where the degree was obtained.")
    graduationYear: Optional[int] = Field(None, description="Year of graduation, often used to gauge seniority.")
    relevantCourseworkOrProjects: Optional[List[str]] = Field(None, description="Details for recent graduates or specialized roles.")


class Skills(BaseModel):
    hardSkills: Optional[List[str]] = Field(None, description="Specific software, tools, languages, or specialized machinery (e.g., Python, AWS, Agile).")
    softSkills: Optional[List[str]] = Field(None, description="Interpersonal and professional skills (e.g., Leadership, Communication).")
    certifications: Optional[List[str]] = Field(None, description="Valid credentials required for specialized roles (e.g., CPA, PMP, RN).")


class OtherAttributes(BaseModel):
    languagesKnown: Optional[List[str]] = Field(None, description="Language proficiency levels, essential for global roles.")
    professionalSummary: Optional[str] = Field(None, description="Brief paragraph highlighting qualifications.")
    awardsAndPublications: Optional[List[str]] = Field(None, description="Special recognitions and industry contributions.")


class PersonalInformation(BaseModel):
    fullName: str = Field(..., description="Standard identification of the candidate.")
    emailAddress: EmailStr = Field(..., description="Essential for reaching out to candidates.")
    phoneNumber: Optional[str] = Field(None, description="Mobile or direct lines.")
    location: Optional[str] = Field(None, description="City/State, often used to check if the candidate is local or requires relocation.")
    linkedinOrPortfolioUrl: Optional[HttpUrl] = Field(None, description="Professional social media or portfolio websites.")


class CandidateProfile(BaseModel):
    personalInformation: PersonalInformation = Field(None, description="Basic personal details of the candidate.")
    workExperience: Optional[List[WorkExperience]] = Field(None, description="Professional history of the candidate.")
    education: Optional[List[Education]] = Field(None, description="Academic background of the candidate.")
    skills: Optional[Skills] = Field(None, description="Technical and soft skills of the candidate.")
    otherAttributes: Optional[OtherAttributes] = Field(None, description="Additional important attributes of the candidate.")
