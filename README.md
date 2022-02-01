# EE 140 - Principles of Electromagnetic Fields & Waves

               o
          o    |
           \   |
            \  |
             \.|-.
             (\|  )
    .==================.
    | .--------------. |
    | |::.::.::.::.::| |
    | |'::'::'::'::':| |
    | |::.::.::.::.::| |
    | |:'::'::'::'::'| |
    | |::.::.::.::.::| |
    | '--------------'o|
    | RF EE """""""   o|
    |==================|
    |  .------------.  |
    | /              \ |
    |/                \|
    "                  "
    
Hey Spartans! I'm Bradley, one of the EE 140 teaching assistants for the Spring 2022 semester taught by [Dr. Raymond Kwok](https://www.linkedin.com/in/ray-kwok-60bb36) at [SJSU](https://www.sjsu.edu/people/raymond.kwok/). For additional practice problems, visit Professor Kwok's EE 140 [YouTube](https://www.youtube.com/channel/UCHL7NY0OffEIV4KQPrEnP-g) channel with students' solutions to practice problems. The TA session weekly schedule is posted on Google Calendar. You can click [here](https://sjsu.instructure.com/courses/1472264/discussion_topics/4560351) to go to the announcement on SJSU Canvas LMS. If you can't make it to the office hour or the TA sessions, feel free to email us or DM us on Discord. We're here to help you succeed in this challenging course. Below is a simple transmission line calculator that I coded that may be beneficial to you. Other than that, this repository is a placeholder just in case I have more information to be compiled later.

If you are still trying to add, contact the professor for an add code. Make sure your one.SJSU shows that you are enrolled. If you are but can't see the course materials for EE 140 on Canvas LMS, let us know. If you are trying to get a physical textbook, contact the professor ASAP so he can reach out to the print shop to ship them out ASAP. Below are just a few ways/tips to be successful in this class. You don't have to follow these to pass the class (not all students are properly prepared or are at the same level of understanding as one another) but feel free to read on.
- Check the Announcements for important information from the professor and/or TAs
- Follow the lectures, take photos or screenshots (in person or online, respectively)
- If you are able to multitask, then feel free to copy down the notes that the same time but most people can't
- Rewrite the notes a second time at least, if not more (if you have time)
- Redo in-class examples
- Go through the textbook examples and problems
- Redo quizzes, homework problems, and exams. Try to understand why and how you get to the answers, not just memorize
- Study alone first then form study groups and teach each other (if you're a solo kind of person, then follow your own method, you know what's best for you)
- Watch EE 140 videos on Professor Kwok's YouTube channel
- Get in touch if you need additional help: email, Canvas Discussions, Canvas message, Discord server, Discord DM (if you're shy), TA sessions (check weekly calendar), professor office hours (check course syllabus)

Now, the most useful tool you need is a scientific calculator as the professor will/may not allow the usage of graphing calculators or programmable calculators. This may or may not change but I wouldn't chance it. In my semester, most students used the [Casio ClassWiz fx-991EX](https://amzn.to/3L1NjAA) calculator. This is a great calculator to help you with computations as well as having useful functions such as complex number conversions between the polar coordinate system and the Cartesian coordinate system (rectangular coordinate system). Only downside is that if the calculator is turned off, you won't have access to old calculations, i.e. the data are wiped from the RAM. If you prefer a calculator with memory, you can get the [TI-36X Pro](https://amzn.to/3ITZ1eI) (although it's a bit more expensive). One pro is that both scientific calculators are powered using the internal solar cells. I will post basic tutorials on how to use the Casio ClassWiz fx-991EX functions.

> Fun fact: EE 140 used to split up into EE 140 and EE 142. Later, both courses merged into a single course, i.e. EE 140. If you're interested in these materials, consider registering for EE 172.

## Transmission Line Calculator
Find values of voltage standing wave ratio (VSWR), reflection coefficient (ρ), return loss (RL). Extreme cases were considered. Refer to the relationship table below. This CLI program is written in Python. A GUI version is being considered for Windows and GNU/Linux with more implemented features if time permits.

I am aware of the ranges of VSWR, ρ, and RL. I opened an [issue](https://github.com/BradleyHo/ee140/issues/1) and I will commit changes after final exams. Also, I understand that ∞ is not a number. For all intents and purposes, ∞ represents a large number. If you're an EE major, you may know how useful the concept of ∞ is.

| Voltage Standing Wave Ratio (VSWR) | Reflection Coefficient (ρ = \|Γ\|) | Return Loss (RL) | Impedance Matching |
| :---: | :---: | :---: | :---: |
| 1.0 | 0 | ∞ dB | Perfectly matched impedance |
| 1.1 | 0.0476 | 26 dB | Good impedance matching |
| 1.5 | 0.2 | 14 dB | Average impedance matching |
| 2.0 | 0.33 | 9.5 dB | Poor impedance matching |
| ∞ | 1 | 0 dB | Open circuit or short circuit |

![EE 140 Homework 10 Chapter 8 Problem 5](https://cdn.discordapp.com/attachments/758422382234042438/915374413258555402/IMG_0085.png)

![Transmission Line Calculator](https://cdn.discordapp.com/attachments/758422382234042438/915189809243377754/transmission-line-calculator.png)
---
## Greek Alphabet

The Greek alphabet is used along with other alphabet systems such as the English alphabet in mathematics, science, and engineering discisplines. There are many ways to pronounce the Greek alphabet letters. Even in American English, there may be multiple accepted pronunciations for certain letters. Whatever floats your boat. 😊


| Greek Letter Name | Uppercase Letter | Lowercase Letter | American English Pronunciation |
| :---: | :---: | :---: | :---: |
| Alpha | Α | α | /ˈælfə/ (AL fuh) |
| Beta | Β | β | /ˈbeɪtə/ (BAY tuh) |
| Gamma | Γ | γ | /ˈɡæmə/ (GAM uh) |
| Delta | Δ | δ | /ˈdɛltə/ (DELL tuh) |
| Epsilon | Ε | ε | /ˈɛpsɨlɒn/ (EP suh lon) |
| Zeta | Ζ | ζ | /ˈzeɪtə/ (ZAY tuh) |
| Eta | Η | η | /ˈeɪtə/ (AY tuh) |
| Theta | Θ | θ | /ˈθeɪtə/ (THAY tuh) |
| Iota | Ι | ι | /aɪˈoʊtə/ (eye OH tuh) |
| Kappa | Κ | κ | /ˈkæpə/ (CAP uh) |
| Lambda | Λ | λ | /ˈlæmdə/ (LAM duh) |
| Mu | Μ | μ | /ˈmjuː/, /ˈmuː/ (MYOO, MOO) |
| Nu | Ν | ν | /ˈnuː/ (NOO) |
| Xi | Ξ | ξ | /ˈzaɪ/, /ˈksaɪ/ (ZIGH, KS EYE, KSEE) |
| Omicron | Ο | ο | /ˈɒmɨkrɒn/ (AH mih cron, OH mih cron) |
| Pi | Π | π | /ˈpaɪ/ (PIE) |
| Rho | Ρ | ρ | /ˈroʊ/ (ROE) |
| Sigma | Σ | σ | /ˈsɪɡmə/ (SIG muh) |
| Tau | Τ | τ | /ˈtaʊ/, /ˈtɔː/ (TOW rhyming with COW, TAW rhyming with LAW) |
| Upsilon | Υ | υ | /ˈʌpsɨlɒn/ (UP suh lon) |
| Phi | Φ | φ | /ˈfaɪ/, /ˈfiː/ (FIE, FEE) |
| Chi | Χ | χ | /ˈkaɪ/ (KIGH, KEE) |
| Psi | Ψ | ψ | /ˈsaɪ/, /ˈpsaɪ/, /ˈsiː/ (SIGH, PSIGH, PSEE) |
| Omega | Ω | ω | /oʊˈmeɪɡə/ (oh MAY guh) |

Sigma also has another lowercase letter ς for word-final position that may be used in STEM subjects as a symbol although in EE 140, we'll be using σ exclusively.

---
## Final Examination

Fall 2021 Semester Topics:
* Definite Integrals
* Magnetostatics
* Biot–Savart Law
* Boundary Conditions
* Faraday's Law
* Maxwell's Equations
* Plane Waves & Polarization
* Lossy Media
* Normal Incidence
* Transmission Lines

![Formula Sheet 1](https://cdn.discordapp.com/attachments/822377994978459729/915524286482100276/formula-sheet-1.JPG)
![Formula Sheet 2](https://cdn.discordapp.com/attachments/822377994978459729/915524286930886706/formula-sheet-2.JPG)

---
## Final Examination

Spring 2022 Semester Topics:
* Definite Integrals
* Magnetostatics
* Biot–Savart Law
* Boundary Conditions
* Faraday's Law
* Maxwell's Equations
* Plane Waves & Polarization
* Lossy Media
* Normal Incidence
* Transmission Lines

![Formula Sheet 1](https://cdn.discordapp.com/attachments/822377994978459729/915524286482100276/formula-sheet-1.JPG)
![Formula Sheet 2](https://cdn.discordapp.com/attachments/822377994978459729/915524286930886706/formula-sheet-2.JPG)
