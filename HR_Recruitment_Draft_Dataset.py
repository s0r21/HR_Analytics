# the script that shows the dataset & data frame
from packages import np, pd, extract_text

# defining all the functions needed for the dataset
    # Normalization function
def normalization(mean, std, resume):
    if mean == 0:
        normalized_values = 0
    else:
        normalized_values = (np.mean(resume) - mean) / std
    return (normalized_values)

def total_score(requirements, responsibility, nice_to_have):
    if nice_to_have == "":
        x = (requirements + responsibility)/2 # (0.60 * requirements) + (0.40 * responsibility)
    else:
        x = (requirements + responsibility + nice_to_have)/3 #(0.55 * requirements) + (0.40 * responsibility) + (0.05 * nice_to_have)
    return x

    # Extracting the text from the pdf
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

    # Getting the resumes into a df / array
def words_to_numbers(resume):
    str_to_num_array = []
    resume = ''.join(ch for ch in resume if ch.isalnum())
    for bad_chars in unwanted_characters_two:
        resume = resume.replace(bad_chars, "")
    for i in resume:
        str_to_num_array.append(Dictionary[i])
    pd.DataFrame(str_to_num_array)
    if not resume:
        str_to_num_array = [0]
    return(str_to_num_array)

# This is a dictionary. Basically, you're referencing a letter to a number. This is mainly for resume processing.
Dictionary =  {
    "A":1, "a":1, "B":2, "b":2,"C":3,"c":3,"D":4,"d":4 ,"E":5,"e":5, "F":6,"f":6 , "G":7, "g":7, "H":8, "h":8,"I":9, "i":9,"J":10, "j":10,
    "K":11, "k":11, "L":12, "l":12, "M":13, "m":13,"N":14, "n":14, "O":15, "o":15, "P":16, "p":16,"Q":17, "q":17, "R":18, "r":18, "S":19, "s":19,"T":20, "t":20,
    "U":21, "u":21, "V":22, "v":22, "W":23, "w":23,"X":24, "x":24, "Y":25, "y":25, "Z":26, "z":26
}

unwanted_characters = ['\n', ' ', '-', ',', '.', '|', '1',
                       '2', '3', '4', '5', '6', '7', '8',
                       '9', '0', '/', '\xa0', "'", "&",
                       "(", ")", ";", ":", "_", "@", "\x0c",
                       "+", "-", "#", "*", "!", "$", "%","’", "•"]

unwanted_characters_two = ['1',
                           '2', '3', '4', '5', '6', '7', '8',
                           '9', '0', 'Ø', 'É', 'è']

responsibilities_for_position = input('Please enter the responsibilities for the position')
requirements_for_position = input('Please enter the requirements for the position')
nice_to_have = input('Please enter the "nice to haves" for the position')

# Fullscript Position
# Requirements_for_position = "• Ongoing help with troubleshooting workstations. You will create and solve tickets, and use triage judgment to set priority levels for different tasks." \
#                         "• Take inventory to the Apple Store for certain hardware repairs." \
#                         "• Assist in the procurement of hardware for the office. Every workstation is equipped with a new display, laptop, keyboard, mouse, and stand." \
#                         "• Troubleshoot and resolve any network-related issues. Familiarity with Cisco, Ubiquiti, Fortigate and ISP Gateways is key." \
#                         "• Provide ongoing support for different cloud-based systems as an admin; responsible for resetting passwords and providing a different level of privileged access." \
#                         "• Performing weekly, monthly and quarterly audits on integral systems to ensure there are no security vulnerabilities." \
#                         "• On-boarding and training for all new employees." \
#                         "• Work closely with team-leads to assist with the integration of new procedures, platforms, and policies." \
#                         "• Maintain inventory asset management of all owned hardware."

# requirements_for_position = "• You have 2+ years of experience in an IT or technical support function." \
#                             "• You have a diploma in Computer Systems Technology or equivalent experience." \
#                             "• Experience in supporting Mac OS, Linux, and Windows Operating Systems." \
#                             "• You’re passionate about the latest tech; you’re an early adopter and love to test out new gadgets." \
#                             "• You’re a lover of all things Apple." \
#                             "• You have strong organizational skills, and love to take initiative." \
#                             "• You have a strong understanding of networking technology (TCP/IP, Subnet Calculation, DNS, VPN, DCHP, Routing, and Switches)." \
#                             "• You’ve worked with software such as JAMF, Samanage, Zendesk and/or Okta." \
#                             "• You’re willing to step out of your comfort zone to learn new things to support our team." \
#                             "• You are an honorary member of the AV club. We live stream every single townhall to all our remote workers and need your help running the rig to do so." \
#                             "• Impress Us With" \
#                             "• ACMT Certification" \
#                             "• Network+ Certification (or Equivalent)" \
#                             "• A+ Certification" \
#                             "• Basic programming knowledge. Scripting in Ruby or Python is a plus but not required."

# if you want to sum the dictionary values
# for i in word.replace(" ", ""):
#     x += Dictionary[i]

# Note: Add Corey, Abe, Kevin's resume to the stockpile

Dirs_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Jiriuss_Resume_.pdf")
Sors_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Sorena Talebizadeh Resume.pdf")
Henrys_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/resume-31.pdf")
Payals_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Payal Vinayak Resume 2021.pdf")
Sinas_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Sina Varahram - Resume.pdf")
Coreys_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/CoreyHum.pdf")
Kevins_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Kevin Emmanuel-Resume.pdf")
Adams_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Adam_Viola_CV_2021.pdf")
Abes_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Abe Sayed Resume.pdf")
# Note: Test_resume is about 120 pages of "lllllllllllllll" formatted into PDF. I just wanted to make sure that if someone spams a bunch of pages,
# it does not return a good result.
Test_resume = extract_text_from_pdf("C:/Users/t0ys0r/OneDrive/Desktop/Data Science & Analytics Practice/HR Analytics/Resumes/Test Resume.pdf")

posting_responsibilities = words_to_numbers(responsibilities_for_position)
posting_requirements = words_to_numbers(requirements_for_position)
posting_nice_for_position = words_to_numbers(nice_to_have)
dirs_resume_return = words_to_numbers(Dirs_resume)
sors_resume_return = words_to_numbers(Sors_resume)
henrys_resume_return = words_to_numbers(Henrys_resume)
payals_resume_return = words_to_numbers(Payals_resume)
sinas_resume_return = words_to_numbers(Sinas_resume)
coreys_resume_return = words_to_numbers(Coreys_resume)
kevins_resume_return = words_to_numbers(Kevins_resume)
adams_resume_return = words_to_numbers(Adams_resume)
abes_resume_return = words_to_numbers(Abes_resume)
test_resume_return = words_to_numbers(Test_resume)

# jobs_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), posting_requirements)
# jobs_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), posting_responsibilities)
# jobs_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), posting_nice_for_position)

dirs_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), dirs_resume_return)
dirs_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), dirs_resume_return)
dirs_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), dirs_resume_return)
# dirs_total_score = total_score()
sors_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), sors_resume_return)
sors_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), sors_resume_return)
sors_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), sors_resume_return)
# sors_total_score = total_score()
henrys_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), henrys_resume_return)
henrys_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), henrys_resume_return)
henrys_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), henrys_resume_return)

payals_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), payals_resume_return)
payals_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), payals_resume_return)
payals_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), payals_resume_return)

sinas_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), sinas_resume_return)
sinas_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), sinas_resume_return)
sinas_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), sinas_resume_return)

coreys_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), coreys_resume_return)
coreys_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), coreys_resume_return)
coreys_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), coreys_resume_return)

kevins_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), kevins_resume_return)
kevins_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), kevins_resume_return)
kevins_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), kevins_resume_return)

adams_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), adams_resume_return)
adams_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), adams_resume_return)
adams_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), adams_resume_return)

abes_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), abes_resume_return)
abes_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), abes_resume_return)
abes_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), abes_resume_return)

tests_requirements_return = normalization(np.mean(posting_requirements), np.std(posting_requirements), test_resume_return)
tests_resposibility_return = normalization(np.mean(posting_responsibilities), np.std(posting_responsibilities), test_resume_return)
tests_nice_return = normalization(np.mean(posting_nice_for_position), np.std(posting_nice_for_position), test_resume_return)

# Make this into a funciton
data = {'Name': [# 'Job',
                 'Dir', 'Sor', 'Henry', 'Payal', 'Sina', 'Corey', 'Kevin', 'Adam', 'Abes', 'Test'],
        'Requirements': [
            #jobs_requirements_return,
            dirs_requirements_return, sors_requirements_return, henrys_requirements_return,
            payals_requirements_return, sinas_requirements_return, coreys_requirements_return,
            kevins_requirements_return, adams_requirements_return, abes_requirements_return,
            tests_requirements_return
        ],
        'Responsibilities': [
            #jobs_resposibility_return,
            dirs_resposibility_return, sors_resposibility_return, henrys_resposibility_return,
            payals_resposibility_return, sinas_resposibility_return, coreys_resposibility_return,
            kevins_resposibility_return, adams_resposibility_return, abes_resposibility_return,
            tests_resposibility_return
        ],
        'Nice to have': [
            # jobs_nice_return,
            dirs_nice_return, sors_nice_return, henrys_nice_return,
            payals_nice_return, sinas_nice_return, coreys_nice_return, kevins_nice_return,
            adams_nice_return, abes_nice_return, tests_nice_return
        ],
        'Total Average': [
            # total_score(jobs_requirements_return, jobs_resposibility_return, jobs_nice_return),
            total_score(dirs_requirements_return, dirs_resposibility_return, dirs_nice_return),
            total_score(sors_requirements_return, sors_resposibility_return, sors_nice_return),
            total_score(henrys_requirements_return, henrys_resposibility_return, henrys_nice_return),
            total_score(payals_requirements_return, payals_resposibility_return, payals_nice_return),
            total_score(sinas_requirements_return, sinas_resposibility_return, sinas_nice_return),
            total_score(coreys_requirements_return, coreys_resposibility_return, coreys_nice_return),
            total_score(kevins_requirements_return, kevins_resposibility_return, kevins_nice_return),
            total_score(adams_requirements_return, adams_resposibility_return, adams_nice_return),
            total_score(abes_requirements_return, abes_resposibility_return, abes_nice_return),
            total_score(tests_requirements_return, tests_resposibility_return, tests_nice_return)
        ] }

data_df = pd.DataFrame(data).sort_values(by='Total Average', ascending=True).reset_index(drop=True)
data_df.replace('NaN', 0)

data_df_KNN = data_df


# Ideal_candidates_using_normalization = data_df_KNN.loc[data_df_KNN['Condition'] == 1]

print(data_df)