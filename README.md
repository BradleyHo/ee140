# ee140
Programs that I created that are useful for EE 140 at SJSU.

Transmission Line Calculator: Find values of voltage standing wave ratio (VSWR), reflection coefficient (ρ), return loss (RL). Extreme cases were considered. Refer to the relationship table below. This CLI program is written in Python. A GUI version is being considered for Windows and GNU/Linux with more implemented features if time permits.

| Voltage Standing Wave Ratio (VSWR) | Reflection Coefficient (ρ = \|Γ\|) | Return Loss (RL) | Impedance Matching |
| :---: | :---: | :---: | :---: |
| 1.0 | 0 | ∞ dB | Perfectly matched impedance |
| 1.1 | 0.0476 | 26 dB | Good impedance matching |
| 1.5 | 0.2 | 14 dB | Average impedance matching |
| 2.0 | 0.33 | 9.5 dB | Poor impedance matching |
| ∞ | 1 | 0 dB | Open circuit or short circuit |

![EE 140 Homework 10 Chapter 8 Problem 5](https://cdn.discordapp.com/attachments/758422382234042438/915374413258555402/IMG_0085.png)

![Transmission Line Calculator](https://cdn.discordapp.com/attachments/758422382234042438/915189809243377754/transmission-line-calculator.png)
