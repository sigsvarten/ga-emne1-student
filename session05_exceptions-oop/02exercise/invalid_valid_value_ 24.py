# int() konverterer brukerens svar til et heltall.
# except ValueError fanger opp feil hvis brukeren skriver noe som ikke er et heltall.
# else kjøres bare dersom konverteringen lykkes.
# if 1 <= antall <= 8 kontrollerer at antallet billetter er innenfor gyldig intervall.
# Totalprisen beregnes med antall * 120 og vises kun når bestillingen er gyldig

# eight førere til ein exception ved int('eight')
#fordi 9 for eks ikkje førre til ein exception siden det er ein int og vil fungere
# på grunn av det trenge vi ein if - setning