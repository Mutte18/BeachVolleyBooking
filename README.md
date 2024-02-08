# Bokningshemsida för Beachvolley i Skövde

## Krav:
* Betalande medlemmar ska kunna boka planer utan kostnad
* Skapa ett konto genom hemsidan, och får ett email skickat till en med en verifieringslänk
* Vid framtida inloggningar skriver man email, och får ett email skickat till en med inloggningslänk 
(för att slippa hantera lösenord)
* IdrottOnline ska komma med ett API man kan hämta personuppgifter via - fram tills dess kan vi använda Excel/Databas
* För att bli medlem ska man kunna swisha till föreningen och bli aktiv för säsongen
* 


## Uppgifter som behövs vid registrering av ett konto:
* För och efternamn
* Personnummer
* Emailaddress
* Lösenord(?)



## Tekniker för detta projekt:
* Docker (för lokal miljö)
* Python (backend)
* Vue eller Angular (frontend)
* MySQL (databas)
* Swish integration
* Webbserver
* Webbdomän
* Test-sida?
* Github Actions (CI-CD)
* Testning
* Bcrypt för kryptera lösenord


## Vad en användare ska kunna göra på sidan:
* Registrera konto
* Logga in
* Betala medlemskap
* Boka plan
* Ta bort bokning
* Ändra bokningstid
* Läsa information om föreningen
* Se karta vart planerna är
* Se GDPR information

## Vad en Admin ska kunna göra på sidan:
* Blockera användare
* Återaktivera användare
* Ge medlemskap manuellt till användare
* Ta bort medlemskap från användare
* Ta bort bokning
* Boka åt någon annan
* Lista på alla användare
* 


# Komponenter som behövs:
Endpoints i Python:
* Login
* Logout
* verifyEmail
* Reset password
* encryptPassword
* Starta swish betalning
* createAccount
* blockAccount
* unblockAccount
* payMembership
* bookACourt
* removingBooking
* editBooking

# Databas tabeller:
* sessions?
* accounts
* passwords
* user_information
* membership
* bookings
* court_schedule